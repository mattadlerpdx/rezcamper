
from Controller import *

def main():
    campsiteDataFile = "campsitesToMonitor.json"
    controller = Controller(campsiteDataFile) 
    controller.consoleMenu()




if __name__ == "__main__":
    main()
