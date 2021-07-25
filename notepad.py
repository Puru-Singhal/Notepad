from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    Textarea.delete(1.0, END)

def openfile():
    global file
    file=askopenfilename(defaultextension="txt",filetypes=[("All Files","*.*"),("Text documents","*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension="txt",
                               filetypes=[("All Files","*.*"),("Text documents","*.txt")])
        if file=="":
            file=None
        else:
            #save as a new file
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ "-Notepad")
            print("FIle saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    Textarea.event_generate("<<Cut>>")

def copy():
    Textarea.event_generate("<<Copy>>")

def paste():
    Textarea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad","Notepad made by Puru Singhal")

if __name__ == '__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    #add textarea
    Textarea=Text(root,font="lucida 13")
    file= None
    Textarea.pack(fill=BOTH,expand=True)

    #lets create a menubar
    Menubar=Menu(root)
    #filemenu starts
    filemenu=Menu(Menubar,tearoff=0)

    #to open new file
    filemenu.add_command(label="New",command=newfile)

    #to open already existing file
    filemenu.add_command(label="Open",command=openfile)

    #to save current file
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitapp)
    Menubar.add_cascade(label="File",menu=filemenu)
    #filemenu ends

    #edit menu starts
    editmenu=Menu(Menubar,tearoff=0)
    #to give feature of cut,copy and paste
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)

    Menubar.add_cascade(label="Edit",menu=editmenu)
     #edit menu ends

    #help menu starts

    helpmenu=Menu(Menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=helpmenu)
    #help menu ends

    root.config(menu=Menubar)
    #adding scrollbar
    Scroll=Scrollbar(Textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()