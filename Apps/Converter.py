import PySimpleGUI as sg

# =============================================================================
# POSSIBLE IMPOROVEMENTS
# 
# add extra file with if statements
# add extra functionality with extra units (decadic or even different properties)
#
# =============================================================================


layout = [
    [
     sg.Text('Please enter Initial units'),
     sg.Input(key='-INPUT-'),
     sg.Spin(['km', 'm', 'cm', 'mm'], key='-INIT-')
     ],
    
    [
     sg.Text('Please enter Target units'), 
     sg.Text('', key='-OUTPUT-'), 
     sg.Spin(['km', 'm', 'cm', 'mm'], key='-TARGET-')
     ],
    
    [
     sg.Button('Covert', key = '-CONVERT-')
     ]
    ]

window = sg.Window(title = 'Converter', layout = layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        #checking if user input is number
        try:
            float(input_value)
            input_value = float(input_value)
            
            if values['-INIT-']== 'km' and  values['-TARGET-'] == 'km':
                output = input_value * 1
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'km' and  values['-TARGET-'] == 'm':
                output = input_value * 1e3
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'km' and  values['-TARGET-'] == 'cm':
                output = input_value * 1e5
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'km' and  values['-TARGET-'] == 'mm':
                output = input_value * 1e6
                window['-OUTPUT-'].update(output)
                continue
            
            
            if values['-INIT-']== 'm' and  values['-TARGET-'] == 'km':
                output = input_value * 1e-3
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'm' and  values['-TARGET-'] == 'm':
                output = input_value * 1
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'm' and  values['-TARGET-'] == 'cm':
                output = input_value * 1e2
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'm' and  values['-TARGET-'] == 'mm':
                output = input_value * 1e3
                window['-OUTPUT-'].update(output)
                continue
            
            
            
            if values['-INIT-']== 'cm' and  values['-TARGET-'] == 'km':
                output = input_value * 1e-5
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'cm' and  values['-TARGET-'] == 'm':
                output = input_value * 1e-2
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'cm' and  values['-TARGET-'] == 'cm':
                output = input_value * 1
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'cm' and  values['-TARGET-'] == 'mm':
                output = input_value * 1e1
                window['-OUTPUT-'].update(output)
                continue
            
            
            
            if values['-INIT-']== 'mm' and  values['-TARGET-'] == 'km':
                output = input_value * 1e-6
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'mm' and  values['-TARGET-'] == 'm':
                output = input_value * 1e-3
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'mm' and  values['-TARGET-'] == 'cm':
                output = input_value * 1e-1
                window['-OUTPUT-'].update(output)
                continue
            
            if values['-INIT-']== 'mm' and  values['-TARGET-'] == 'mm':
                output = input_value * 1
                window['-OUTPUT-'].update(output)
                continue
            
     
        
        except:
             output = 'ERROR: INVALID INPUT, please use numeric values '
             window['-OUTPUT-'].update(output)
       
window.close()
    