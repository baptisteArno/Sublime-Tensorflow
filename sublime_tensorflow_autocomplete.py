import re
import sublime
import sublime_plugin
import webbrowser
from .helper import get_tf_functions

RE_TRIGGER_BEFORE = re.compile(
    r"\w*(\.[\w\.]+)"
)

tf_functions = get_tf_functions()


class TensorflowAutocomplete(sublime_plugin.EventListener):

    def __init__(self):

        self.tf_completions = [
            ("%s \tTensorflow" % s, s.replace("()", "($1)"))
            for s in tf_functions
        ]

    def on_query_completions(self, view, prefix, locations):

        loc = locations[0]
        if not view.match_selector(loc, 'source.python'):
            return

        completions = self.tf_completions
        # get the inverted line before the location
        line_before_reg = sublime.Region(view.line(loc).a, loc)
        line_before = view.substr(line_before_reg)[::-1]

        # check if it matches the trigger
        m = RE_TRIGGER_BEFORE.match(line_before)
        if m:
            # get the text before the .
            trigger = m.group(1)[::-1]
            # filter and strip the completions
            completions = [
                (c[0], c[1][len(trigger):])
                for c in completions
                if c[1].startswith(trigger)
            ]

        return completions


class TensorflowDocCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        is_auto_selection = False
        selection = ""
        regions = self.view.sel()

        if len(regions) == 1 and len(regions[0]) == 0:
            selection = self.view.substr(
                self.extend_point_by_allowed_chars(
                    point=regions[0].a,
                    allowed_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._',
                )
            )
            is_auto_selection = True
        else:
            for region in self.view.sel():
                selection += self.view.substr(region)

        if selection + "()" in tf_functions:
            selec_link = selection.replace('.', '/')
            webbrowser.open("https://www.tensorflow.org/api_docs/python/%s" % selec_link)
        elif not is_auto_selection:
            sublime.error_message(
                "'%s' is not a Tensorflow class or function.\n"
                "Here is an example of what can be selected: 'tf.nn.conv2d'"
                % (selection)
            )

    def extend_point_by_allowed_chars(self, point, allowed_chars):
        bound_l = bound_r = point
        # extend left
        while self.view.substr(bound_l) in allowed_chars:
            bound_l -= 1
        # extend right
        while self.view.substr(bound_r) in allowed_chars:
            bound_r += 1
        return sublime.Region(bound_l+1, bound_r)
