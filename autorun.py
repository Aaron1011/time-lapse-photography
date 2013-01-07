#!/usr/bin/env python
import time, datetime
import os
import getpass
USER = getpass.getuser()

class ConfigFileError:
    pass

class PhotoTaker:

    def __init__(self):
        self.USER = getpass.getuser()
        for i in range(11):
            if os.path.lexists("/dev/video" + str(i)):
                self.WEBCAM = "/dev/video" + str(i)
                break
        if not os.path.lexists("Photos"):
            os.mkdir("Photos")
        self.daysofweek = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        self.choices = ("Seconds", "Minutes", "Hours", "Days", "Weeks", "Daily", "Weekly")

    @staticmethod
    def getChoices():
        return PhotoTaker().choices

    @staticmethod
    def getDaysofWeek():
        return PhotoTaker().daysofweek

    def start(self, action, interval, day=None):
        if day:
            getattr(self, action.lower())(interval, day)
        elif action in self.getChoices():
            getattr(self, action.lower())(interval)

    def readConfig(self):
        if os.path.lexists("/home/" + self.USER + "/.pysnap.conf"):
            config = open("/home/" + self.USER + "/.pysnap.conf", "r")
            config = config.readlines()
            for line in config:
                if len(line) > 0:
                    if line[0] is not "#":
                        line2 = line.split("=")
                        if len(line2) == 2:
                            return line2[0], int(line2[1])
    def removeConfig(self):
        try:
            os.remove("/home" + self.USER + "/.pysnap.conf")
        except Exception:
            pass

    def seconds(self, num):
        try:
            if os.path.lexists("Photos/Seconds") == False:
                os.mkdir("Photos/Seconds")
            while True:
                currtime = str(time.strftime('%X'))
                os.system("streamer -c "  + self.WEBCAM + " -o ./Photos/Seconds/" + currtime + ".jpeg")
                time.sleep(float(num))
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()
                
                    
    def minutes(self, num):
        try:
            if os.path.lexists("Photos/Minutes") == False:
                os.mkdir("Photos/Minutes")
            num *= 60
            while True:
                currtime = str(time.strftime('%X'))
                os.system("streamer -c " + self.WEBCAM + " -o ./Photos/Minutes/" + currtime + ".jpeg")
                time.sleep(float(num))

        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()
    def hours(self, num=None):
        if os.path.lexists("Photos/Hours") == False:
            os.mkdir("Photos/Hours")
        num *= 60**2
        while True:
            try:
                currtime = str(time.strftime('%X'))
                os.system("streamer -c "+ self.WEBCAM + " -o ./Photos/Hours/" + currtime + ".jpeg")
                time.sleep(num)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()
                
    def days(self, num=None):
        if os.path.lexists("Photos/Weeks") == False:
            os.mkdir("Photos/Weeks")
        num *= 60**2*24
        while True:
            try:
                currtime = str(time.strftime('%X'))
                os.system("streamer -c "+ self.WEBCAM + " -o ./Photos/Weeks/" + currtime + ".jpeg")
                time.sleep(num)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

    def weeks(self, num=None):
        if os.path.lexists("Photos/Weeks") == False:
            os.mkdir("Photos/Weeks")
        num *= 60**2*24*7
        while True:
            try:
                currtime = str(time.strftime('%X'))
                os.system("streamer -c "+ self.WEBCAM + " -o ./Photos/Weeks/" + currtime + ".jpeg")
                time.sleep(num)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()            

                  
    def daily(self, picturetime):
        if os.path.lexists("Photos/Daily") == False:
            os.mkdir("Photos/Daily")
        while True:
            try:
                currtime = time.strftime('%I:%M:%S %p')
                if currtime == picturetime:
                    os.system("streamer -d -c " + self.WEBCAM + " -o ./Photos/Daily/" + currtime + ".jpeg")
                    time.sleep(5)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()


    def weekly(self, phototime, day):
        if os.path.lexists("Photos/Weekly") == False:
            os.mkdir("Photos/Weekly")
        print day
        print self.daysofweek[day - 1]
        while True:
            try:
                currtime = time.strftime('%I:%M:%S %p')
                currday = time.strftime('%A')
                if currtime == phototime and currday == self.daysofweek[day - 1]:
                    os.system("streamer -c "+ self.WEBCAM + " -o ./Photos/Weekly/" + currtime + ".jpeg")
                    time.sleep(5)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

def getTime():
    while True:
        try:
            picturetime = raw_input("\nPlease enter the time you would like pySnap to take a picture at each day, in 12-hour format: ")
            time.strptime(picturetime, "%I:%M:%S %p")
            break
        except ValueError:
            print ("Please enter a time in the following format: HH:MM:SS AM/PM: ")
    return picturetime


def main():
    try:
        print("Welcome to pySnap! pySnap makes it easy to do time lapse photography using your webcam.")
        print("\nThe following time and date has been detected from your computer: \n" + str(time.strftime('%X %x')))
        print("\nIf this is not correct, please exit the program now by pressing Control - C, and change your computer's time and date. Then, re-run this program.")
        if os.system("dpkg-query -l streamer > /dev/null 2>/dev/null") is not 0:
            print("The program streamer, which pySnap requires to run, has not been detected. Enter in your password to install streamer, or press Control - C to exit the program.")
            if os.path.lexists("streamer.deb"):
                os.system("sudo dpkg -i streamer.deb")
            else:
                os.system("sudo apt-get install -y streamer")
                    
        print("\n\n\nPress Enter to advance to the next page.")
        raw_input()



        os.system('clear')

        print("Press Control - C and any time to exit the program")

        os.system('streamer -c /dev/video0 -b 16 -o test.jpeg > /dev/null 2> /dev/null')

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

        while cont == False:
            try:
                selection = raw_input()
                selection = int(selection)
                if selection in range(1,8):
                    cont = True
                else:
                    print("Please enter a number from 1 to 7")

            except ValueError:
                print("Please enter a valid selection")

        action = PhotoTaker.getChoices()[selection - 1]


        if selection == 6:
            PhotoTaker().start(action, getTime())

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
                    if choice in range(1,8):
                        break
                    else:
                        print("Please enter a number from 1 to 7: ")
                except ValueError:
                    print("Please enter a valid selection: ")
            phototime = getTime()
            PhotoTaker().start(action, phototime, choice)
        else:

            num = raw_input("Please enter the interval, in " + action.lower() + ", that you would like pySnap to take a picture: ")
            while True:
                try:
                    num = abs(int(num))
                    break
                except ValueError:
                    num = raw_input("Please enter a number: ")
            PhotoTaker().start(action, num)
                
    except KeyboardInterrupt:
            print("\nGoodbye!")

if __name__ == "__main__":
    main()
