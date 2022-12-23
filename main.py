import fileNamer


class Choice:
    def __init__(self):
        path = input("enter the path of the document: \n")
        fileNamer.FileNamerClass(path)


if __name__ == '__main__':
    choice_made = Choice()
