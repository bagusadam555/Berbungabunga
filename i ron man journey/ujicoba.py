import PySimpleGUI as sg

layout = [
    [sg.Text('Masukkan teks:')],
    [sg.InputText()],
    [sg.Button('Cetak')],
    [sg.Output(size=(40, 10))]
]

window = sg.Window('Program Cetak Teks', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Cetak':
        teks = values[0]
        print(teks)

window.close()
