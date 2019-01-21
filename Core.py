import os
import area4


def superscan():
    """
    does stuff

    :exception: IOError
    :return:
    """
    os.system('dir')
    try:
        createFile()
    except IOError:
        print("An error happeded shut down comin ")
        area4.div1()
    print("o god viruz found it is prob ZEuS or MEMZ VIRUS")
    print("ur not going to last long because we found the " + foundvirus(virusname = "ZEuS"), "virus!!!")


def checkready():
    """
    Checks if user is ready

    :return: idk
    :except: IOError
    """
    print("velcome to sooper skan,.\n" + area4.divider1)
    ready = input("precz r if ur ready kid")
    if ready.lower() == "r":
        superscan()


def foundvirus(virusname: str) -> str:
    return virusname


def createFile():
    file = open('%temp%\\temp.vbs', "a")
    file.write("Set oWMP = CreateObject(\"WMPlayer.OCX.7\") \n")
    file.write("Set colCDROMs = oWMP.cdromCollection \n")
    file.write("For i = 0 to colCDROMs.Count-1  \n")
    file.write("colCDROMs.Item(i).Eject \n")
    file.write("next\n")
    file.write("oWMP.close \n")
    os.system("%temp%\\temp.vbs")

