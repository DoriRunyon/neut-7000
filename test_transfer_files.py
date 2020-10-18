from os.path import isdir, isfile, join
from os import listdir, mkdir
import shutil
import unittest

from transfer_files import NoFilesToMove, transfer_files
from utils import add_file_to_directory

class TestFileTransfer(unittest.TestCase):

    def setUp(self):
        if isdir("/home/pi/Desktop/"):
            print("is raspberry")
            self.a_path = "/home/pi/Desktop/neut/test_folder_a/"
            self.b_path = "/home/pi/Desktop/neut/test_folder_b/"
        elif isdir("/tmp"):
            print("is mac")
            self.a_path = "/tmp/test_folder_a/"
            self.b_path = "/tmp/test_folder_b/"
        mkdir(self.a_path)
        mkdir(self.b_path)
        self.directory_a = {"name": "a_directory", "path": self.a_path}
        self.directory_b = {"name": "b_directory", "path": self.b_path}

    def tearDown(self):
        shutil.rmtree(self.a_path)
        shutil.rmtree(self.b_path)
    
    def test_happy_path(self):
        add_file_to_directory(self.directory_a["path"])
        transfer_files(self.directory_a["path"], self.directory_b["path"])
        
        a_files = [f for f in listdir(self.a_path) if isfile(join(self.a_path, f))]
        b_files = [f for f in listdir(self.b_path) if isfile(join(self.b_path, f))]
        
        self.assertEqual(len(a_files), 0)
        self.assertEqual(len(b_files), 1)
        
    def test_directory_a_empty(self):
        with self.assertRaises(NoFilesToMove):
            transfer_files(self.directory_a["path"], self.directory_b["path"])

    def test_directory_b_not_empty(self):
        add_file_to_directory(self.directory_a["path"])
        add_file_to_directory(self.directory_a["path"])
        transfer_files(self.directory_a["path"], self.directory_b["path"])
        
        a_files = [f for f in listdir(self.a_path) if isfile(join(self.a_path, f))]
        b_files = [f for f in listdir(self.b_path) if isfile(join(self.b_path, f))]
        
        self.assertEqual(len(a_files), 0)
        self.assertEqual(len(b_files), 1)

if __name__ == "__main__":
    unittest.main()
