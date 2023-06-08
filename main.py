import customtkinter
import os
import platform
import tkinter

from pathlib import Path


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x400")
app.title("Detection Tool")

def scan_function():
    if platform.system() == "Linux":
        userServicePath = str(Path.home()) + "/.config/systemd/user/systemd-utility.service"
        if os.path.isfile(userServicePath) == True:
            userService = True
            frame.itemconfig(userServiceText, text="Detected User Service: YES", fill='red')
        else:
            userService = False
            frame.itemconfig(userServiceText, text="Detected User Service: NO", fill='green')

        systemServicePath = "/etc/systemd/system/systemd-utility.service"
        if os.path.isfile(systemServicePath) == True:
            systemService = True
            frame.itemconfig(systemServiceText, text="Detected System Service: YES", fill='red')
        else:
            systemService = False
            frame.itemconfig(systemServiceText, text="Detected System Service: NO", fill='green')

        libJarPath = str(Path.home()) + "/.config/.data/lib.jar"
        if os.path.isfile(libJarPath) == True:
            libJar = True
            frame.itemconfig(libJarText, text="Detected lib.jar: YES", fill='red')
        else:
            libJar = False
            frame.itemconfig(libJarText, text="Detected lib.jar: NO", fill='green')

        if libJar == False and systemService == False and userService == False:
            frame.itemconfig(summaryText, text="Summmry: Malware was not detected on your machine", fill='green')
        else:
           frame.itemconfig(summaryText, text="Possible Malware traces were detected on your machine", fill='red')
    
    elif platform.system() == "Windows":
        edgePath = str(Path.home()) + "/AppData/Local/Microsoft Edge/"
        if os.path.isfile(edgePath + ".ref") == True:
            edge = True
            frame.itemconfig(microsoftEdgeText, text="Detected Edge folder: YES", fill='red')
        elif os.path.isfile(edgePath + "client.jar") == True:
            edge = True
            frame.itemconfig(microsoftEdgeText, text="Detected Edge folder: YES", fill='red')
        elif os.path.isfile(edgePath + "lib.dll") == True:
            edge = True
            frame.itemconfig(microsoftEdgeText, text="Detected Edge folder: YES", fill='red')
        elif os.path.isfile(edgePath + "libWebGL64.jar") == True:
            edge = True
            frame.itemconfig(microsoftEdgeText, text="Detected Edge folder: YES", fill='red')
        elif os.path.isfile(edgePath + "run.bat") == True:
            edge = True
            frame.itemconfig(microsoftEdgeText, text="Detected Edge folder: YES", fill='red')
        else:
            edge = False
            frame.itemconfig(microsoftEdgeText, text="Detected Edge folder: NO", fill='green')

        startupPath = str(Path.home()) + "/AppData/Romaing/Microsoft/Windows/Start Menu/Programs/Startup"
        if os.path.isfile(startupPath + "run.bat") == True:
            startup = True
            frame.itemconfig(startupText, text="Detected Startup file: YES", fill='red')
        else:
            startup = False
            frame.itemconfig(startupText, text="Detected Startup file: NO", fill='green')

        if startup == False and edge == False:
            frame.itemconfig(summaryText, text="Summmry: Malware was not detected on your machine", fill='green')
        else:
           frame.itemconfig(summaryText, text="Possible Malware traces were detected on your machine", fill='red')
    

button = customtkinter.CTkButton(master=app, text="Scan", command=scan_function)
button.place(anchor="center", relx = .5, rely = .055)

frame = customtkinter.CTkCanvas(master=app, width=680, height=350, bg="#2b2b2b", highlightthickness=0)
frame.place(anchor="center", relx = .5, rely = .55)

summaryText = frame.create_text(20, 50, anchor="w", text="Summmry: Not Run", fill="white", font=('15'))

if platform.system() == "Windows":
    microsoftEdgeText = frame.create_text(20, 80, anchor="w", text="Detected Edge folder: Not Run", fill="white", font=('15'))
    startupText = frame.create_text(20, 110, anchor="w", text="Detected Startup file: Not Run", fill="white", font=('15'))

elif platform.system() == "Linux":
    userServiceText = frame.create_text(20, 80, anchor="w", text="Detected User Service: Not Run", fill="white", font=('15'))
    systemServiceText = frame.create_text(20, 110, anchor="w", text="Detected System Service: Not Run", fill="white", font=('15'))
    libJarText = frame.create_text(20, 140, anchor="w", text="Detected lib.jar: Not Run", fill="white", font=('15'))

else:
    pass

app.mainloop()
