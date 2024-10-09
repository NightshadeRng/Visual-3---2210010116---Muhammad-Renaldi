import PySimpleGUI as sg
sg.theme_background_color('#FF0000')
sg.theme_text_color('#0000FF') 
window = sg.Window(title="Profile",
    layout=[[sg.Text("NPM       : 2210010116 ")],
            [sg.Text("Nama      : Muhammad Renaldi ")],
            [sg.Text("Kelas     : 5P Reg Banjarmasin ")],
            {sg.Text("Matkul    : Pemrograman Visual 3")}
            ], size=(400, 200))
window()
window.close()