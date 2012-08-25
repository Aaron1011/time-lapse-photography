import time
import sys
import os
import getpass
USER = getpass.getuser()
for i in range(1,8):
    if os.path.lexists("/dev/video" + str(i)):
        WEBCAM = "/dev/video" + str(i)

def seconds(num2=None):
    try:
        if num2 is not None:
            print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
            print("Time lapse photograph has been started.")
            print("A picture will be placed into the Photos folder every " + str(num2) + " seconds")
            if os.path.lexists("Photos/Seconds") == False:
                os.mkdir("Photos/Seconds")
            while True:
                currtime = str(time.strftime('%X'))
                os.system("streamer -c " + WEBCAM + " -o ./Photos/Seconds" + currtime + ".jpeg")
                time.sleep(float(num2))   
        cont = False
        print("\n\n\n")
        num = raw_input("Please enter the interval, in seconds, that you would like pySnap to take a picture: ")
        while cont == False:
            try:
                num = int(num)
                cont = True
            except ValueError:
                num = raw_input("\nPlease enter a number: ")
        config = open("/home/" + USER + "/.pysnap.conf", "w")
        config.write("\nSeconds=" + str(num))
        config.close()
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every " + str(num) + " seconds")
        if os.path.lexists("Photos/Seconds") == False:
            os.mkdir("Photos/Seconds")
        while True:
        
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Seconds/" + currtime + ".jpeg")
            time.sleep(float(num))
    except KeyboardInterrupt:
        print("\nGoodbye!")
        quit()
            
            
                
                
def minutes(num2=None):
    if num2 is not None:
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every " + str(num2) + " minutes")
        if os.path.lexists("Photos/Minutes") == False:
            os.mkdir("Photos/Minutes")
        num3 = num2 * 60
        while True:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Minutes" + currtime + ".jpeg")
            time.sleep(float(num3))
    cont = False
    print("\n\n\n")
    num = raw_input("Please enter the interval, in minutes, that you would like pySnap to take a picture: ")
    while cont == False:
        try:
            num = int(num)
            num3 = num *  60
            cont = True
        except ValueError:
            num = raw_input("\nPlease enter a number: ")
    config = open("/home/" + USER + "/.pysnap.conf", "w")
    config.write("\nMinutes=" + str(num))
    config.close()
    print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
    print("Time lapse photograph has been started.")
    print("A picture will be placed into the Photos folder every " + str(num) + " minutes")
    if os.path.lexists("Photos/Minutes") == False:
        os.mkdir("Photos/Minutes")
    while True:
        
        currtime = str(time.strftime('%X'))
        os.system("streamer -c " + WEBCAM + " -o ./Photos/Minutes/" + currtime + ".jpeg")
        time.sleep(float(num3))

def hours(num2=None):
    if num2 is not None:
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every " + str(num2) + " hours")
        if os.path.lexists("Photos/Hours") == False:
            os.mkdir("Photos/Hours")
        num3 = num2 * 60 * 60
        while True:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Hours/" + currtime + ".jpeg")
            time.sleep(float(num3))
    cont = False
    print("\n\n\n")
    num = raw_input("Please enter the interval, in hours, that you would like pySnap to take a picture: ")
    while cont == False:
        try:
            num = int(num)
            num3 = int(num)
            num *= 60
            num *= 60
            cont = True
        except ValueError:
            num = raw_input("\nPlease enter a number: ")
    config = open("/home/" + USER + "/.pysnap.conf", "w")
    config.write("\nHours=" + str(num))
    config.close()
    print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
    print("Time lapse photograph has been started.")
    print("A picture will be placed into the Photos folder every " + str(num3) + " hours")
    if os.path.lexists("Photos/Hours") == False:
        os.mkdir("Photos/Hours")
    while True:
        try:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Hours/" + currtime + ".jpeg")
            time.sleep(num)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()
            
def days(num2=None):
    if num2 is not None:
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every " + str(num2) + " days")
        if os.path.lexists("Photos/Days") == False:
            os.mkdir("Photos/Days")
        num3 = num2 * 7 * 60 * 60
        while True:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Weeks/" + currtime + ".jpeg")
            time.sleep(float(num3))
    cont = False
    print("\n\n\n")
    num = raw_input("Please enter the interval, in days, that you would like pySnap to take a picture: ")
    while cont == False:
        try:
            num = int(num)
            num3 = int(num)
            num *= 24
            num *= 60
            num *= 60
            cont = True
        except ValueError:
            num = raw_input("\nPlease enter a number: ")
    config = open("/home/" + USER + "/.pysnap.conf", "w")
    config.write("\nDays=" + str(num))
    
    print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
    print("Time lapse photograph has been started.")
    print("A picture will be placed into the Photos folder every " + str(num3) + " days")
    if os.path.lexists("Photos/Weeks") == False:
        os.mkdir("Photos/Weeks")
    while True:
        try:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Weeks/" + currtime + ".jpeg")
            time.sleep(num)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()



            
