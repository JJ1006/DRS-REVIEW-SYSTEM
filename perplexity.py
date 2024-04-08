# import tkinter
# import cv2
# import PIL.Image, PIL.ImageTk
# from functools import partial
# import threading
# import imutils
# import time

# stream = cv2.VideoCapture('convert.mp4')
# flag = True

# def play(speed):
#     global flag
#     print(f"You clicked on play. Speed is {speed}")
    
#     # Play the video in reverse/forward mode
#     frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
#     stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed) # Set the video speed
#     grabbed, frame = stream.read()
#     if not grabbed: # If the video is completed
#         exit()
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))) # Convert BGR to RGB without converting to grayscale
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
#     if flag:
#         canvas.create_text(134, 25, fill="black", font="Times 26 bold", text="Decision Pending")
#     flag = not flag

# def pending(decision):
#     # 1. Display decision pending image
#     frame = cv2.cvtColor(cv2.imread("pending.jpeg"), cv2.COLOR_BGR2RGB)
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT) # Resize the image if not done
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # Make it tkinter compatible
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

#     # 2. Wait for 1 second
#     time.sleep(1)

#     # 3. Display sponsor image
#     frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT) # Resize the image if not done
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # Make it tkinter compatible
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

#     # 4. Wait for 1.5 seconds
#     time.sleep(1.5)
    
#     # 5. Display out/notout image
#     if decision == 'out':
#         decisionImg = "out.jpeg"
#     else:
#         decisionImg = "not_out.jpeg"
    
#     frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
#     frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT) # Resize the image if not done
#     frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # Make it tkinter compatible
#     canvas.image = frame
#     canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

# def out():
#     thread = threading.Thread(target=pending, args=("out",))
#     thread.daemon = 1 
# # Daemon threads are used for background supporting tasks and are only needed while normal threads are executing. If normal threads are not running and remaining threads are daemon threads then the interpreter exits. When a new thread is created it inherits the daemon status of its parent.
    
#     thread.start()
#     print("Player is OUT")

# def not_out():
#     thread = threading.Thread(target=pending, args=("not out",))
#     thread.daemon = 1 
#     thread.start()
#     print("Player is NOT OUT")

# # Width and height of our main screen
# SET_WIDTH = 600
# SET_HEIGHT = 362

# # Tkinter GUI starts here
# window = tkinter.Tk()
# window.title("Jaahanava Joshi DRS Review System")
# cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB) # Read the image in BGR format and convert it to RGB format

# canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT) # Make tkinter GUI compatible with images

# photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img)) # Make it tkinter compatible

# image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo) # Display the image on the canvas

# canvas.pack() # Pack the canvas in window

# # Buttons to control playback
# btn = tkinter.Button(window, text="<< Previous (fast)", width=80, command=partial(play,-25))
# btn.pack()

# btn = tkinter.Button(window,text="<< Previous (slow)",width=80,
# command=partial(play,-2))
# btn.pack()

# btn=tkinter.Button(window,text=" Next (slow) >>",width=80,
# command=partial(play ,1))
# btn.pack()

# btn=tkinter.Button(window,text=" Next (fast) >>",width=80,
# command=partial(play ,25))
# btn.pack()

# btn=tkinter.Button(window,text=" Give Out",width=80,
# command=out)
# btn.pack()

# btn=tkinter.Button(window,text=" Give Not Out",width=80,
# command=not_out)
# btn.pack()

# window.mainloop()






# import tkinter
# import cv2
# import PIL.Image, PIL.ImageTk
# from functools import partial

# class MyVideoCapture:
#     def __init__(self, video_source):
#         self.vid = cv2.VideoCapture(video_source)

#     def get_frame(self):
#         if self.vid.isOpened():
#             ret, frame = self.vid.read()
#             if ret:
#                 # Return a boolean success flag and the current frame without converting to BGR
#                 return (ret, frame)
#             else:
#                 return (ret, None)
#         else:
#             return (ret, None)

#     def __del__(self):
#         if self.vid.isOpened():
#             self.vid.release()

# class App:
#     def __init__(self, window, window_title, video_source):
#         self.window = window
#         self.window.title(window_title)
#         self.vid = MyVideoCapture(video_source)
#         self.canvas = tkinter.Canvas(window, width=self.vid.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.canvas.pack()
#         self.btn = tkinter.Button(window, text="Play", width=50, command=self.play)
#         self.btn.pack()
#         self.delay = 15
#         self.update()

#         self.window.mainloop()

#     def play(self):
#         # Add your play logic here
#         pass

#     def update(self):
#         ret, frame = self.vid.get_frame()
#         if ret:
#             self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
#             self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        
#         self.window.after(self.delay, self.update)

# # Set your video file path here
# video_source = 'IMG_2364.mov'

# # Set the window title
# window_title = "Video Player"

# # Create a tkinter window
# window = tkinter.Tk()

# # Create the application instance
# app = App(window, window_title, video_source)








import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial

class MyVideoCapture:
    def __init__(self, video_source):
        self.vid = cv2.VideoCapture(video_source)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, frame)
            else:
                return (ret, None)
        else:
            return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

class App:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.vid = MyVideoCapture(video_source)
        self.canvas = tkinter.Canvas(window, width=self.vid.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        # Buttons for controlling playback
        btn_play = tkinter.Button(window, text="Play", width=50, command=self.play)
        btn_play.pack()
        
        btn_pause = tkinter.Button(window, text="Pause", width=50, command=self.pause)
        btn_pause.pack()
        
        btn_stop = tkinter.Button(window, text="Stop", width=50, command=self.stop)
        btn_stop.pack()
        
        self.delay = 15
        self.update()

        self.window.mainloop()

    def play(self):
        # Add your play logic here
        pass

    def pause(self):
        # Add your pause logic here
        pass

    def stop(self):
        # Add your stop logic here
        pass

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        
        self.window.after(self.delay, self.update)

# Set your video file path here
video_source = 'IMG_2775.mov'

# Set the window title
window_title = "Video Player"

# Create a tkinter window
window = tkinter.Tk()

# Create the application instance
app = App(window, window_title, video_source)