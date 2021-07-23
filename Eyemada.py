#!/bin/python3
from tkinter import *
import subprocess
import socket
import validators
from tkinter.font import families

from validators.utils import ValidationFailure
root = Tk()
root.geometry('800x600')
root.resizable(width=False, height=False)
root.title("Armada")
root.config(bg='grey20')

MainStr = ""

Main = Text(root, relief=SOLID, fg='grey85', bg='gray35')
Main.config(wrap=WORD)
Main.place(width = 500, height = 400, x=300, y=200)

inputLabel = Label(root, text="Target Parameters")
inputLabel.place(height=25, width=250, x=0, y=0)

target = Text(root, relief=SOLID, fg='grey85', bg='gray35')
target.place(width = 150, height=25, x=100, y=25)

targetLBL = Label(root, text="Target", relief=SOLID, fg='grey85', bg='gray35')
targetLBL.place(width = 100, height=25, x=0, y=25)

targetDefault = Label(root, text="URL, IP, or CIDR", font=("TkDefaultFont",10), anchor=W, relief=FLAT, fg='grey85', bg='gray20')
targetDefault.place(width = 250, height=15, x=0, y=50)

ports = Text(root, relief=SOLID, fg='grey85', bg='gray35')
ports.place(width = 150, height=25, x=100, y=65)

portsLBL = Label(root, text="Ports", relief=SOLID, fg='grey85', bg='gray35')
portsLBL.place(width = 100, height=25, x=0, y=65)

portsDefault = Label(root, text="defaults to top 1000", font=("TkDefaultFont",10), anchor=W, relief=FLAT, fg='grey85', bg='gray20')
portsDefault.place(width = 250, height=15, x=0, y=90)

scanName = Text(root, relief=SOLID, fg='grey85', bg='gray35')
scanName.place(width = 150, height=25, x=100, y=105)

ScanNameLBL = Label(root, text="Scan Name", relief=SOLID, fg='grey85', bg='gray35')
ScanNameLBL.place(width = 100, height=25, x=0, y=105)

ScanNameDefault = Label(root, text="defaults to target", font=("TkDefaultFont",10), anchor=W, relief=FLAT, fg='grey85', bg='gray20')
ScanNameDefault.place(width = 250, height=15, x=0, y=130)

ScanList = Label(root, text="Scans")
ScanList.place(width=140, height=40, x=160, y=200)

Scan0Str=""   
Scan1Str=""   
Scan2Str=""   
Scan3Str=""   
Scan4Str=""   
Scan5Str=""   
Scan6Str=""   
Scan7Str=""   
Scan8Str=""  

taken0 = False
taken1 = False
taken2 = False
taken3 = False
taken4 = False
taken5 = False
taken6 = False
taken7 = False
taken8 = False

def Scan0In():
    global Scan0Str
    Main.delete('1.0', END)
    Main.insert(END, Scan0Str)
def Scan0Rm():
    global Scan0Str
    global ScanCt
    global taken0
    Scan0.config(text="")
    Scan0Str = ""
    Main.delete('1.0', END)
    if ScanCt > 0:
        ScanCt = 0
    taken0 = False
Scan0 = Button(root, command=Scan0In)
Scan0.place(width=125, height=40, x=160, y=240)
Scan0RM = Button(root, command=(Scan0Rm),text="X", activebackground="red4")
Scan0RM.place(width=15, height=40, x=285, y=240)

def Scan1In():
    global Scan1Str
    Main.delete('1.0', END)
    Main.insert(END, Scan1Str)
def Scan1Rm():
    global Scan1Str
    global ScanCt
    global taken1
    Scan1.config(text="")
    Scan1Str = ""
    Main.delete('1.0', END)
    if ScanCt > 1:
        ScanCt = 1
    taken1 = False
Scan1 = Button(root, command=Scan1In)
Scan1.place(width=125, height=40, x=160, y=280)
Scan1X = Button(root, command=(Scan1Rm),text="X", activebackground="red4")
Scan1X.place(width=15, height=40, x=285, y=280)

def Scan2In():
    global Scan2Str
    Main.delete('1.0', END)
    Main.insert(END, Scan2Str)
def Scan2Rm():
    global Scan2Str
    global ScanCt
    global taken2
    Scan2.config(text="")
    Scan2Str = ""
    Main.delete('1.0', END)
    if ScanCt > 2:
        ScanCt = 2
    taken2 = False
Scan2 = Button(root, command=Scan2In)
Scan2.place(width=125, height=40, x=160, y=320)
Scan2RM = Button(root, command=(Scan2Rm),text="X", activebackground="red4")
Scan2RM.place(width=15, height=40, x=285, y=320)

def Scan3In():
    global Scan3Str
    Main.delete('1.0', END)
    Main.insert(END, Scan3Str)
def Scan3Rm():
    global Scan3Str
    global ScanCt
    global taken3
    Scan3.config(text="")
    Scan3Str = ""
    Main.delete('1.0', END)
    if ScanCt > 1:
        ScanCt = 1
    taken3 = False
