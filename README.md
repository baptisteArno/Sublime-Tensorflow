# Sublime Tensorflow

Tensorflow plugin for Sublime Text editor.

# Installation #

Sublime Tensorflow can be installed: 
* Through Sublime Package Control 
* Manually by cloning this repo and copy/paste in a folder into the Sublime Text packages directory.

# Usage #

Sublime Tensorflow offers you: 
* Autocompletion from a list scrapped from official Tensorflow API documentation.
* Shortcut to check the doc by selecting the Tensorflow class/function and:
  * Linux: `ctrl + shift + t`
  * Windows: `ctrl + alt + t`
  * OSX: `ctrl + cmd + t`
  
# Config #

You can change the shortcut by editing the keymap file accessible from *Preferences->Package Settings->Sublime Tensorflow->Settings - User*

The correct syntax is the following:

```
[
    {
        "keys": ["ctrl+shift+t"],
        "command": "tfdoc"
    }
]
```
  
