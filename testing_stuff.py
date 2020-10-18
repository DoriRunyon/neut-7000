import os


PATH_TO_DEVICE = "/tmp/test_op_2/"

def testing_stuffs():

    if not os.path.isdir(PATH_TO_DEVICE):
        os.mkdir(PATH_TO_DEVICE)

    print("is directory there?")
    if not os.path.isdir(PATH_TO_DEVICE):
        print("no")
    else:
        print("yes")

    file = open("{}/testing_file.txt".format(PATH_TO_DEVICE), "w+")
    file.close()


testing_stuffs()