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

        name_box = wx.TextEntryDialog(None, "What is your name?", "Welcome",
                                      "name")
        if name_box.ShowModal() == wx.ID_OK:
            user_name = name_box.GetValue()

        yes_no_box = wx.MessageDialog(None, "Poop fart?", "Serious Question",
                                      wx.YES_NO)
        yes_no_answer = yes_no_box.ShowModal()
        yes_no_box.Destroy()

        wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))



        if yes_no_answer == wx.ID_NO:
            user_name = "FartPoop"

        choose_one_box = wx.SingleChoiceDialog(None, "Pick one:", "Picky Picky",
                                               ["Poop", "Fart"])
        if choose_one_box.ShowModal() == wx.ID_OK:
            fav_poop_fart = choose_one_box.GetStringSelection()

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.quit, exit_item)
        self.SetTitle("Welcome " + user_name)

        poop_text = wx.StaticText(panel, -1, "Pooping Farts", (3, 3))
        poop_text.SetForegroundColour("brown")
        poop_text.SetBackgroundColour("yellow")
        poopiest_text = wx.StaticText(panel, -1, "Poopiest Farts", (3, 30))
        poopiest_text. SetForegroundColour("brown" if fav_poop_fart == "Poop"
                                           else "yellow")
        poopiest_text. SetForegroundColour("brown" if fav_poop_fart == "Poop"
                                           else "yellow")


    def quit(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Window(None)
    app.MainLoop()