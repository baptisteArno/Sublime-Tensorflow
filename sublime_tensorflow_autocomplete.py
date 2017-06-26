import sublime_plugin
import sublime

tensorflow_functions = ["tf.test", "tf.camarche", "tf.mdr"]

class TensorflowCompletions(sublime_plugin.EventListener):

	def __init__(self):

		self.tf_completions = [("%s \tTensorflow" % s, s) for s in tensorflow_functions]

	def on_query_completions(self, view, prefix, locations):

		if view.match_selector(locations[0], "source.py"):

			return self.tf_completions

		else:

			return []