import os


# renaming files uses to rename() function
class FileNamerClass:
    def __init__(self, path):
        path = "/home/mark/" + path
        print(os.listdir(path))
        self.file_extension = input("what is the file extension: \n")
        self.new_name = input("what is the name to rename to: \n")
        test = True
        while test:
            type_name = int(input("how many files to change: \n 1) all \n 2) specific \n"))
            if type_name == 1:
                self.all_file_renamed(path)
                test = False
            elif type_name == 2:
                test = False
                self.specific_file_renamed(path)
            else:
                print("error occurred")

    def all_file_renamed(self, path):
        i = 0
        for file_name in os.listdir(path):
            new_name = self.new_name + f"{str(i)}." + self.file_extension
            new_name_source = path + new_name
            old_name_source = path + file_name
            os.rename(old_name_source, new_name_source)
            i = i + 1
        print("finished")

    def specific_file_renamed(self, path):
        find_name = input("enter the unique character in the filename: ")
        i = 0
        for files in os.listdir(path):
            if find_name in files:
                file_name = self.new_name + f"{str(i)}." + self.file_extension
                old_file = path + files
                new_file = path + file_name
                os.rename(old_file, new_file)
                i = i + 1
            else:
                print("done")
