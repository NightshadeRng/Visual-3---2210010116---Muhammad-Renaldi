import PySimpleGUI as sg

layout = [
    [sg.Titlebar("Contoh Button")],
    [sg.Text("Contoh Button")],
    [sg.Button("Button Simpan")],
    [sg.Button("Button Keluar")]
]

window = sg.Window("Contoh Button", layout, size=(400, 200), font=("Times", 18))

while True:
    event, values = window.read()
    
    if event == "Button Simpan":
        print("Button Simpan clicked")
        
    elif event == "Button Keluar":
        print("Button Keluar clicked")
        
    elif event == sg.WINDOW_CLOSED:
        print("Window closed")
        break

window.close()
