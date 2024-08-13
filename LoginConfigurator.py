import json
import PySimpleGUI as sg
import tkinter as tk

icon_path = "icon.png"

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

# Fenster-Layout definieren
layout = [
    [sg.Text("Add user credentials to Config-File:", font="Arial 20")],
    [sg.Text("App Name: ", font="Arial 14"), sg.InputText(key="-appName-", font="Arial 14", text_color="#548D9E", size=30), sg.Button("x", key="-delName-", button_color="#7F7F7F", mouseover_colors="#CD738C", border_width=2, pad=((5,0)))],
    [sg.Text("Q-Number :", font="Arial 14"), sg.InputText(key="-qNumber-", font="Arial 14", text_color="#548D9E", size=30, pad=(7,0)), sg.Button("x", key="-delQNumber-", button_color="#7F7F7F", mouseover_colors="#CD738C", border_width=2, pad=(3,0))],
    [sg.Text("ID:              ", font="Arial 14"), sg.InputText(key="-secret_id-", font="Arial 14", text_color="#548D9E", password_char="*", size=30, pad=(10,0)), sg.Button("x", key="-delID-", button_color="#7F7F7F", mouseover_colors="#CD738C", border_width=2, pad=(0,0))],
    [sg.Text("Password: ", font="Arial 14"), sg.InputText(key="-secret_pw-", font="Arial 14", text_color="#548D9E", password_char="*", size=30, pad=(10,0)), sg.Button("x", key="-delPW-", button_color="#7F7F7F", mouseover_colors="#CD738C", border_width=2, pad=(1,0))],
    [sg.Button("show passwords", key="-checkpw-", pad=((118,0),(0,0)), font="Arial 8", button_color="#7F7F7F"), sg.Button("clear all", key="-clearAll-", font="Arial 8", button_color="#7F7F7F", mouseover_colors="#CD738C",pad=((224,0),(0,0)))],
    [sg.Button("Add", key="-add-", font="Arial 14", mouseover_colors="#18C9F9")],
    [sg.Text("Content Credentials.json:", font="Arial 12"), sg.Button("Delete entry:", key="-delEntryButton-", font="Arial 8", button_color="#AC1640", mouseover_colors="#d70000"), sg.InputText(key="-delEntry-", text_color="#548D9E", size=29)],
    [sg.Multiline("<empty>",  key="-jsonText-", size=(65, 50), background_color="#BFBFBF", text_color="#012C38")],
]

pwShow = False
appName = ""
qNumber = ""
secret_id = ""
secret_pw = ""

# Fenster erstellen
window = sg.Window("Credential Manager", layout, icon=icon_path, size=(520, 700))

def updateText():
    with open("Credentials.json", "r") as f:
        data_old = json.load(f)
    data = {
        "credentials": data_old["credentials"]
    }
    try:
        with open("Credentials.json", "r") as f:
            data_old = json.dumps(data, indent=4)
            window["-jsonText-"].update(data_old)
    except (FileNotFoundError, json.JSONDecodeError):
        window["-jsonText-"].update("JSON file not found!")


# Ereignis-Schleife
while True:
    window.finalize()
    updateText()
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    if event == "-add-":
        appName = values["-appName-"]
        qNumber = values["-qNumber-"]
        secret_id = values["-secret_id-"]
        secret_pw = values["-secret_pw-"]

        # Variablen in ein Dictionary packen
        data = {
            "credentials": [
                {
                    "appName": appName,
                    "qNumber": qNumber,
                    "secretId": secret_id,
                    "secretPw": secret_pw
                }
            ]
        }

        try:
            with open("new.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("Credentials.json", "r") as f:
                data_old = json.load(f)
            with open("new.json", "r") as f:
                data_new = json.load(f)
            data = {
                "credentials": data_old["credentials"] + data_new["credentials"]
            }
            with open("Credentials.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("Credentials.json", "r") as f:
                data_old = json.dumps(data, indent=4)
                window["-jsonText-"].update(data_old)
        except (FileNotFoundError, json.JSONDecodeError):
            data_old = []

        window["-appName-"].update("")
        window["-qNumber-"].update("")
        window["-secret_id-"].update("")
        window["-secret_pw-"].update("")

    if event == "-checkpw-":
        if pwShow == False:
            window["-checkpw-"].update(button_color=("black", "#B2EDFD"))
            window["-secret_id-"].update(password_char="")
            window["-secret_pw-"].update(password_char="")
            pwShow = True
        elif pwShow == True:
            window["-checkpw-"].update(button_color=("white", "#7F7F7F"))
            window["-secret_id-"].update(password_char="*")
            window["-secret_pw-"].update(password_char="*")
            pwShow = False

    if event == "-delName-":
        window["-appName-"].update("")
    if event == "-delQNumber-":
        window["-qNumber-"].update("")
    if event == "-delID-":
        window["-secret_id-"].update("")
    if event == "-delPW-":
        window["-secret_pw-"].update("")
    if event == "-clearAll-":
        window["-appName-"].update("")
        window["-qNumber-"].update("")
        window["-secret_id-"].update("")
        window["-secret_pw-"].update("")

    if event == "-delEntryButton-":
        found = False
        target = values["-delEntry-"]
        # Öffne die JSON-Datei und lies den Inhalt ein
        with open('Credentials.json', 'r') as file:
            data = json.load(file)
        # Finde den Index des Elements mit appName "App2"
        for i, credential in enumerate(data["credentials"]):
            if credential["appName"] == target:
                if target == values["-delEntry-"]:
                    found = True
                break
        # Entferne den gewünschten Eintrag
        if found == True:
            del data['credentials'][i]
        # Schreibe das aktualisierte Objekt zurück in die JSON-Datei
        with open('Credentials.json', 'w') as file:
            json.dump(data, file, indent=4)
        updateText()
        window["-delEntry-"].update("")

# Fenster schließen
window.close()