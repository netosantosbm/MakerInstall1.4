
import PySimpleGUI as sg


layout = [[sg.T("")], [sg.T("        "), sg.Button('Iniciar', key='-INIC-',size=(9, 1))], [sg.T("")],
          [sg.T("         "), sg.Checkbox('Backup:', default=False, key="-BKP-"),sg.Checkbox('Restore:', default=False, key="-RES-")],
          ]


window = sg.Window('Push my Buttons', layout, size=(300, 300))



while True:
        event, values = window.read()
        checkBox =''
        if event == sg.WIN_CLOSED or event == "Exit":
                break
        if values["-BKP-"] == True:
                checkBox = 'Teste1'

        if values["-RES-"] == True:
                checkBox = 'Teste2'


        if event == '-INIC-':
                print(checkBox)
window.close()