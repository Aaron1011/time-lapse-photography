#! /usr/bin/env python
import subprocess
import os
import string


def main():
    try:
        print("Welcome to pySnap's movie-making program! This program allows you to turn the time lapse photography you have taken into a movie\n\n")
        if not os.path.exists("Photos"):
            print("You don't seem to have any pictures yet. Run pySnap first, and then run this program again")
            quit()
        dirs = os.listdir("Photos")
        print("The following picture folders have been detected:")
        i = 1
        for path in dirs:
            print("%s: %s" % (i, path))
            i += 1
        choice = int(raw_input("Enter in the number corresponding the the folder you would like to use: "))
        while not choice - 1 in range(len(dirs)):
            choice = raw_input("Please enter a valid choice: ")

        fps = raw_input("Enter in the frame rate (FPS) for your movie. Hit enter for the default of 20: ")
        if not fps:
            fps = 20
        elif not fps in string.digits:
            fps = 20

        print("Creating movie:")
        subprocess.call(("mencoder mf://%s/*.jpeg -mf w=800:h=600:fps=%s:type=jpeg -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi" % ("Photos/" + dirs[choice - 1], fps)).split(" "), stdout=subprocess.PIPE)
    except KeyboardInterrupt:
        print("\b\b\nGoodbye!")
        quit()

if __name__ == "__main__":
    main()
