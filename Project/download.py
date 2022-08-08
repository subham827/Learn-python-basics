from tkinter import *
from tkinter import filedialog
from turtle import color
from moviepy import *
from moviepy.editor import *
from pytube import YouTube
import shutil



def select_path():
    global path
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    yt = YouTube(get_link).streams.get_highest_resolution().download()
    video = VideoFileClip(yt)
    video.close()
    shutil.move(yt, user_path)
    screen.title("Downloaded !")


screen = Tk()
title = screen.title("Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter the link:", font=("Arial", 15))
canvas.create_window(250, 100, window=link_label)
canvas.create_window(250, 130, window=link_field)

path_label = Label(screen, text="Enter the path:", font=("Arial", 15))
select_btn = Button(screen, text="Select" , command=select_path)

canvas.create_window(250, 200, window=path_label)
# path_field = Entry(screen, width=50)
canvas.create_window(250, 230, window=select_btn)
download_btn = Button(screen, text="Download", command=download)
canvas.create_window(250, 270, window=download_btn)


screen.mainloop()