def weeks(num2=None):
    if num2 is not None:
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every " + str(num2) + " Weeks")
        if os.path.lexists("Photos/Weeks") == False:
            os.mkdir("Photos/Weeks")
        num3 = num2 * 7 * 24 * 60 * 60
        while True:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Weeks/" + currtime + ".jpeg")
            time.sleep(float(num3))
    cont = False
    print("\n\n\n")
    num = raw_input("Please enter the interval, in weeks, that you would like pySnap to take a picture: ")
    while cont == False:
        try:
            num = int(num)
            num3 = int(num)
            num *= 7
            num *= 24
            num *= 60
            num *= 60
            cont = True
        except ValueError:
            num = raw_input("\nPlease enter a number: ")
    config = open("/home/" + USER + "/.pysnap.conf", "w")
    config.write("\nWeeks=" + str(num))
    config.close()
    print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
    print("Time lapse photograph has been started.")
    print("A picture will be placed into the Photos folder every " + str(num3) + " Weeks")
    if os.path.lexists("Photos/Weeks") == False:
        os.mkdir("Photos/Weeks")
    while True:
        try:
            currtime = str(time.strftime('%X'))
            os.system("streamer -c " + WEBCAM + " -o ./Photos/Weeks/" + currtime + ".jpeg")
            time.sleep(num)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()            

              
              
def daily(num2=None):
    if num2 is not None:
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every day at" + num2)
        if os.path.lexists("Photos/Daily") == False:
            os.mkdir("Photos/Daily")
        picture = True
        while True:
            try:
                currtime = time.strftime('%X')[:5]
                if currtime == num2[:5] and picture == True:
                    os.system("streamer -c " + WEBCAM + " -o ./Photos/Daily/" + currtime + ".jpeg")
                    picture = False
                elif currtime is not num2[:5]:
                    picture = True
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()
    cont = False
    print("\n\n\n")
    num = raw_input("Please enter the time that you would like pySnap to take a picture at each day, in 24-hour format: ")
    while cont == False:
        try:
            num2 = int(num[:2])
            num2 = int(num[3:5])
            cont = True
        except ValueError:
            num = raw_input("\nPlease enter a valid time: ")
    config = open("/home/" + USER + "/.pysnap.conf", "w")
    config.write("\nDaily=" + str(num))
    config.close()
    print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
    print("Time lapse photograph has been started.")
    print("A picture will be placed into the Photos folder every day at " + str(num))
    if os.path.lexists("Photos/Daily") == False:
        os.mkdir("Photos/Daily")
    picture = True
    while True:
        try:
            currtime = time.strftime('%X')[:5]
            if currtime == num[:5] and picture == True:
                os.system("streamer -c " + WEBCAM + " -o ./Photos/Daily/" + currtime + ".jpeg")
                picture = False
            elif currtime != num[:5]:
                picture = True
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()


