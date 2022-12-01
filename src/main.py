
from Controller import *

def main():
    campsiteDataFile = "src/campsitesToMonitor.json"
    controller = Controller(campsiteDataFile) 
    controller.consoleMenu()




if __name__ == "__main__":
    main()
