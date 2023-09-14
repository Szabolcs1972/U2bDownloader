import pytube
from pytube import YouTube
import PySimpleGUI as sg
import os
import time
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def on_progress_audio(pwindow, chunk, bytesremaining):
    percentages = range(0,101,1)

    for count in percentages:
            time.sleep(0.1)
            window['-PBAR-'].update(count)


def on_progress_video(pwindow, chunk, bytesremaining):
    percentages = range(0,101,1)

    for count in percentages:
            time.sleep(0.5)
            window['-PBAR-'].update(count)


def download_audio(plink):
    youtube_object = YouTube(link, on_progress_callback=on_progress_audio(window,None,None))
    youtube_object = youtube_object.streams.get_audio_only()

    try:
        downloaded_file = youtube_object.download()
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)
    except:
        window["-TEXT-"].update("An error occured!")

    window["-TEXT-"].update("Done! The file has been downloaded successfully!")
    window['-PBAR-'].update(0)


def download_video(plink):
    youtube_object = YouTube(link, on_progress_callback=on_progress_video(window,None,None))
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
         window["-TEXT-"].update("An error occured!")
    window["-TEXT-"].update("Done! The file has been downloaded successfully!")
    window['-PBAR-'].update(0)


menu_def = [['Help', ['ReadMe', 'Notice']]]
layout = [[sg.Menu(menu_def)], [sg.Text("Copy the YouTube - Share link - in the textbox (for example):")], [sg.In("https://youtu.be/KDxJlW6cxRk?si=OnZnf9SPR83cSrpU", size=(50, 1), enable_events=True, key="-INPUT-")], [sg.Radio('Video (mp4)', "RADIO1", default=False, key="-INPUT2-")], [sg.Radio('Audio (mp3)', "RADIO1", default=True)], [sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20),  key='-PBAR-')], [sg.Button("Download")], [sg.Text("and press Download, if you are ready!", key="-TEXT-")]]

# Create the window
window = sg.Window("U2b Downloader", layout, margins=(30, 25),)
window.set_icon("mosomaci.ico")

# Create an event loop
while True:
    event, values = window.read()
    if event == 'ReadMe':
        window["-TEXT-"].update("ReadMe")
        sg.popup_scrolled("Hardware & Software Requirements:",
                          "- PC with Windows 11",
                          "",
                          "Installation:",
                          "- Copy the Windows executable in any folder in your machine",
                          "- Double click to the u2bdownloader.exe to start the program",
                          "- The video or the music is going to be downloaded in the same folder.",
                          "",
                          "The process of the downloads:",
                          "1. Find your favourite video In YouTube",
                          "2. Press the Share button under your video",
                          "3. Copy the link to the textbox of your U2b Downloader",
                          "4. Please, write over the link of the example. It is the 'Ocean Drive' :)",
                          "5. The program is cheching your link starts with: https://youtu.be/",
                          "6. Select Video or Audio with the radio buttons",
                          "If you select - Video - is going to be downloaded with the best quality in mp4 video format.",
                          "If you select - Audio - it is goig to be downloaded as music with mp3 file extesion.",
                          "7. Press the Download button!",
                          "8. The downloading is going to be finished, when you can see the message:",
                          "- Done! The file has been downloaded successfully! - ",
                          "and the progress indicator sets to Zero again.",
                          "",
                          "Thanks for feedbacks!",
                          "",
                          "Happy downloading!",
                          title="ReadMe", icon="mosomaci.ico", size=(80, 10))

    if event == 'Notice':
        window["-TEXT-"].update("Notice")
        sg.popup_scrolled("License: Free, open source, CC BY 4.0",
                          "Icon - CC BY 4.0 https://iconduck.com/icons/176906/raccoon",
                          "",
                          "Used software products:",
                          "PyCharm - by JetBrains s.r.o.",
                          "Python 3 extensions",
                          "- pytube",
                          "- PySimpleGUI",
                          "- pyinstaller",
                          "",
                          "Dr. Szlávik Szabolcs, 2023",
                          "https://www.szlavikszabolcs.hu/",
                          "https://github.com/Szabolcs1972/",
                          title="Notice", icon="mosomaci.ico", size=(50, 10))

    if event == "Download":

        link = values["-INPUT-"]
        if str(link).__contains__("https://youtu.be/"):
            if values["-INPUT2-"] is False:
                window["-TEXT-"].update("Downloading audio...")

                try:
                    download_audio(link)
                except:
                    window["-TEXT-"].update("An error occurred!")
            if values["-INPUT2-"] is True:
                window["-TEXT-"].update("Downloading video...")

                try:
                    download_video(link)
                except:
                    window["-TEXT-"].update("An error occured!")

        else:
            window["-TEXT-"].update("It seems, it is not a 'youtu.be' link!")

    if event == sg.WIN_CLOSED:
        break
window.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
