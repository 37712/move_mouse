# this code moves the mouse
import pyautogui # library to move the mouse and interact with gui, it is multiplatform
import time
import os

def get_screenshot():
    # if foo.png file exists, delete file
    if os.path.isfile('screenshot.png'):
        os.remove('screenshot.png')

    # get screen shot
    pyautogui.screenshot('screenshot.png')

# click on imgae or target location
def click(foo):
    pyautogui.click(foo) # find location of image and click it, error if fails

# depricated
def click_here(foo):
    target = pyautogui.locateOnScreen(foo)# find cordintates of roboform icon
    if  target == None:
        # if codinates not found
        print("Error:", foo, "button not found, target =", target)
        exit()
    else:
        # clic on roboform icon to get netx password
        print("target found, target =", target)
        pyautogui.click(target) # click on x,y location

# find cordintates of picture
def find(foo):
    if pyautogui.locateOnScreen(foo) == None:
        wait(1)
        find(foo)
    else:
        print(foo, "located")

# wait x seconds
def wait(x):
    print("waiting for ", x, "seconds")
    time.sleep(x)

# code start here
print("\nmove_mouse start\n")

# signing in to netx360
click('netx360.png')
find('netx_login.png')
click('netx_robo.png')
wait(3) # waiting for roboform to fill credentials
click('cont.png')

# waiting for netx360 to open
find('report_tab.png')
click('report_tab.png')

# waiting for all reports button to show up
find('all_reports.png')
click('all_reports.png')

# waiting for all holdings button to show up
find('all_holdings.png')
click('all_holdings.png')

# waiting for first next button to show up
find('next1.png')
click('next1.png')
wait(1)

# waiting for second next button to show up
find('next1.png')
click('next1.png')

# generate report
while True:
    find('generate.png')
    click('generate.png')
    click('csv.png')
    # if the button got succesfully clicked
    if pyautogui.locateOnScreen('generate.png') == None:
        break

# waiting for csv file to be created


print("\nmove_mouse end")

# old test stuff
# (0,0) is at the top left of screen
#pyautogui.moveTo(1000, 1000) # move mouse to x,y location
#pyautogui.moveRel(500, 500)  # move mouse by x,y pixels
#pyautogui.dragTo(100, 150) # drag mouse to x,y location
#pyautogui.dragRel(0, 10)  # drag mouse by x,y pixels
#pyautogui.click('netx_robo.png') # find location of image and click it, error if fails