# Sublime Tensorflow

Tensorflow plugin for Sublime Text editor.

## Installation ##

Sublime Tensorflow can be installed: 
* Through Sublime Package Control. Package name: *Tensorflow*
* Manually by cloning this repo and copy/paste in a folder into the Sublime Text packages directory.

## Usage ##

Sublime Tensorflow offers you: 
* Autocompletion from a list scrapped from official Tensorflow API documentation.
* Shortcut to check the doc by selecting the Tensorflow class/function and:
  * Windows & Linux: `ctrl + alt + w`
  * OSX: `ctrl + cmd + w`
  
## Configuration ##

You can change the shortcut by editing the keymap file accessible from *Preferences->Package Settings->Sublime Tensorflow->Settings - User*

The correct syntax is the following:

```
[
    {
        "keys": ["ctrl+alt+w"],
        "command": "tfdoc"
    }
]
```
  
