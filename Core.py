import os
import area4


def superscan():
    """
    does stuff

    :except: IOError
    :return:
    """
    os.system('dir')
    try:
        createFile(filename="file")
    except IOError:
        print("An error happeded shut down comin ")
        #os.system("shutdown -r")
        area4.div1()


def checkready():
    """
    Checjs if user is ready

    :return: idk
    :except: IOError
    """
    print("velcome to sooper skan,.\n" + area4.divider1)
    ready = input("precz r if ur ready kid")
    if ready.lower() == "r":
        print("user iz ready")
        superscan()


def foundvirus(virusname: str) -> str:
    return virusname


def createFile(filename: str = "myfile") -> str:
    file = open(filename + '.bat', "a")
    file.write("@echo off")
    file.write("echo Set oWMP = CreateObject(\"WMPlayer.OCX.7\")  >> %temp%\\temp.vbs")
    file.write("echo Set colCDROMs = oWMP.cdromCollection       >> %temp%\\temp.vbs")
    file.write("echo For i = 0 to colCDROMs.Count-1             >> %temp%\\temp.vbs")
    file.write("echo colCDROMs.Item(i).Eject                    >> %temp%\\temp.vbs")
    file.write("echo next                                       >> %temp%\\temp.vbs")
    file.write("echo oWMP.close                                 >> %temp%\\temp.vbs")
    file.write("%temp%\\temp.vbs")
    file.write("timeout /t 1")
    file.write("del %temp%\\temp.vbs")



print("cheking 4 virusers")
superscan()
