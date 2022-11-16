from FileInterface import *
from Controller import *
from JsonModel import *

def main():
    campsiteDataFile = "data.json"
    toFile = InterfaceToFile()
    model = JsonModel(campsiteDataFile)
    controller = Controller(toFile)

    mockPost = controller.getPostAsInput()
    validPost = controller.validatePost(mockPost)
    controller.updateEmail(validPost)


if __name__ == "__main__":
    main()
