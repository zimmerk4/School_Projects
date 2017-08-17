import wx


class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self). __init__(*args, **kwargs)
        self.basic_GUI()
        self.Center()
        self.Show()

    def basic_GUI(self):
        panel = wx.Panel(self)

        menu_bar = wx.MenuBar()

        file_button = wx.Menu()
        edit_button = wx.Menu()

        exit_item = file_button.Append(wx.ID_EXIT, "Exit", "status msg..")

        menu_bar.Append(file_button, "File")
        menu_bar.Append(edit_button, "Edit")

        name_box = wx.TextEntryDialog(None, "What is your name?", "Welcome", "name")
        if name_box.ShowModal() == wx.ID_OK:
            user_name = name_box.GetValue()

        yes_no_box = wx.MessageDialog(None, "Poop fart?", "Serious Question", wx.YES_NO)
        yes_no_answer = yes_no_box.ShowModal()
        yes_no_box.Destroy()

        wx.TextCtrl(panel, pos=(10, 10), size=(250, 150))
        if yes_no_answer == wx.ID_NO:
            user_name = "FartPoop"

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.quit, exit_item)
        self.SetTitle("Welcome " + user_name)

    def quit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Window(None)
    app.MainLoop()