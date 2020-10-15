import uuid

from argparse import ArgumentTypeError
from os import listdir, mkdir,remove
from os.path import isfile, join
from shutil import copyfile, move, rmtree
from sys import argv

NEUT = {"path": "/home/pi/Desktop/neut/test_folder/", "name": "Neut 7000"}
HARD_DRIVE = {"path": "/media/pi/backup/caperbunny/", "name": "External Hard Drive"}

class NoFilesToMove(Exception):
    
    def __init__(self):
        pass

def neut_file_transfer(to_neut=False):
    to_neut = string_to_bool(to_neut)
    if to_neut:
        transfer_files(HARD_DRIVE, NEUT)
    else:
        transfer_files(NEUT, HARD_DRIVE)

def transfer_files(a, b):
    """Transfer all files in directory 'a' to directory 'b'."""

    a_path = a["path"]
    b_path = b["path"]

    a_files = [f for f in listdir(a_path) if isfile(join(a_path, f))]
    b_files = [f for f in listdir(b_path) if isfile(join(b_path, f))]

    if (len(a_files) < 1):
        print("No files to move")
        raise NoFilesToMove()
    
    if (len(b_files) > 0):
        print("Removing directory {} files".format(b["name"]))
        print("b path one", b_path)
        rmtree(b_path) # fix this for actual script
        mkdir(b_path)
        print(b_files)
        print("b path two", b_path)

    for file in a_files:
        print("Transfering files to ", b["name"], "!")
        file_path = "{}{}".format(a_path, file)
        move(file_path, b_path)

def string_to_bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    neut_file_transfer(argv[1])
