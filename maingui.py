import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

##### Tkinter stuff ######
root = customtkinter.CTk()
root.title('Multifaceted Music Player(MMP)')
root.geometry('500x580')
pygame.mixer.init()
##########################

list_of_songs = ['music/#Insert music here.mp3'] # Add more MP3S into the music directory.
list_of_covers = ['img/#Insert img here.jpeg'] # Add more JPEGS into the img directory.
n = 0

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((400, 400))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-4] #This is to exlude the other characters
                                                # 6       :      -4
                                    # Example: 'music/ | TLG | .mp3'
                                    # This works because the music will always be between those 2 values
    
    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.4, rely=.6)

def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(.4)
        progressbar.set(pygame.mixer.music.get_pos() / 299999)

def threading():
    t1 = Thread(target=progress)
    t1.start()

def play_music():
    threading()
    global n 
    current_song = n
    if n > 2:
        n = 0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover(song_name, n)

    n += 1

    global paused
    paused = False

def pause_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def skip_forward():
    global n
    n == 2
    play_music()

def skip_back():
    global n
    n -= 2
    play_music()

def volume(value):
    #print(value) #if u care 2 see the volume value in the terminal, un-comment tis btch!
    pygame.mixer.music.set_volume(value)

# All Buttons
play_button = customtkinter.CTkButton(master=root, text='Initiate', command=play_music, width=0)
play_button.place(relx=0.4, rely=0.7, anchor=tkinter.CENTER)

pause_button = customtkinter.CTkButton(master=root, text='Play/Pause', command=pause_music, width=0)
pause_button.place(relx=0.6, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='Next', command=skip_forward, width=0)
skip_f.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='Prev', command=skip_back, width=0)
skip_b.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_= 0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#F29EBA', width=300)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

root.mainloop()