import getpass
import os
import cv2
import time

class PhotoTaker:
    daysofweek = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    choices = ("Seconds", "Minutes", "Hours", "Days", "Weeks", "Daily", "Weekly")

    def __init__(self, cm=False):
        self.USER = getpass.getuser()
        self.cm = cm
        if cm:
            self.WEBCAM = ['raspistill', '-o']
        else:
            for i in range(11):
                if os.path.lexists("/dev/video" + str(i)):
                    self.WEBCAM = cv2.VideoCapture(i)
                    break
            if not os.path.lexists("Photos"):
                os.mkdir("Photos")
            
    @classmethod
    def getChoices(klass):
        return klass.choices

    @classmethod
    def getDaysofWeek(klass):
        return klass.daysofweek

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

    def takePictureCV(self, directory, currtime=None):
        if not currtime:
            currtime = str(time.strftime("%X"))
        rval, img = self.WEBCAM.read()
        cv2.waitKey(20)
        if rval:
            cv2.imwrite(directory + currtime + '.jpeg', img)

    def takePicture(self, *args):
        if self.cm:
            self.takePictureCmd(*args)
        else:
            self.takePictureCV(*args)

    def takePictureCmd(self, directory, currtime=None):
        if not currtime:
            currtime = str(time.strftime("%X"))
        fname = directory + currtime + '.jpeg'
        subprocess.Popen(self.WEBCAM + [fname])

    def removeConfig(self):
        try:
            os.remove("/home" + self.USER + "/.pysnap.conf")
        except Exception:
            pass

    def seconds(self, num):
        try:
            if not os.path.lexists("Photos/Seconds"):
                os.mkdir("Photos/Seconds")
            while True:
                self.takePicture("./Photos/Seconds/")
                time.sleep(float(num))
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()

    def minutes(self, num):
        try:
            if not os.path.lexists("Photos/Minutes"):
                os.mkdir("Photos/Minutes")
            num *= 60
            while True:
                self.takePicture("./Photos/Minutes/")
                time.sleep(float(num))

        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()

    def hours(self, num=None):
        if not os.path.lexists("Photos/Hours"):
            os.mkdir("Photos/Hours")
        num *= 60 ** 2
        while True:
            try:
                self.takePicture("./Photos/Hours/")
                time.sleep(num)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

    def days(self, num=None):
        if not os.path.lexists("Photos/Weeks"):
            os.mkdir("Photos/Weeks")
        num *= 60 ** 2 * 24
        while True:
            try:
                self.takePicture("./Photos/Days/")
                time.sleep(num)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

    def weeks(self, num=None):
        if not os.path.lexists("Photos/Weeks"):
            os.mkdir("Photos/Weeks")
        num *= 60 ** 2 * 24 * 7
        while True:
            try:
                self.takePicture("./Photos/Weeks/")
                time.sleep(num)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

    def daily(self, picturetime):
        if not os.path.lexists("Photos/Daily"):
            os.mkdir("Photos/Daily")
        while True:
            try:
                currtime = time.strftime('%I:%M:%S %p')
                if currtime == picturetime:
                    self.takePicture("./Photos/Daily/", currtime=currtime)
                    time.sleep(5)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

    def weekly(self, phototime, day):
        if not os.path.lexists("Photos/Weekly"):
            os.mkdir("Photos/Weekly")
        print self.daysofweek[day - 1]
        while True:
            try:
                currtime = time.strftime('%I:%M:%S %p')
                currday = time.strftime('%A')
                if currtime == phototime and currday == self.daysofweek[day - 1]:
                    self.takePicture("./Photos/Weekly/", currtime=currtime)
                    time.sleep(5)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                quit()

