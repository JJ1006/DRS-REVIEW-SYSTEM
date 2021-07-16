import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading


def play(speed):
    print(f"You clicked on play.Speed is {speed}")

def pending(decision):
    # 1. Dispal decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    # 2. Wait for 1 second
    # 3. Display sponsor image
    # 4. Wait for 1.5 seconds
    # 5. Display out/notout image


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is OUT")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT")

# Width and height of our main screen
SET_WIDTH = 600
SET_HEIGHT = 368

#Tkinter GUI starts here
window = tkinter.Tk()
window.title("Jaahanava Joshi DRS Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image = photo)
canvas.pack()


#Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text=" Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text=" Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" Give Out", width=50, command = out)
btn.pack()

btn = tkinter.Button(window, text=" Give Not Out", width=50, command = not_out)
btn.pack()

window.mainloop()