import tkinter
import os
from tkinter import *
# from PIL import ImageTk,Image
from tkinter import filedialog
from imageai.Detection import ObjectDetection

if not os.path.exists("C:/RecogImg"):
    os.makedirs("C:/RecogImg")


def igui():
    global details
    global detector
    global cl
    global cr

    execution_path = os.getcwd()
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    root = tkinter.Tk()
    root.title('Obvision')
    root.geometry('1000x500+10+10')
    root.iconbitmap(r'icon.exe')

    frame = Frame(root)
    frame.pack()

    # topframe = Frame(root)
    # topframe.pack(side=TOP)

    # save_button = tkinter.Button(frame, text="Save File", width=20, command=sv)
    # save_button.pack(side=BOTTOM)

    open_button = tkinter.Button(frame, text="Open File", width=20, command=op)
    open_button.pack(side=BOTTOM)

    details = Text(frame, height=20, width=600)
    details.pack(side=BOTTOM)

    # cr = tkinter.Canvas(frame, width=500, height=500)
    # cr.pack(side=RIGHT)

    # cl = tkinter.Canvas(frame, width=500, height=500)
    # cl.pack(side=RIGHT)


def op():
    opfile = filedialog.askopenfilename(initialdir="/", title="Select file",
                                        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    detections = detector.detectObjectsFromImage(input_image=opfile,
                                                 output_image_path=os.path.join("C:/RecogImg", "image new.jpg"))
    # input_img = ImageTk.PhotoImage(Image.open(opfile))
    # cl.create_image(0, 0, image=input_img, anchor='nw')
    for eachObject in detections:
        details.insert(END, eachObject["name"])
        details.insert(END, "\n")
        details.insert(END, eachObject["percentage_probability"])
        details.insert(END, "\n")
        details.insert(END, "\n")


# def sv():
    # svfile = filedialog.asksaveasfilename(initialdir="/", title="Save As",
    #                                       filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    # if svfile != "":
    #    opfile.save(svfile)
