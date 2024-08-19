import json

import PySimpleGUI as sg

# Add your new theme colors and settings
my_new_theme = {'BACKGROUND': '#F2F2F2',
                'TEXT': '#012C38',
                'INPUT': 'lightgrey',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#9EABC4',
                'BUTTON': ('white', '#5F769C'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('MyNewTheme', my_new_theme)

# Switch your theme to use the newly added one. You can add spaces to make it more readable
sg.theme('My New Theme')

# Bild-Datei in Bytes konvertieren
with open("eye.png", "rb") as f:
    image_data = f.read()

# Fenster-Layout definieren
layout = [
    [sg.Text("Add user credentials to Config-File:", font="Arial 20")],

    [sg.Text("Content Credentials.json:", font="Arial 12"), sg.Button("Delete entry:", key="-delEntryButton-", font="Arial 8", button_color="#AC1640", mouseover_colors="#d70000", pad=((95,0),(0,0))), sg.DropDown(("ivsr_client", "cce", "vds", "testApp"), key="-delAppName-", size=25)],
    [sg.Multiline("<empty>",  key="-jsonText-", size=(75, 20), background_color="#BFBFBF", text_color="#012C38")],

    [sg.Text("Select Application:", font="Arial 14"), sg.DropDown(("ivsr_client", "cce", "vds"), key="-appName-", size=25, pad=((30,0),(0,0))), sg.Button("Configurate", key="-config-", font="Arial 13", mouseover_colors="#18C9F9", pad=((8,0),(0,0))), sg.Button("Add", key="-add-", font="Arial 13", mouseover_colors="#18C9F9", pad=((10,0),(0,0)))],


    [sg.Text("", font="Arial 14", key="-headingInput1-", visible=False), sg.InputText(key="-input1-", font="Arial 14", text_color="#548D9E", size=27, pad=(10,0), visible=False)],
    [sg.Text("", font="Arial 14", key="-headingInput2-", visible=False), sg.InputText(key="-input2-", font="Arial 14", text_color="#548D9E", size=27, pad=(10,0), visible=False), sg.Button(image_filename="eye.png", image_data=image_data, image_size=(30,20), key="-checkpw-", pad=((0,0),(0,0)), border_width=2, font="Arial 8", button_color="#7F7F7F", visible=False)],
    [sg.Text("", font="Arial 14", key="-headingInput3-", visible=False), sg.InputText(key="-input3-", font="Arial 14", text_color="#548D9E", size=27, pad=(10,0), visible=False)],
    [sg.Text("", font="Arial 14", key="-headingInput4-", visible=False), sg.InputText(key="-input4-", font="Arial 14", text_color="#548D9E", size=27, pad=(10,0), visible=False)]
]

pwShow = False

# Fenster erstellen
window = sg.Window("Credential Manager", layout, icon="icon.ico", size=(620, 550))

def updateText():
    # Lesen der JSON-Datei in ein Dictionary
    with open("Credentials.json", "r") as f:
        credentials = json.load(f)
    window["-jsonText-"].update(json.dumps(credentials, indent=4))

def clearConfigWindow():
    window["-input1-"].update("")
    window["-headingInput1-"].update(visible=False)
    window["-input1-"].update(visible=False)
    window["-input2-"].update("")
    window["-headingInput2-"].update(visible=False)
    window["-input2-"].update(visible=False)
    window["-input3-"].update("")
    window["-headingInput3-"].update(visible=False)
    window["-input3-"].update(visible=False)
    window["-input4-"].update("")
    window["-headingInput4-"].update(visible=False)
    window["-input4-"].update(visible=False)
    window["-checkpw-"].update(visible=False)

# Ereignis-Schleife
while True:
    window.finalize()
    updateText()
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    if event == "-add-":
        if values["-appName-"] == "":
            sg.popup("Bitte wählen Sie eine Applikation aus \nund konfigurieren Sie diese!", title="Hint", icon="hint.ico")
        if values["-appName-"] in ["ivsr_client"]:
            client_id = values["-input1-"]
            client_secret = values["-input2-"]
            # Lesen der Zugangsdaten aus der Credentials.json Datei
            with open("Credentials.json", "r") as f:
                credentials = json.load(f)
            credentials[values["-appName-"]] = {
                "client_id": client_id,
                "client_secret": client_secret,
            }
            # Schreiben der aktualisierten Credentials in die Datei
            with open("Credentials.json", "w") as f:
                json.dump(credentials, f, indent=4)
        if values["-appName-"] in ["cce", "vds"]:
            username = values["-input1-"]
            password = values["-input2-"]
            # Lesen der Zugangsdaten aus der Credentials.json Datei
            with open("Credentials.json", "r") as f:
                credentials = json.load(f)
            credentials[values["-appName-"]] = {
                "username": username,
                "password": password
            }
            # Schreiben der aktualisierten Credentials in die Datei
            with open("Credentials.json", "w") as f:
                json.dump(credentials, f, indent=4)

        clearConfigWindow()

    if event == "-checkpw-":
        if pwShow == False:
            window["-checkpw-"].update(button_color=("black", "#B2EDFD"))
            window["-input2-"].update(password_char="")
            pwShow = True
        elif pwShow == True:
            window["-checkpw-"].update(button_color=("white", "#7F7F7F"))
            window["-input2-"].update(password_char="*")
            pwShow = False

    if event == "-delEntryButton-":
        try:
            # Lesen der JSON-Datei in ein Dictionary
            with open("Credentials.json", "r") as f:
                credentials = json.load(f)
            # Löschen des "cce" Eintrags
            del credentials[values["-delAppName-"]]
            # Schreiben des aktualisierten Dictionaries in die JSON-Datei
            with open("Credentials.json", "w") as f:
                json.dump(credentials, f, indent=4)
        except KeyError:
            if values["-delAppName-"] == "":
                sg.popup("Bitte wählen Sie eine Applikation aus!", title="Hint", icon="hint.ico")
            else:
                sg.popup("Die App \"" + values["-delAppName-"] + "\" ist nicht in der JSON konfiguriert!", title="App not found", icon="error.ico")

    if event == "-config-":
        clearConfigWindow()
        if values["-appName-"] in ["ivsr_client"]:
            window["-headingInput1-"].update(visible=True)
            window["-headingInput1-"].update("Client ID:\t\t")
            window["-input1-"].update(visible=True)
            window["-headingInput2-"].update(visible=True)
            window["-headingInput2-"].update("Client Secret:\t")
            window["-input2-"].update(visible=True)
        if values["-appName-"] in ["cce", "vds"]:
            window["-headingInput1-"].update(visible=True)
            window["-headingInput1-"].update("Username:\t")
            window["-input1-"].update(visible=True)
            window["-headingInput2-"].update(visible=True)
            window["-headingInput2-"].update("Password:\t")
            window["-input2-"].update(visible=True)
            window["-input2-"].update(password_char="*")
            window["-checkpw-"].update(visible=True)
            window["-checkpw-"].update(button_color=("white", "#7F7F7F"))
            pwShow = False

# Fenster schließen
window.close()