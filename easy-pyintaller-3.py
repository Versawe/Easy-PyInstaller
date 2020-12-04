import os
import subprocess
import wx
import time
 
# currently saves file where this file/exe is located
# cool future thing could be to find a way to make the 
# executable save in the path location of the .py file itself not this file
 
class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    def OnDropFiles(self, x, y, filename):
        self.window.path = filename
        self.window.text2.Show()
        self.window.text.SetLabel("Path was found: ")
        self.window.text2.SetLabel(self.window.path[0] +"\nClick to continue")
        self.window.sizer.Layout()
        #print(self.window.path)
        return True
 
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Easy-PyInstaller-2')
        panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetBackgroundColour(wx.BLACK)
        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.small_font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
 
        self.path = []
        self.new_path = ""
 
        self.text = wx.StaticText(panel, label="Drag File Here")
        self.text.SetForegroundColour(wx.RED)
        self.text.SetFont(self.font)
        self.sizer.Add(self.text, 0, wx.ALL, 5)
 
        self.text2 = wx.StaticText(panel, label="")
        self.text2.SetForegroundColour(wx.RED)
        self.text2.SetFont(self.small_font)
        self.sizer.Add(self.text2, 0, wx.ALL, 5)
        self.text2.Show(False)
 
        #drag and drop here
        self.text_box = wx.TextCtrl(panel)
        self.text_box.SetBackgroundColour(wx.RED)
        self.sizer.Add(self.text_box, 1, wx.ALL | wx.EXPAND, 5)
        self.dt = MyFileDropTarget(self)
        self.text_box.SetDropTarget(self.dt)
 
        self.findbutton = wx.Button(panel, label='CREATE EXE')
        self.findbutton.Bind(wx.EVT_BUTTON, self.trigger_activation)
        self.sizer.Add(self.findbutton, 0, wx.ALL | wx.CENTER, 5)
 
        self.yesButton = wx.Button(panel, label='YES')
        self.yesButton.Bind(wx.EVT_BUTTON, self.create_build)
        self.sizer.Add(self.yesButton, 0, wx.ALL | wx.CENTER, 5)
        self.yesButton.Show(False)
 
        self.backButton = wx.Button(panel, label='BACK')
        self.backButton.Bind(wx.EVT_BUTTON, self.back_function)
        self.sizer.Add(self.backButton, 0, wx.ALL | wx.CENTER, 5)
        self.backButton.Show(False)
 
        panel.SetSizer(self.sizer)
        self.sizer.Layout()
        self.Show()
 
    def back_function(self, event):
        self.text.SetLabel("Drag File Here")
        self.text_box.Show()
        self.text2.Show(False)
        self.yesButton.Show(False)
        self.findbutton.Show()
        #trying to reset variables here, somehow it stays permanent
        #FIXED just needed to use MyFrame.path instead of self.path
        self.path = []
        self.new_path = ""
        self.backButton.Show(False)
        self.sizer.Layout()
 
    def trigger_activation(self, event):
        self.text2.Show(False)
        if(len(self.path) <= 0):
            self.text.SetLabel("No file dragged in")
            self.text_box.Show(False)
            self.findbutton.Show(False)
            self.backButton.Show()
        else:
            self.new_path = self.path[0]
            #print("path before: "+self.new_path)
            self.new_path = self.new_path.replace("\\", "/")
            #print("path after "+self.new_path)
            if(self.new_path[-3:] != ".py"):
                self.hide_original()
                self.text.SetLabel("Not a .py file")
                self.backButton.Show()
            else:
                self.hide_original()
                self.text.SetLabel("Are You Sure you want\nto make an executable\nfor this file?")
                self.text2.Show()
                self.text2.SetLabel(self.new_path)
                self.yesButton.Show()
                self.backButton.Show()
        self.sizer.Layout()
 
    def hide_original(self):
        self.text_box.Show(False)
        self.findbutton.Show(False)
        self.sizer.Layout()
 
    def create_build(self, event):
        if(os.path.exists(self.new_path)):
            self.text.SetLabel("Creating File...\nPlease Wait")
            self.text2.Show(False)
            self.yesButton.Show(False)
            self.backButton.Show(False)
            self.sizer.Layout()
            time.sleep(0.5)
            wx.Yield()
            cmd = 'PyInstaller --onefile "'+self.new_path+'"'
            subprocess.call(cmd)
            self.text.SetLabel("Executable made Successfully!\nGo back to make another")
            self.yesButton.Show(False)
            self.text_box.Show(False)
            self.backButton.Show()
            self.sizer.Layout()
        else:
            self.text.SetLabel("Something went wrong\nPlease try again")
            self.yesButton.Show(False)
            self.text_box.Show(False)
            self.text2.Show(False)
            self.backButton.Show()
            self.sizer.Layout()
        self.sizer.Layout()
 
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()