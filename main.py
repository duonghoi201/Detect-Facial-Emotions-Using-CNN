import cv2
import tkinter as tk
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
from tkinter import filedialog

window = tk.Tk()
window.geometry('850x430+370+170')
window.iconbitmap('logo/icon.ico')

# stop resize
window.resizable(width=False, height=False)
window.title("TGMT - EMOTION RECOGNITION")

label_1 = tk.Label(window, text="BÁO CÁO HỌC PHẦN")
label_1.configure(font=("Times New Roman", 20, "bold"))
label_1.pack()

label_4 = tk.Label(window, text="THỊ GIÁC MÁY TÍNH TRÊN NỀN NHÚNG")
label_4.configure(font=("Times New Roman", 20, "bold"))
label_4.pack()

label_2 = tk.Label(window, text="XÂY DỰNG ỨNG DỤNG NHẬN DIỆN CẢM XÚC")
label_2.configure(font=("Times New Roman", 20, "bold"))
label_2.pack()

# SPKT logo
img = Image.open("logo/logo.jpg")
logo_rz = img.resize((90, 90))
logo = ImageTk.PhotoImage(logo_rz)
label_4 = tk.Label(image=logo)
label_4.place(relx=0.01, rely=0.02, anchor=NW)

# load model
model = model_from_json(open("fer_arch_final.json", "r").read())
# load weights
model.load_weights("fer_model_final.h5")
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Import file and recognition
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    cap = cv2.VideoCapture(filename)
    while cap.isOpened():
        res, frame = cap.read()
        # frame = cv2.resize(frame,(480,480))
        height, width, channel = frame.shape
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(gray_image)
        try:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
                roi_gray = gray_image[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48))
                image_pixels = img_to_array(roi_gray)
                image_pixels = np.expand_dims(image_pixels, axis=0)
                image_pixels /= 255
                predictions = model.predict(image_pixels)
                max_index = np.argmax(predictions[0])
                emotion_detection = ('angry', 'happy', 'neutral', 'sad', 'surprise')
                emotion_prediction = emotion_detection[max_index]
                cv2.putText(frame, emotion_prediction, (x + 5, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1,
                            cv2.LINE_AA)
        except:
            pass
        frame[0:int(height / 1000), 0:int(width)] = res
        cv2.imshow('TGMT - EMOTION DETECTION - DETECT', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()




# Open camera & detect
def detect():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        res, frame = cap.read()
        height, width, channel = frame.shape
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(gray_image)
        try:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
                roi_gray = gray_image[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48))
                image_pixels = img_to_array(roi_gray)
                image_pixels = np.expand_dims(image_pixels, axis=0)
                image_pixels /= 255
                predictions = model.predict(image_pixels)
                max_index = np.argmax(predictions[0])
                emotion_detection = ('angry', 'happy', 'neutral', 'sad', 'surprise')
                emotion_prediction = emotion_detection[max_index]
                cv2.putText(frame, emotion_prediction, (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                            cv2.LINE_AA)
        except:
            pass
        frame[0:int(height / 20), 0:int(width)] = res
        cv2.imshow('TGMT - EMOTION DETECTION - DETECT', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# Detect & record
def detectRec():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    op = cv2.VideoWriter('videorec.mp4', fourcc, 9.0, (640, 480))
    while cap.isOpened():
        res, frame = cap.read()
        height, width, channel = frame.shape
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(gray_image)
        try:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
                roi_gray = gray_image[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48))
                image_pixels = img_to_array(roi_gray)
                image_pixels = np.expand_dims(image_pixels, axis=0)
                image_pixels /= 255
                predictions = model.predict(image_pixels)
                max_index = np.argmax(predictions[0])
                emotion_detection = ('angry', 'happy', 'neutral', 'sad', 'surprise')
                emotion_prediction = emotion_detection[max_index]
                cv2.putText(frame, emotion_prediction, (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                            cv2.LINE_AA)
        except:
            pass
        frame[0:int(height / 20), 0:int(width)] = res
        op.write(frame)
        cv2.imshow('TGMT - EMOTION DETECTION - DETECT & RECORD', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    op.release()
    cap.release()
    cv2.destroyAllWindows()


# exit program
def exitt():
    exit()


# Button import file and recog
but1 = Button(window, padx=5, pady=5, width=30, bg='white', fg='black', relief=GROOVE, text='Import File & Recognition',
              command=UploadAction, font=('helvetica 15 bold'))
but1.place(relx=0.5, rely=0.44, anchor=CENTER)


# Button only detect
but2 = Button(window, padx=5, pady=5, width=30, bg='white', fg='black', relief=GROOVE, command=detect,
              text='Open Camera & Recognition', font=('helvetica 15 bold'))
but2.place(relx=0.5, rely=0.56, anchor=CENTER)

# Button detect & record
but3 = Button(window, padx=5, pady=5, width=30, bg='white', fg='black', relief=GROOVE, command=detectRec,
              text='Recognition & Record', font=('helvetica 15 bold'))
but3.place(relx=0.5, rely=0.68, anchor=CENTER)

# Button exit
but4 = Button(window, padx=5, pady=5, width=30, bg='white', fg='red', relief=GROOVE, text='EXIT', command=exitt,
              font=('helvetica 15 bold'))
but4.place(relx=0.5, rely=0.8, anchor=CENTER)

window.mainloop()