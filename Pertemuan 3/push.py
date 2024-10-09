import PySimpleGUI as sg

susunan = [
    [sg.Push(), sg.Text("UNISKA MAAB", font=("Helvetica", 24)), sg.Push()],
    [sg.Push(), sg.Text("BANJARMASIN", font=("Courier", 18)), sg.Push()]
]

window = sg.Window(title="Elemen Text", layout=susunan, size=(430, 200))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()