import PySimpleGUI as sg
sg.theme("DarkGreen4") 

layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24), text_color="#FFFFFF")],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "italic bold underline"), text_color="#FFFF00")],
    [sg.Text("UNISKA MAB BANJARMASIN", font=("Times", 18), text_color="#FFCC00")]
]

window = sg.Window(title="Profile", layout=layout, size=(430, 200), font=("Times", 18))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()