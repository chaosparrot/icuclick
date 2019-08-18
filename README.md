# ICUClick
This program is a data collection tool to retrieve mouse clicks with their corresponding UI elements.
To spin it up, just run `py detect.py` , afterwards, run `py process.py` to turn the raw screenshots into smaller processable images

Default processed size is 128x128 , but you can alter it by changing the process.py file

# Software requirements
* Python 3
* numpy
* pyautogui
* win32api for windows
* PIL

Mac / linux not yet supported :(