import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture('video0.mp4')
flag = True
def play(speed):
    global flag
    print(f"You clicked on play.Speed is {speed}")
    
    # Play the video in reverse/forward mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed) # to set the video speed
    grabbed, frame = stream.read()
    if not grabbed: # if the video is completed
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 25, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag
        


def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT) # resizing the image if not done
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # tkinter compactible, takes image wherever expects an image.
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 second
    time.sleep(1)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT) # resizing the image if not done
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # tkinter compactible, takes image wherever expects an image.
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 seconds
    time.sleep(1.5)
    
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "out.jpeg"
    else:
        decisionImg = "not_out.jpeg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT) # resizing the image if not done
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) # tkinter compactible, takes image wherever expects an image.
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1 
# Daemon threads are used for background supporting tasks and are only needed while normal threads are executing. If normal threads are not running and remaining threads are daemon threads then the interpreter exits. When a new thread is created it inherits the daemon status of its parent.
    thread.start()
    print("Player is OUT")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT")

# Width and height of our main screen
SET_WIDTH = 600
SET_HEIGHT = 362

#Tkinter GUI starts here
window = tkinter.Tk()
window.title("Jaahanava Joshi DRS Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT) #makes tkinter GUI compactible image
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image = photo)
canvas.pack()


#Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text=" Next (slow) >>", width=50, command=partial(play, 1))
btn.pack()
btn = tkinter.Button(window, text=" Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" Give Out", width=50, command = out)
btn.pack()

btn = tkinter.Button(window, text=" Give Not Out", width=50, command = not_out)
btn.pack()

window.mainloop()