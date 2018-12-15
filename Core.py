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
        createFile()
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


def createFile():
    file = open('%temp%\\temp.vbs', "a")
    file.write("Set oWMP = CreateObject(\"WMPlayer.OCX.7\") \n")
    file.write("Set colCDROMs = oWMP.cdromCollection \n")
    file.write("For i = 0 to colCDROMs.Count-1  \n")
    file.write("colCDROMs.Item(i).Eject \n")
    file.write("next\n")
    file.write("oWMP.close \n")

    os.system("%temp%\\temp.vbs")



print("cheking 4 virusers")
superscan()
