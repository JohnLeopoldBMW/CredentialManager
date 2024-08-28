import wx

class LoginWindow(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Login')
        panel = wx.Panel(self)

        # Erstellen der Widgets
        self.username_label = wx.StaticText(panel, label="Benutzername:")
        self.username_input = wx.TextCtrl(panel)
        self.password_label = wx.StaticText(panel, label="Passwort:")
        self.password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        self.login_button = wx.Button(panel, label="Anmelden")
        self.login_button.Bind(wx.EVT_BUTTON, self.login)

        # Layout erstellen
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.username_label, 0, wx.TOP | wx.LEFT, 10)
        vbox.Add(self.username_input, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 10)
        vbox.Add(self.password_label, 0, wx.TOP | wx.LEFT, 10)
        vbox.Add(self.password_input, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 10)
        vbox.Add(self.login_button, 0, wx.TOP | wx.ALIGN_CENTER, 10)
        panel.SetSizer(vbox)

        self.SetSize((300, 200))
        self.Centre()

    def login(self, event):
        username = self.username_input.GetValue()
        password = self.password_input.GetValue()

        # Hier können Sie Ihre Anmeldelogik implementieren
        if username == "admin" and password == "password":
            print("Anmeldung erfolgreich!")
        else:
            wx.MessageBox("Ungültiger Benutzername oder Passwort.", "Fehler", wx.OK | wx.ICON_ERROR)

if __name__ == '__main__':
    app = wx.App()
    window = LoginWindow()
    window.Show()
    app.MainLoop()