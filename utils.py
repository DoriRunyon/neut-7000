

def add_file_to_directory(path):
    print("adding file to directory!")
    file = open("{}testing_file.txt".format(path), "w+")
    file.close()