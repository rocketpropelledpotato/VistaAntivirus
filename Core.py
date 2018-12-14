import os
def superscan():
    os.system('dir')

def checkready():
    print("velcome to sooper skan,.")
    ready = input("precz r if ur ready kid")
    if (ready.lower() == "r"):
        print("user iz ready")
        superscan()

def foundvirus(virusname: str) -> str:
    return virusname
print("cheking 4 virusers")
superscan()