def weekly(num2=None):
    if num2 is not None:
        print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
        print("Time lapse photograph has been started.")
        print("A picture will be placed into the Photos folder every week on " + num2[1] + " at " + num2[0])
        if os.path.lexists("Photos/Weekly") == False:
            os.mkdir("Photos/Weekly")
        picture = True
        while True:
            try:
                currtime = time.strftime('%X')
                currday = time.strftime("%A")
                if currtime == num2[0] and num2[1] == currday and picture == True:
                    os.system("streamer -c " + WEBCAM + " -o ./Photos/Weekly/" + currtime + ".jpeg")
                    picture = False
                elif currtime is not num2[:5]:
                    picture = True
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()
    
    print("\n1)\033[31mSunday\033[39m")
    print("2)\033[31mMonday\033[39m")
    print("3)\033[31mTuesday\033[39m")
    print("4)\033[31mWednesday\033[39m")
    print("5)\033[31mThursday\033[39m")
    print("6)\033[31mFriday\033[39m")
    print("7)\033[31mSaturday\033[39m")
    print("Please enter the number that corresponds to the day that you would like pySnap to take a picture on: ")
    cont = False

    while cont == False:
        try:
            choice = raw_input()
            choice = int(selection)
            if choice in range(1,8):
                cont = True
            else:
                print("Please enter a number from 1 to 7")

        except ValueError:
            print("Please enter a valid selection")
            cont = False
    num = raw_input("Please enter the time that you would like pySnap to take a picture at each day, in 24-hour format: ")
    while cont == False:
        try:
            num = int(num[:2])
            num = int(num[3:5])
            cont = True
        except ValueError:
            num = raw_input("\nPlease enter a valid time: ")
    config = open("/home/" + USER + "/.pysnap.conf", "w")
    config.write("\nWeekly=" + str(num + "," + time.strftime("%A")))
    config.close()
    print("Your selection has been saved in a configuration file at /home/" + USER + "/.pysnap.conf")
    print("Time lapse photograph has been started.")
    print("A picture will be placed into the Photos folder every day at " + str(num))
    if os.path.lexists("Photos/Weekly") == False:
        os.mkdir("Photos/Weekly")
    picture = True
    while True:
        try:
            currtime = time.strftime('%X')[:5]
            if currtime == num and picture == True:
                os.system("streamer -c " + WEBCAM + " -o ./Photos/Weekly/" + currtime + ".jpeg")
                picture = False
            elif currtime != num:
                picture = True
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()


def select(num):
    os.system('clear')
    print("Press Control - C at any time to exit the program")
    if num == 1:
        seconds()
    elif num == 2:
        minutes()
    elif num == 3:
        hours()
    elif num == 4:
        days()
    elif num == 5:
        weeks()
    elif num == 6:
        daily()
    elif num == 7:
        weekly()
        


try:
    print("Welcome to pySnap! pySnap makes it easy to do time lapse photography using your webcam.")
    print("\nThe following time and date have been detected from your computer: \n" + str(time.strftime('%X %x')))
    print("\nIf this is not correct, please exit the program now by pressing Control - C, and change your computer's time and date. Then, re-run this program.")
    if os.system("dpkg-query -l streamer > /dev/null 2>/dev/null") is not 0:
        print("The program streamer, which pySnap requires to run, has not been detected. Enter in your password to install streamer, or press Control - C to exit the program.")
        if os.path.lexists("streamer.deb"):
            os.system("sudo dpkg -i streamer.deb")
        else:
            os.system("sudo apt-get install -y streamer")
    if os.path.lexists("/home/" + USER + "/.pysnap.conf"):
        config = open("/home/" + USER + "/.pysnap.conf", "r")
        config2 = config.read()
        config = config2.split("\n")
        for line in config:
            if len(line) > 0:
                if line[0] is not "#":
                    line2 = line.split("=")
                    if line2[0] == "Seconds":
                       response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                       if response == "N" or response == "n":
                           os.remove("/home/" + USER + "/.pysnap.conf")
                       else:
                            seconds(num2=line2[1])
                    elif line2[0] == "Minutes":
                       response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                       if response == "N" or response == "n":
                           os.remove("/home/" + USER + "/.pysnap.conf")
                       else:
                            minutes(num2=line2[1]) 
                    elif line2[0] == "Hours":
                        response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                        if response == "N" or response == "n":
                            os.remove("/home/" + USER + "/.pysnap.conf")
                        else:
                            hours(num2=line2[1])
                    elif line2[0] == "Days":
                        response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                        if response == "N" or response == "n":
                            os.remove("/home/" + USER + "/.pysnap.conf")   
                        else:
                            days(num2=line2[1])
                    elif line2[0] == "Weeks":
                        response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                        if response == "N" or response == "n":
                            os.remove("/home/" + USER + "/.pysnap.conf")
                        else:
                            weeks(num2=line2[1])
                    elif line2[0] == "Daily":
                        response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                        if response == "N" or response == "n":
                            os.remove("/home/" + USER + "/.pysnap.conf")
                        else:
                            daily(num2=line2[1])
                    elif line2[0] == "Weekly":
                        response = raw_input("\nA configuration file has been detected. Would you like to load it? (Y or N): ")
                        if response == "N" or response == "n":
                            os.remove("/home/" + USER + "/.pysnap.conf")   
                        else:
                            weekly(num2=line2[1].split(","))                             
                
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
    select(selection)
except KeyboardInterrupt:
    print("\nGoodbye!")