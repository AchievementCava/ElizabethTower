import sys
import tkinter as tk
import time
import winsound
import threading

muteAll =  bool(False)

class foreground:
    height = 500
    width = 720

    def muteAll():
        muteAll = bool(True)

class background():
       #defining a function, tick, which will repeat as the window updates
       def tick():
               time_string = time.strftime("%I:%M:%S%p")
               clock.config(text=time_string)
               clock.after(200, background.tick)
       #function to run chimes
       #18 second break period for chime, first bong on the hour
       def hour():
           if muteAll == bool(False):
              while True:
                     if time.strftime("%M:%S") == "59:42":
                            #if muteAll = False:
                            winsound.PlaySound("Chimes", winsound.SND_FILENAME)
                            strikes = int(time.strftime("%I"))
                            for count in range (strikes):

                                   winsound.PlaySound("Bong", winsound.SND_FILENAME)
                            #different chimes for every 15mins
                            #if muteMisc == False:
                     elif time.strftime("%M:%S") == "15:00":
                            winsound.PlaySound("15chime", winsound.SND_FILENAME)
                     elif time.strftime("%M:%S") == "30:00":
                            winsound.PlaySound("30chime", winsound.SND_FILENAME)
                     elif time.strftime("%M:%S") == "45:00":
                            winsound.PlaySound("45chime", winsound.SND_FILENAME)

#runtime code

thread1 = threading.Thread(target = background.hour)

thread1.start()

        #sets up the window and the label
root = tk.Tk()
root.title("Elizabeth Tower")
root.configure(background = "black")
clock = tk.Label(root, font=("Georgia", 35), fg = "white", bg= "black", anchor="e")
clock.pack(side = "top", expand = "true")

#buttons and shit
mute = tk.Button(root, text = "Mute", fg = "White", bg = "grey", command = muteAll)
mute.pack(side = "right")



background.tick()
#function to recur
root.mainloop()

