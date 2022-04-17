"""XBPS Repo Manager"""

import tkinter

DEBUG_MODE=True

class Debugger():
    """Debug assistant class"""
    def __init__(self):
        self.last='' # no reason for this, shuts up pylint
    def out(self, line, prefix=''):
        """Output some data"""
        self.last=line
        if DEBUG_MODE:
            if prefix=='':
                print(line)
            else:
                print(f'{prefix}: {line}')

class RepoManager():
    """XBPS Repo Manager"""
    def __init__(self, args):
        self.args=args
        self.dbg=Debugger()
    def start_ui(self):
        """UI start point"""
        self.dbg.out(self.args, r'Args')
        self.dbg.out(r'test')
#
##!/bin/python
#
#import tkinter
#import os
#
#ST_TITLE = "xbps-repoman"
#
#CO_BGD = "#ffffff"
#CO_HILIGHT = "#ff0000"
#
#DR_EXAMPLES = "/usr/share/xbps.d"
#DR_CONFIG = "/etc/xbps.d"
#
## tags:
## st - sanitised text
## co - colour
## dr - directory
#
#class CheckList(tkinter.Frame):
#    def __init__(self, parent, choices, **kwargs):
#        tkinter.Frame.__init__(self, parent, **kwargs)
#
#        self.vars = []
#        bg = self.cget("background")
#        for choice in choices:
#            var = tkinter.StringVar(value=choice)
#            self.vars.append(var)
#            cb = tkinter.Checkbutton(self, var=var, text=choice,
#                                onvalue=choice, offvalue="",
#                                anchor='w', width=20, background=bg,
#                                relief='flat', highlightthickness=0)
#            cb.pack(side='top', fill='x', anchor='w')
#    def getCheckedItems(self):
#        values = []
#        for var in self.vars:
#            value = var.get()
#            if value:
#                values.append(value)
#        return values
#
#if __name__ == 'main':
#    wwMain = tkinter.Tk()
#    wwMain.title(ST_TITLE)
#    wwMain.configure(background=CO_BGD)
#    wwMain.rowconfigure(0, weight=1)
#    wwMain.columnconfigure(0, weight=1)
#
#    print('here')
#    choices = ("A", "B", "C")
#    checklist = CheckList(wwMain, choices, bd=1, relief='sunken', background=CO_BGD)
#    checklist.pack()
#    wwMain.mainloop()
