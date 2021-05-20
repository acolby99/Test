import os
import pathlib

os.system('cls')

def GetState():
    state = input("Please enter the name of a state: ")
    return state;

def FormalState(state):
    if len(state) < 8:
        just = state.ljust(8, "*")
        return just
    else:
        return state;

print ("1. Get information and display to screen")
print ("2. Call user created functions")
print ("3. Write list of files to file")
print ("4. Read specified file")

answer = input ("Please enter the number of the menu item you want to perform: ")

if answer == "1":
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uName = os.environ['UserName']
    classFirst = input ("Enter your first class: ")
    classSecond = input ("Enter your second class: ")
    print ("Logged on as", uName, "at", companyName, "in department:", programName)
    print ("My first class is", classFirst, "and my second class is", classSecond)

elif answer == "2":
    state = GetState()
    newState = FormalState(state)
    print ("State was", state, "and is now", newState)

elif answer == "3":
    fileName = input ("Enter a file name to create: ")
    fList = []
    dList = []
    for p in pathlib.Path('.').iterdir():
        if p.is_file():
            fList.append(p)
        else:
            dList.append(p)

    with open(fileName, "w") as myFileWrite:
        myFileWrite.write("These are my files:\n")
        for f in fList:
            myFileWrite.write(f.name)
            myFileWrite.write("\n")

elif answer == "4":
    fRead = input ("Enter a filename to read: ")

    with open(fRead, "r+") as myFileRead:
        print(myFileRead.read())

else:
    print ("Have a nice day")
