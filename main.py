import customtkinter
import os
import tkinter

from pathlib import Path


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x400")
app.title("Detection Tool")

def scan_function():
    userServicePath = str(Path.home()) + "/.config/systemd/user/systemd-utility.service"
    if os.path.isfile(userServicePath) == True:
        userService = True
        frame.itemconfig(userServiceText, text="Detected User Service: YES")
    else:
        userService = False
        frame.itemconfig(userServiceText, text="Detected User Service: NO")

    systemServicePath = "/etc/systemd/system/systemd-utility.service"
    if os.path.isfile(systemServicePath) == True:
        systemService = True
        frame.itemconfig(systemServiceText, text="Detected System Service: YES")
    else:
        systemService = False
        frame.itemconfig(systemServiceText, text="Detected System Service: NO")

    libJarPath = str(Path.home()) + "/.config/.data/lib.jar"
    if os.path.isfile(libJarPath) == True:
        libJar = True
        frame.itemconfig(libJarText, text="Detected lib.jar: YES")
    else:
        libJar = False
        frame.itemconfig(libJarText, text="Detected lib.jar: NO")


    if libJar == False and systemService == False and userService == False:
        frame.itemconfig(summaryText, text="Summmry: Malware was not detected on your machine")
    else:
       frame.itemconfig(summaryText, text="Possible Malware traces were detected on your machine")

button = customtkinter.CTkButton(master=app, text="Scan", command=scan_function)
button.place(anchor="center", relx = .5, rely = .055)

frame = customtkinter.CTkCanvas(master=app, width=680, height=350, bg="#2b2b2b", highlightthickness=0)
frame.place(anchor="center", relx = .5, rely = .55)

summaryText = frame.create_text(20, 50, anchor="w", text="Summmry: Not Run", fill="white", font=('15'))
userServiceText = frame.create_text(20, 80, anchor="w", text="Detected User Service: Not Run", fill="white", font=('15'))
systemServiceText = frame.create_text(20, 110, anchor="w", text="Detected System Service: Not Run", fill="white", font=('15'))
libJarText = frame.create_text(20, 140, anchor="w", text="Detected lib.jar: Not Run", fill="white", font=('15'))

app.mainloop()
