import PySimpleGUI as sg

sg.theme("DarkGreen4")

layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24), text_color="#FFFF00")],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
    [sg.Text("UNISKA MAB BANJARMASIN")]
]

window = sg.Window(title="Profile", layout=layout, size=(430, 200), font=("Times", 18))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
