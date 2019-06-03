import tkinter as tk
from WebCamDetection import web
from ImageDetection import igui

def pd():
    igui()


def wd():
    web()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Obvision')
    root.iconbitmap(r'icon.exe')

    # pick a .gif image file you have in the working directory
    f_name = "Obvision_bg.gif"
    bg_image = tk.PhotoImage(file=f_name)

    # get the width and height of the image
    w = bg_image.width()
    h = bg_image.height()

    # size the window so the image will fill it
    root.geometry("%dx%d+10+10" % (w, h))
    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')

    # add canvas text at coordinates x=15, y=20
    # anchor='nw' implies upper left corner coordinates
    # cv.create_text(15, 20, text="Python Greetings", fill="red", anchor='nw')

    # now add some button widgets
    btn1 = tk.Button(cv, text="Image", width=20, command=pd)
    btn1.place(x=700, y=300)
    btn2 = tk.Button(cv, text="WebCam", width=20, command=wd)
    btn2.place(x=700, y=400)
    root.resizable(False, False)
    root.mainloop()