Scan3 = Button(root, command=Scan3In)
Scan3.place(width=125, height=40, x=160, y=360)
Scan3RM = Button(root, command=(Scan3Rm),text="X", activebackground="red4")
Scan3RM.place(width=15, height=40, x=285, y=360)

def Scan4In():
    global Scan4Str
    Main.delete('1.0', END)
    Main.insert(END, Scan4Str)
def Scan4Rm():
    global Scan4Str
    global ScanCt
    global taken4
    Scan4.config(text="")
    Scan4Str = ""
    Main.delete('1.0', END)
    if ScanCt > 4:
        ScanCt = 4
    taken4 = False
Scan4 = Button(root, command=Scan4In)
Scan4.place(width=125, height=40, x=160, y=400)
Scan4RM = Button(root, command=(Scan4Rm),text="X", activebackground="red4")
Scan4RM.place(width=15, height=40, x=285, y=400)

def Scan5In():
    global Scan5Str
    Main.delete('1.0', END)
    Main.insert(END, Scan5Str)
def Scan5Rm():
    global Scan5Str
    global ScanCt
    global taken5
    Scan5.config(text="")
    Scan5Str = ""
    Main.delete('1.0', END)
    if ScanCt > 5:
        ScanCt = 5
    taken5 = False
    Main.insert(END, Scan5Str)
Scan5 = Button(root, command=Scan5In)
Scan5.place(width=125, height=40, x=160, y=440)
Scan5RM = Button(root, command=(Scan5Rm),text="X", activebackground="red4")
Scan5RM.place(width=15, height=40, x=285, y=440)

def Scan6In():
    global Scan6Str
    Main.delete('1.0', END)
    Main.insert(END, Scan6Str)
def Scan6Rm():
    global Scan6Str
    global ScanCt
    global taken6
    Scan6.config(text="")
    Scan6Str = ""
    Main.delete('1.0', END)
    if ScanCt > 6:
        ScanCt = 6
    taken6 = False
    Main.insert(END, Scan6Str)
Scan6 = Button(root, command=Scan6In)
Scan6.place(width=125, height=40, x=160, y=480)
Scan6RM = Button(root, command=(Scan6Rm),text="X", activebackground="red4")
Scan6RM.place(width=15, height=40, x=285, y=480)

def Scan7In():
    global Scan7Str
    Main.delete('1.0', END)
    Main.insert(END, Scan7Str)
def Scan7Rm():
    global Scan7Str
    global ScanCt
    global taken7
    Scan7.config(text="")
    Scan7Str = ""
    Main.delete('1.0', END)
    if ScanCt > 7:
        ScanCt = 7
    taken7 = False
    Main.insert(END, Scan7Str)
Scan7 = Button(root, command=Scan7In)
Scan7.place(width=125, height=40, x=160, y=520)
Scan7RM = Button(root, command=(Scan7Rm),text="X", activebackground="red4")
Scan7RM.place(width=15, height=40, x=285, y=520)

def Scan8In():
    global Scan8Str
    Main.delete('1.0', END)
    Main.insert(END, Scan8Str)
def Scan8Rm():
    global Scan8Str
    global ScanCt
    global taken8
    Scan1.config(text="")
    Scan8Str = ""
    Main.delete('1.0', END)
    if ScanCt > 8:
        ScanCt = 8
    taken8 = False
    Main.insert(END, Scan8Str)
Scan8 = Button(root, command=Scan8In)
Scan8.place(width=125, height=40, x=160, y=560)
Scan8RM = Button(root, command=(Scan8Rm),text="X", activebackground="red4")
Scan8RM.place(width=15, height=40, x=285, y=560)

