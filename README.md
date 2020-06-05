[![HitCount](http://hits.dwyl.com/xinabox/mu-editor.svg)](http://hits.dwyl.com/xinabox/mu-editor)

# mu-editor
☒ version of the mu-editor from codewith.mu

# Downloads 
- [MacOS](https://github.com/xinabox/mu-editor/releases/download/v1.1.0a2/mu-editor.dmg)
- [Windows 64bit](https://github.com/xinabox/mu-editor/releases/download/v1.1.0a2/mu-editor_64bit.exe)
- Find them here: https://github.com/xinabox/mu-editor/releases/latest

## Temporary Release
This version of mu-editor found in this release is only temporary, as the main mu-editor undergoes some longer term changes. Our Pull Request can therefore not be honoured now, so we are releasing this XinaBox version instead. This will be removed as soon as our changes is incorporated into the main mu-editor.

## Special Note regarding CW01
The CW01 doesn't have an "auto resetting" circutry on it like the CW02 has, therefore the the CW01 will be stuck in "bootloader" mode when inserted into your computer with a standard IP01. However if you have an old IP01 with switches, then you can bypass that by setting the A-B switch in position `A` when programming the CW01 using mu-editor. And when loading the MicroPython using the [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest), the switches should be in `B` and `DCE`
