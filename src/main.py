
from Controller import *

def main():
    campsiteDataFile = "src/campsitesToMonitor.json"
    webKey = "WFiiKkgW1oaFCB2oLzUCYhmdu9cEQCPgPnkClMmd"
    controller = Controller(campsiteDataFile, webKey) 
    controller.consoleMenu()


if __name__ == "__main__":
    main()
