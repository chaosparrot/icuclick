# Code to check if left or right mouse buttons were pressed
import win32api
import time
import pyautogui
import numpy
from win32gui import WindowFromPoint, GetWindowRect

pyautogui.PAUSE = 0
pyautogui.FAILSAVE = False

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

large_movement_picture = None
movement_start_time = None
previous_position = pyautogui.position()
window_bounds = GetWindowRect( WindowFromPoint( (0, 0) ) )
window_bounds_text = '[' + ','.join(str(x) for x in window_bounds) + ']'

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    position = pyautogui.position()
    if a != state_left:  # Button state changed
        state_left = a
        pic = pyautogui.screenshot()
		
        if a < 0:
		    # Keep the window bounds only when holding down the mouse button, because the windows size can change based on releasing the mouse button
            window_bounds = GetWindowRect( WindowFromPoint( position ) )
            window_bounds_text = '[' + ','.join(str(x) for x in window_bounds) + ']'
            pic.save('data/raw/' + str( int( time.time() * 100 ) ) + '--(' + str(position[0]) + '-' + str(position[1]) + ')--' + window_bounds_text + '--mousedown.png')		
            print('Saving mousedown screenshot')
        else:
            pic.save('data/raw/' + str( int( time.time() * 100 ) ) + '--(' + str(position[0]) + '-' + str(position[1]) + ')--' + window_bounds_text + '--mouseup.png')
            print( "Saving mouseup screenshot" )
		
        if large_movement_picture is not None:
            large_movement_picture.save('data/raw/' + str( int( movement_start_time * 100 ) ) + '--(' + str(position[0]) + '-' + str(position[1]) + ')--' + window_bounds_text + '--mousemove.png')
            print( "Saving mousemovement screenshot" )
            large_movement_picture = None
            movement_start_time = None
			
    if b != state_right:  # Button state changed
        state_right = b
        #print(b)
        #if b < 0:
            #print('Right Button Pressed')
        #else:
            #print('Right Button Released')
	
    # Large movement detection
    xDistance = numpy.linalg.norm(previous_position[0]-position[0])
    yDistance = numpy.linalg.norm(previous_position[1]-position[1])
    if( xDistance + yDistance > 10 ):
        large_movement_picture = pyautogui.screenshot()
        movement_start_time = time.time()
        print( "Detecting large movement - " + str( xDistance + yDistance ) )

    previous_position = position