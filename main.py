# Journal
import os # Imported Operating System

# Definitions
def file(fileEntry):
    try:
        fileOpen = open(fileEntry, "r")
        return fileOpen
    except FileNotFoundError:
        print("File doesn't exist.")
        return None

# Code
directoryChanger = input("Dir ... ")
os.chdir(directoryChanger)
while True:
    viewerEntry = input("Would you like to view a previous journal? (Yes/No) ... ")
    if viewerEntry == "Yes" or viewerEntry == "yes":
        fileEntry = input("File: ")
        fFunction = file(fileEntry)
        print(f"Text: {fFunction.read()}")
        fFunction.close()
    elif viewerEntry == "No" or viewerEntry == "no":
        while True:
            nameFile = input("Write new journal name: ")
            fileWrite = input("Text: ")
            confirm = input("Create File? ")
            
            try:
                if confirm == "yes" or confirm == "Yes":
                    fileProperties = open(nameFile, "w")
                    write = fileProperties.write(fileWrite)
                    fileProperties.close()
                    break
                elif confirm == "no" or confirm == "No":
                    continue
            except Exception:
                print("Error occured, please try again.")
            
        print("File Created Successfully.")
        quit()
    else:
        print("Command Error.")
        continue