ScanCt = 0 
ScanManage = [Scan0Str, Scan1Str, Scan2Str, Scan3Str, Scan4Str, Scan5Str, Scan6Str, Scan7Str, Scan8Str]
def startScan():
    global MainStr
    global ScanCt
    global Scan0Str, Scan1Str, Scan2Str, Scan3Str, Scan4Str, Scan5Str, Scan6Str, Scan7Str, Scan8Str
    global taken0, taken1, taken2, taken3, taken4, taken5, taken6, taken7, taken8
    #get text from text entry
    defports = ports.get("1.0",'end-1c')
    deftarget = target.get("1.0",'end-1c')
    defname = scanName.get("1.0",'end-1c')
    #default for target
    if defports == "":
        defports = "1-1000"
    #confirm ScanCt with Taken
    if ScanCt == 0 and taken0 == True:
        ScanCt += 1
    if ScanCt == 1 and taken1 == True:
        ScanCt += 1
    if ScanCt == 2 and taken2 == True:
        ScanCt += 1
    if ScanCt == 3 and taken3 == True:
        ScanCt += 1
    if ScanCt == 4 and taken4 == True:
        ScanCt += 1
    if ScanCt == 5 and taken5 == True:
        ScanCt += 1
    if ScanCt == 6 and taken6 == True:
        ScanCt += 1
    if ScanCt == 7 and taken7 == True:
        ScanCt += 1
    if ScanCt == 8 and taken8 == True:
        ScanCt += 1
    #check for URL
    try:
        socket.inet_aton(deftarget)
        UrlCheck = False
    except socket.error:
        UrlCheck = TRUE
    #if not url check if ip
    if UrlCheck == False:
        badtarget = False
        checktarget = deftarget
        checktarget = checktarget.replace("..", "X").replace(".", "").replace("/", "")
        try:
            int(checktarget)
        except ValueError:
            badtarget = True
            Main.insert(END, "error: illegal target specifications\n")
    #if url check if valid url
    if UrlCheck == True:
        if "https://" in deftarget:
            deftarget = deftarget[8:]
        if "http://" in deftarget:
            deftarget = deftarget[7:]
        try:
            validators.url(deftarget)
            badtarget = False
            hostName = deftarget
            deftarget = socket.gethostbyname(hostName)
        except ValidationFailure:
            badtarget = True
            Main.delete('1.0', END)
            Main.insert(END, "error: failed to resolve ip from URL\n")
    badports = False
    checkports = defports
    checkports = checkports.replace(",,", "X").replace(",", "").replace("-", "")
    try:
        int(checkports)
        badports = False
    except ValueError:
        badports = True
    if badports == False and badtarget == False:
        TempStr = subprocess.check_output(["armada", deftarget, "-p", defports])
        Main.delete('1.0', END)
        Main.insert(END, TempStr)
        if ScanCt == 0:
            if scanName.get("1.0",'end-1c') == "":
                Scan0.config(text=deftarget)
            else:
                Scan0.config(text=defname)
            Scan0Str = TempStr
            taken0 = True
        if ScanCt == 1:
            if scanName.get("1.0",'end-1c') == "":
                Scan1.config(text=deftarget)
            else:
                Scan1.config(text=defname)
            Scan1Str = TempStr
            taken1 = True
        if ScanCt == 2:
            if scanName.get("1.0",'end-1c') == "":
                Scan2.config(text=deftarget)
            else:
                Scan2.config(text=defname)
            Scan2Str = TempStr
            taken2 = True
        if ScanCt == 3:
            if scanName.get("1.0",'end-1c') == "":
                Scan3.config(text=deftarget)
            else:
                Scan3.config(text=defname)
            Scan3Str = TempStr
            taken3 = True
        if ScanCt == 4:
            if scanName.get("1.0",'end-1c') == "":
                Scan4.config(text=deftarget)
            else:
                Scan4.config(text=defname)
            Scan4Str = TempStr
            taken4 = True
        if ScanCt == 5:
            if scanName.get("1.0",'end-1c') == "":
                Scan5.config(text=deftarget)
            else:
                Scan5.config(text=defname)
            Scan5Str = TempStr
            taken5 = True
        if ScanCt == 6:
            if scanName.get("1.0",'end-1c') == "":
                Scan6.config(text=deftarget)
            else:
                Scan6.config(text=defname)
            Scan6Str = TempStr
            taken6 = True
        if ScanCt == 7:
            if scanName.get("1.0",'end-1c') == "":
                Scan7.config(text=deftarget)
            else:
                Scan7.config(text=defname)
            Scan7Str = TempStr
            taken7 = True
        if ScanCt == 8:
            if scanName.get("1.0",'end-1c') == "":
                Scan8.config(text=deftarget)
            else:
                Scan8.config(text=defname)
            Scan8Str = TempStr
            taken8 = True
        elif badports == True:
            Main.delete('1.0', END)
            Main.insert(END, "error: illegal port specifications\n")
        elif badtarget == True:
            Main.delete('1.0', END)
            Main.insert(END, "error: illegal target specifications\n")
        ScanCt += 1

ScanBtn = Button(root, text="scan", command=startScan)
ScanBtn.place(height=75, width=75, x=725, y=0)

HelpStr = """Eyemada v1.0.0
Eyemada by Melidee <https://github.com/Melidee>

Armada v1.0.2
Armada by d0nutptr <d0nut@resync.gg>

USAGE
Target - the target of the scan
    -accepts URL, IPv4, or CIDR
Ports - sets which ports to scan 
    -accepts a single port, a port range, or multiple ports
Scan Name - what the scan will be listed as
    -defaults to target ip
Scan - starts the port scan
"""
Help = "false"
def ShowHelp():
    global Help
    if Help == False:
        Main.delete('1.0', END)
        Main.insert(END, HelpStr)
        Help = True
    else:
        Main.delete('1.0', END)
        Main.insert(END, MainStr)
        Help = False
HelpBtn = Button(root, text="Toggle\nHelp Text", command=ShowHelp, relief=FLAT, font=("TkDefaultFont",7))
HelpBtn.place(height=50, width=50, x=735, y=120)

root.mainloop()
