import os
import subprocess
import wx

class MyFrame(wx.Frame):

    new_path = ""
    fresh_string = ""

    def __init__(self):
        super().__init__(parent=None, title='Easy-PyInstaller-2')
        panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetBackgroundColour(wx.BLACK)
        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)


        #drag and drop here
        self.text = wx.StaticText(panel, label="Drag file Here")
        self.text.SetForegroundColour(wx.RED)
        self.text.SetFont(self.font)
        self.sizer.Add(self.text, 0, wx.ALL, 5)

        self.text_box = wx.TextCtrl(panel)
        self.text_box.SetBackgroundColour(wx.RED)
        self.sizer.Add(self.text_box, 1, wx.ALL | wx.EXPAND, 5)
        dt = MyFileDropTarget(self)
        self.text_box.SetDropTarget(dt)


        self.findbutton = wx.Button(panel, label='Create Executable')
        self.findbutton.Bind(wx.EVT_BUTTON, self.make_magic_happen)
        self.sizer.Add(self.findbutton, 0, wx.ALL | wx.CENTER, 5)
        self.aYSText = wx.StaticText(panel, label="Are You Sure you want\nto make an executable\nfor this file?")
        self.aYSText.SetForegroundColour(wx.RED)
        self.aYSText.SetFont(self.font)
        self.sizer.Add(self.aYSText, 0, wx.ALL, 5)
        self.aYSText.Show(False)

        self.yesButton = wx.Button(panel, label='yes')
        self.yesButton.Bind(wx.EVT_BUTTON, self.commence_cool)
        self.sizer.Add(self.yesButton, 0, wx.ALL | wx.CENTER, 5)
        self.yesButton.Show(False)

        self.noPIE = wx.StaticText(panel, label="Not a .py file extension")
        self.noPIE.SetForegroundColour(wx.RED)
        self.noPIE.SetFont(self.font)
        self.sizer.Add(self.noPIE, 0, wx.ALL, 5)
        self.noPIE.Show(False)


        self.backButton = wx.Button(panel, label='Back')
        self.backButton.Bind(wx.EVT_BUTTON, self.back_bruh)
        self.sizer.Add(self.backButton, 0, wx.ALL | wx.CENTER, 5)
        self.backButton.Show(False)

        panel.SetSizer(self.sizer)

        self.Show()


    def make_magic_happen(self, event):
        if(self.new_path == "" or self.new_path == " "):
            print("error")
            self.text_box.Show(False)
            self.text.Show(False)
            self.findbutton.Show(False)
            self.backButton.Show() 
        else:
            self.fresh_string = self.new_path[0]
            self.fresh_string = self.fresh_string.replace("\\", "/")
            print(self.fresh_string)
            if(self.fresh_string[-3:] != ".py"):
                print("not a py file")
                self.hide_original()
                self.noPIE.Show()
                self.backButton.Show()
            else:
                print("py file")
                print("are you sure?")
                self.hide_original()
                self.aYSText.Show()
                self.yesButton.Show()
                self.backButton.Show()

        self.sizer.Layout()

    def back_bruh(self, event):
        self.text.Show()
        self.text_box.Show()
        dt = MyFileDropTarget(self)
        self.text_box.SetDropTarget(dt)
        self.backButton.Show(False)
        self.aYSText.Show(False)
        self.yesButton.Show(False)
        self.noPIE.Show(False)
        self.findbutton.Show()
        self.sizer.Layout()


    def hide_original(self):
        self.text.Show(False)
        self.text_box.Show(False)
        self.findbutton.Show(False)
        self.sizer.Layout()

    def commence_cool(self, event):
        print("cool")
        self.sizer.Layout()


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.path = ""


    def OnDropFiles(self, x, y, filename):
        path = filename
        MyFrame.new_path = path
        return True


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()