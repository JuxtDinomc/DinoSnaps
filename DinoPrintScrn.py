import os
import time
import keyboard
import mss

def take_screenshot() :

    print("Taking screeshot...")

    output_folder = "My_screenshots"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{output_folder}/screenshot_{timestamp}.png"

    with mss.MSS() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)

    print(f"imgage printed successfully and saved to folder {filename}")

keyboard.add_hotkey("print screen", take_screenshot)

print("---SCREENSHOT APP IS ACTIVE---")
print("Press key PrtSc to take screenshot")
print("Press Esc to close app")

keyboard.wait("esc")
