import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
    layout=[[sg.Text("SELAMAT DATANG DI KELAS",font=("Arial",25,"bold","italic","underline"))],
            [sg.Text("NPM : 2210010116 ")],
            [sg.Text("Nama : Muhammad Renaldi ")],
            [sg.Text("Kelas : 5P Reg Banjarmasin ")]
            ],
    size=(510,200),
    font=("Times", 18))
window()
window.close()