 # !/bin/bash python3 

import tkinter as tk
import os 
gui = tk.Tk()
gui.geometry("200x200")
##----labels----buttons---others---##
def poweroffs() :
	os.system("poweroff")
def suspends():
	os.system("sudo systemctl suspend")
def reboots():
	os.system("reboot")
def hibs():
	os.system("sudo systemctl hibernate")


poweroff=tk.Button(gui,text='Shutdown',command=poweroffs)
reboot=tk.Button(gui,text="Restart",command=reboots)
suspend=tk.Button(gui,text="Sleep",command=suspends)
hib=tk.Button(gui,text="Safe Sleep",command=hibs)
poweroff.grid(row=0,column=0,columnspan=2)
reboot.grid(row=0,column=2,columnspan=2)
suspend.grid(row=1,column=0,columnspan=2)
hib.grid(row=1,column=2,columnspan=2)


#---mainloop

gui.mainloop()
