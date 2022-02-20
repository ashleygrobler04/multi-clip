#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import wx, json, clipboard

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        self.savedData="clipdata.json"
        self.res=self.load(self.savedData)

        # begin wxGlade: MyFrame.__init__()
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.SetSize((400, 300))
        self.SetTitle("frame")


        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Clipboard History")
        sizer_1.Add(label_1, 0, 0, 0)

        self.choices=[]
        self.initListBox()
        self.list_box_1 = wx.ListBox(self.panel_1, wx.ID_ANY, choices=self.choices)
        sizer_1.Add(self.list_box_1, 0, 0, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Copy")
        sizer_1.Add(self.button_1, 0, 0, 0)
        self.button_1.Bind(wx.EVT_BUTTON, self.copy)
        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "Save")
        sizer_1.Add(self.button_2, 0, 0, 0)
        self.button_2.Bind(wx.EVT_BUTTON, self.onSave)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

    def initListBox(self):
        self.choices=[]
        for v in self.res:
            self.choices.append(v)

    def copy(self, e):
        text=self.choices[self.list_box_1.GetSelection()]
        clipboard.copy(self.res[text])

    def load(self, file):
        try:
            with open(file, 'r') as f:
                data=json.load(f)
                return data
        except:
            return {}

    def saveItems(self, path, data):
        with open (path, 'w') as f:
            json.dump(data, f)


    def input(self, text, title):
        t=wx.TextEntryDialog(None, text, title)
        t.ShowModal()
        res=t.GetValue()
        t.Destroy()
        return res

    def onSave(self, e):
        key=self.input("Enter key", "enter key")
        self.res[key]=clipboard.paste()
        self.saveItems(self.savedData, self.res)
        self.choices.append(key)
        self.list_box_1.Set(self.choices)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
