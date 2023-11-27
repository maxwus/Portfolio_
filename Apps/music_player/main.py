import PySimpleGUI as sg
import pygame as pg
import base64
from io import BytesIO
from PIL import Image

def base64_image_import(path):
    image = Image.open(path)
    buffer = BytesIO()
    image.save(buffer, format = 'PNG')
    b64 = base64.b64encode(buffer.getvalue())
    return b64
    
base64_image_import('play.png')

sg.theme('reddit')

play_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text('Song name', font = 'Arial 20'), sg.Push()],
    [sg.VPush()],
    [
     sg.Push(),
     sg.Button(image_data = base64_image_import('play.png'), button_color = 'white', border_width = 0, key = '-PLAY-'),
     sg.Text(''),
     sg.Button(image_data = base64_image_import('pause.png'), button_color = 'white', border_width = 0, key = '-CLOSE-'),
     sg.Push()
     ],
    [sg.VPush()],
    [sg.Progress(100, size = (20, 20), key = '-PROGRESS-')]
    ]



volume_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Slider(range = (0,100), default_value = 100, orientation = 'h', key = '-VOLUME-'), sg.Push()],
    [sg.VPush()]
    ]





layout = [
    [sg.TabGroup([[sg.Tab('Play', play_layout), sg.Tab('Volume', volume_layout)]])]
    ]

window = sg.Window('Music player', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
window.close()