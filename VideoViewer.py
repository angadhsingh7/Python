import tkinter
from tkinter import StringVar
import cv2
import PIL.Image, PIL.ImageTk
import time
from datetime import datetime
import sys 
import os

class App:
    def keypressed(self, event): 
        print("key pressed =" + event.char)
        if (event.char == 'f'):
            self.vid.skipframes += 1
        if (event.char == 's'):
            self.vid.skipframes = 0
        if (event.char == 'b'):
            self.vid.skipframes -= 1
    
    def __init__(self, window, window_title, video_source=0):
       self.window = window
       self.window.title(window_title)
       self.window.bind("<Key>", self.keypressed)
       self.video_source = video_source
        # open video source (by default this will try to open the computer webcam)
       self.vid = MyVideoCapture(self.video_source)
       
       self.imgwidth = min(self.vid.width, 1400)
       self.imgheight = min(self.vid.height, 1400 * self.vid.height / self.vid.width)
       print("height ", str(self.imgheight), "weight", str(self.imgwidth)) 
        # Create a canvas that can fit the above video source size
       self.canvas = tkinter.Canvas(window, width = self.imgwidth, height = self.imgheight)
       self.canvas.pack()

        # Button that lets the user take a snapshot
       self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
       self.btn_snapshot.pack(anchor=tkinter.S, expand=True)
       self.btn_info=tkinter.Label(window, textvariable=self.vid.infostring)
       self.btn_info.pack(anchor=tkinter.S, expand=True)
       
        # After it is called once, the update method will be automatically called every delay milliseconds
       self.delay = int(1000 / self.vid.vid.get(cv2.CAP_PROP_FPS))
       self.update()

       self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            print(self.vid.infostring.get())
            cv2.imwrite(self.vid.video_source + "frame-" + self.vid.infostring.get() + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        """ now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")
        print("start Time =", current_time)  """
        ret, frame = self.vid.get_frame()
    
        if ret:
            scale = self.imgwidth / frame.shape[1] # percent of original size
            #print ("scale =", str(scale))  
            #print("frame.shape[1]", str(frame.shape[1]))
            width = int(frame.shape[1] * scale)
            height = int(frame.shape[0] * scale)
            dim = (width, height)

            frame = cv2.resize(frame, dim)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        """ now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")
        print("end Time =", current_time) """
        #self.btn_info.config(self.vid.infostring)
        adjusteddelay = max( 1, self.delay / max(1, abs(self.vid.skipframes)))
        nextupdate = min(1, adjusteddelay)
        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.video_source = video_source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.framespersec = self.vid.get(cv2.CAP_PROP_FPS)
        self.totalnumofframes = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        self.endtimeinsecs = self.totalnumofframes / self.framespersec
        self.skipframes = 0
        self.prevret = False
        self.prevframe = None
        self.infostring = StringVar()
        self.infostring.set("framerate @" + str(self.skipframes) + " @ secs from start 0" )

    def back_frame(self):
        next_frame = self.vid.get(cv2.CAP_PROP_POS_FRAMES)
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, next_frame - 2 + self.skipframes)

    def get_frame(self):
        if self.vid.isOpened():
            self.currentframe = self.vid.get(cv2.CAP_PROP_POS_FRAMES)
            self.timefromstart = self.currentframe / self.framespersec
            if (self.skipframes == 0):
                self.infostring.set("framerate @ " + str(self.skipframes) + " @ secs from start " + str(int(self.timefromstart)) +  " / " + str(int(self.endtimeinsecs)))
                return (self.prevret, self.prevframe)
            
            if (self.skipframes < 0): 
                self.back_frame()
            else: 
                for x in range(self.skipframes):
                    ret = self.vid.grab()
                
            ret, frame = self.vid.read()

            self.prevret = ret
            self.infostring.set("framerate @ " + str(self.skipframes) + " @ secs from start " + str(int(self.timefromstart)) + " / " + str(int(self.endtimeinsecs)))
            #self.

            if ret:
                self.prevframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, self.prevframe)
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

if (2 > len(sys.argv)):
     print("Run as : " + sys.argv[0] + " VIDEO FILE NAME")
     exit(1)

App(tkinter.Tk(), os.path.basename(sys.argv[1]).split('/')[-1], sys.argv[1])