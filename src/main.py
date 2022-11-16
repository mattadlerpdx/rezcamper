from FileInterface import *
from Controller import *
from JsonModel import *

def main():
    campsiteDataFile = "src/campsitesToMonitor.json"
    #toFile = InterfaceToFile()
    model = JsonModel(campsiteDataFile)
    controller = Controller(model)

    mockPost = controller.getPostAsInput()
    controller.updateEmail(mockPost)


if __name__ == "__main__":
    main()
