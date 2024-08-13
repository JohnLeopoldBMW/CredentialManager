import PySimpleGUI as sg

icon_path = "C://01_FG-790//CredentialManager//icon.png"

# Fenster-Layout definieren
layout = [
    [sg.Text("Add user credentials to Config-File:", font="Arial 20")]
]

# Fenster erstellen
window = sg.Window("Credential Manager", layout, icon=icon_path, size=(500, 200))

# Ereignis-Schleife
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break

# Fenster schließen
window.close()