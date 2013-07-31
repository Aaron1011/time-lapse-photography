#!/usr/bin/env python
import time
import os
import subprocess
import getpass
import argparse
import sys

USER = getpass.getuser()
PACKAGES = ["python-opencv", "mencoder"]

def install_deps():
    subprocess.Popen(["sudo", "apt-get", "install"] + PACKAGES).wait()

try:
    import cv2
except:
    print "OpenCV, a computer vision library which pySnap requires to run, is not installed. Please visit http://opencv.org/ for installation instructions for your platform."
    print "If you are running a Debian-based Linux distribution, pySnap can automatically install OpenCV for you"
    if raw_input("Install OpenCV? [y/n]").lower() == 'y':
        install_deps()
    else:
        print "PySnap will now exit."
        quit()


from PhotoTaker import PhotoTaker

class ConfigFileError:
    pass



def getTime():
    while True:
        try:
            picturetime = raw_input("\nPlease enter the time you would like pySnap to take a picture at each day, in 12-hour format: ")
            time.strptime(picturetime, "%I:%M:%S %p")
            break
        except ValueError:
            print ("Please enter a time in the following format: HH:MM:SS AM/PM: ")
    return picturetime


def on_indie(args):
    return not args.indie and not os.path.exists(os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), '.git')))

def use_indie():
    TERM = os.environ.get("TERM")
    if os.uname()[1] == 'raspberrypi':
        TERM = 'lxterminal'
    subprocess.Popen([TERM, "-e", sys.executable, os.path.abspath(__file__), '-i']).wait()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--indie', action='store_true', help='Run in IndieCity mode')
    parser.add_argument('-cm', '--camera-module', action='store_true', help='Use Raspberry Pi camera module' )
    args = parser.parse_args()
    photo_taker = PhotoTaker(args.camera_module)

    if on_indie(args):
        use_indie()
        quit()

    try:
        print("Welcome to pySnap! pySnap makes it easy to do time lapse photography using your webcam.")
        print("\nThe following time and date has been detected from your computer: \n" + str(time.strftime('%X %x')))
        print("\nIf this is not correct, please exit the program now by pressing Control - C, and change your computer's time and date. Then, re-run this program.")

        print("\n\n\nPress Enter to advance to the next page.")
        raw_input()

        subprocess.call(['clear'])

        print("Press Control - C and any time to exit the program")

        photo_taker.takePicture('./', 'test')

        print("\n\n\nA test image has been taken using your webcam. Look in the location that autorun.py is located for a file named test.jpeg. If you do not see test.jpeg, or it does not contain an image, ensure that your webcam is connected and that it works properly with other programs.")

        print ("\n")
        print ("1) Every \033[31m'x'\033[39m seconds")
        print ("2) Every \033[31m'x'\033[39m minutes")
        print ("3) Every \033[31m'x'\033[39m hours")
        print ("4) Every \033[31m'x'\033[39m days")
        print ("5) Every \033[31m'x'\033[39m weeks")
        print ("6) Every day at \033[31m'x'\033[39m")
        print ("7) Every week at \033[31m'x'\033[39m")
        print('\n')
        print("Enter in the number that corresponds to the frequency that you would like to have pySnap take a picture. You will be prompted to enter \033[31m'x'\033[39m after you make your selection.")

        cont = False

        while not cont:
            try:
                selection = raw_input()
                selection = int(selection)
                if selection in range(1, 8):
                    cont = True
                else:
                    print("Please enter a number from 1 to 7")

            except ValueError:
                print("Please enter a valid selection")

        action = photo_taker.getChoices()[selection - 1]

        if selection == 6:
            photo_taker.start(action, getTime())

        if selection == 7:
            print("\n1)\033[31mSunday\033[39m")
            print("2)\033[31mMonday\033[39m")
            print("3)\033[31mTuesday\033[39m")
            print("4)\033[31mWednesday\033[39m")
            print("5)\033[31mThursday\033[39m")
            print("6)\033[31mFriday\033[39m")
            print("7)\033[31mSaturday\033[39m")
            print("Please enter the number that corresponds to the day that you would like pySnap to take a picture on: ")

            while True:
                try:
                    choice = int(raw_input())
                    if choice in range(1, 8):
                        break
                    else:
                        print("Please enter a number from 1 to 7: ")
                except ValueError:
                    print("Please enter a valid selection: ")
            phototime = getTime()
            photo_taker.start(action, phototime, choice)
        else:

            num = raw_input("Please enter the interval, in " + action.lower() + ", that you would like pySnap to take a picture: ")
            while True:
                try:
                    num = abs(int(num))
                    break
                except ValueError:
                    num = raw_input("Please enter a number: ")
            photo_taker.start(action, num)

    except KeyboardInterrupt:
            print("\nGoodbye!")

if __name__ == "__main__":
    main()
