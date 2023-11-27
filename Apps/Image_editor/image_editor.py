import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

def update_image(image, blur, contrast, emboss, contour, flipx, flipy):
    filtered_image = image.copy()
    
    filtered_image = filtered_image.filter(ImageFilter.GaussianBlur(blur))
    filtered_image = filtered_image.filter(ImageFilter.UnsharpMask(contrast))
    
    if emboss:
        filtered_image = filtered_image.filter(ImageFilter.EMBOSS())
    if contour:
        filtered_image = filtered_image.filter(ImageFilter.CONTOUR())
    if flipx:
        filtered_image = ImageOps.mirror(filtered_image)
    if flipy:
        filtered_image = ImageOps.flip(filtered_image)
    
    bio = BytesIO()
    filtered_image.save(bio, format='PNG')
    window['-IMAGE-'].update(data=bio.getvalue())

default_pic = 'white.png'

control_col = sg.Column([
    [sg.Button('Open', key='-OPEN-')],
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Contour', key='-CONTOUR-')],
    [sg.Button('Save image', key='-SAVE-')]
])

image_col = sg.Column([[sg.Image(default_pic, key='-IMAGE-')]])

layout = [[control_col, image_col]]
image = Image.open(default_pic)  # Load the default image

window = sg.Window('Image Editor', layout)

while True:
    event, values = window.read(timeout=50)
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == '-SAVE-':
        save_path = sg.popup_get_file('Save', save_as=True, no_window=True) + '.png'
        image.save(save_path)
    
    if event == '-OPEN-':
        image_path = sg.popup_get_file('Open', no_window=True)
        image = Image.open(image_path)
    
    update_image(image, 
                 values['-BLUR-'],
                 values['-CONTRAST-'],
                 values['-EMBOSS-'],
                 values['-CONTOUR-'],
                 values['-FLIPX-'],
                 values['-FLIPY-']
                 )
    
window.close()