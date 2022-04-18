"""XBPS Repo Manager"""

from os import open as osopen, O_WRONLY, O_CREAT, write, close, replace
from os.path import exists
from tkinter import Tk, LabelFrame, Frame, BOTH, SUNKEN, LEFT, RIGHT
from tkinter import NORMAL, StringVar, Checkbutton, TOP, X, DISABLED
from glob import glob
from .config import *

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

class CheckbuttonRM(Checkbutton):
    """CheckbuttonRM class"""
    def __init__(self, parent, line, **kwargs):
        self.var=StringVar(value=line)
        Checkbutton.__init__(self, parent, **kwargs, command=self.onchange, variable=self.var)
        self.parent=parent
        self.line=line
    def onchange(self):
        value=self.var.get()
        # read file, change only matching value
        lines=[]
# TODO: figure out how to write a file properly 'cos this don't work
#        file_in=open(self.parent.file, r'r', encoding=r'utf-8')
#        file_out=open(f'{self.parent.file}.tmp', r'w', encoding=r'utf-8')
#        count=0
#        for file_line in file_in:
#            if value=='0':
#                if file_line==self.line:
#                    print('Matched line, add comment')
#                    file_out.write(f'#{self.line}')
#                else:
#                    file_out.write(f'{file_line}')
#            else:
#                if file_line==f'#{self.line}':
#                    print('Matched line, remove comment')
#                    file_out.write(f'{self.line}')
#                else:
#                    file_out.write(f'{file_line}')
#            count+=1
#        file_out.close()
#        file_in.close()
#        # move out file over in file
#        replace(f'{self.parent.file}.tmp', self.parent.file)

class Checklist(LabelFrame):
    """Checklist class"""
    def __init__(self, parent, file, **kwargs):
        LabelFrame.__init__(self, parent, **kwargs)
        self.file=file
        with open(file, r'rt', encoding=r'utf-8') as file2:
            lines=file2.readlines()
            file2.close()
        for line in lines:
            if line.find('=')>-1:
                line=line.strip()
                comment=False
                if line[0]=='#':
                    comment=True
                    line=line[1:]
                state=NORMAL
                if line.find('repository=')==-1:
                    state=DISABLED
                chk=CheckbuttonRM(self, line, state=state, text=line, anchor='w', height=1, relief='flat', highlightthickness=0)
                if not comment:
                    chk.select()
                chk.pack(side='top', fill='x', anchor='w')

# TODO: change filenames to adjust order of precedence?
# TODO: Add new entries in custom file

class RepoManager(Tk):
    """XBPS Repo Manager"""
    def __init__(self, args):
        Tk.__init__(self)
        self.args=args
        self.dbg=Debugger()
        # TODO: check we have read/write access to directories, throw if not
        customfile=f'{DR_EXAMPLES}/{ST_CUSTOM_FILENAME}'
        if not exists(customfile):
            file = osopen(customfile, O_WRONLY | O_CREAT)
            write(file, b'#repository=')
            close(file)
        customfile=f'{DR_CONFIG}/{ST_CUSTOM_FILENAME}'
        if not exists(customfile):
            file = osopen(customfile, O_WRONLY | O_CREAT)
            write(file, b'#repository=')
            close(file)
    def start_ui(self):
        """UI start point"""
        self.dbg.out(self.args, r'Args')
        self.title(ST_TITLE)
        self.configure()
        frame = Frame(self, bd=2, padx=5, pady=5)
        frame.pack(fill=BOTH, expand=1)
        # TODO: add vertical scrollbars
        fr_examples = LabelFrame(frame, text='Examples', bd=2,
                                 relief=SUNKEN, padx=5, pady=5)
        fr_examples.pack(side=LEFT, fill=BOTH, expand=1, ipadx=5,
                         ipady=5)
        fr_config = LabelFrame(frame, text='Config', bd=2,
                               relief=SUNKEN, padx=5, pady=5)
        fr_config.pack(side=RIGHT, fill=BOTH, expand=1)
        widgets_examples = {}
        for file in glob(f'{DR_EXAMPLES}/*.conf'):
            lst=Checklist(fr_examples, file, text=file, bd=2,
                          relief=SUNKEN, padx=5, pady=5)
            widgets_examples[file]=lst
            widgets_examples[file].pack(side=TOP, fill=X)
        widgets_config = {}
        for file in glob(f'{DR_CONFIG}/*.conf'):
            lst=Checklist(fr_config, file, text=file, bd=2,
                          relief=SUNKEN, padx=5, pady=5)
            widgets_config[file]=lst
            widgets_config[file].pack(side=TOP, fill=X)
        self.dbg.out(widgets_examples)
        self.dbg.out(widgets_config)
        self.mainloop()
