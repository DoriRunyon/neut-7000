import os

from key import Key, StorageKey
from enum import Enum


# run all tests: python3 -m unittest discover -s neut -p '*test_'

# PATH_TO_STORAGE = "/home/pi/Desktop/neut_files/"
# PATH_TO_DEVICE = "/media/pi/backup/caperbunny"

PATH_TO_STORAGE = "/Users/dorirunyon/Desktop/neut_files/"
PATH_TO_DEVICE = "/Users/dorirunyon/Desktop/test_op_1/"

def program():
    neut = Program()

    neut_key = neut.create_key(name="neut", value="1", is_storage=False)
    op_1_key = neut.create_key(name="op-1", value="3", is_storage=False)
    storage_1 = neut.create_key(name="storage-1", value="a")
    storage_2 = neut.create_key(name="storage-1", value="b")
    storage_3 = neut.create_key(name="storage-1", value="c")
    
    if not os.path.isdir(PATH_TO_STORAGE):
        os.mkdir(PATH_TO_STORAGE)
        neut.create_storage()
    else:
        neut.load_storage()
    
    while neut.state == ProgramState.ready_for_device:
        if os.path.isdir(PATH_TO_DEVICE):
            neut.state = ProgramState.ready_for_commands
            
    key_press = input()
    pass

class ProgramState(Enum):
    ready_for_device = "ready_for_device"
    ready_for_commands = "ready_for_commands"
    
class Program:
    
    def __init__(self):
        self.state = ProgramState.ready_for_device
        self.last_input = None
        self.keys = {}
        self.available_storage = 0
        self.allowed_commands = {}

    def create_storage(self):
        """Create storage from scratch"""
        neut_keys = self.keys.values()
        
        for key in neut_keys:
            if isinstance(key, StorageKey):
                file_path = PATH_TO_STORAGE + key.name
                os.mkdir(file_path)
                key.file_path = file_path
            
    def load_storage(self, neut):
        for key in self.keys.values():
            if isinstance(key, StorageKey):
                file_path = PATH_TO_STORAGE + key.name
                assert os.path.isdir(file_path) is True
                key.file_path = file_path
    
    def create_allowed_command(self, *args):
        pass

#     def is_valid_command(self, key_press):
#         
#         if key_press in self.allowed_commands[self.state]:
#             return True
#         
#         return False
        
    def create_key(self, name, value, is_storage=True):
        if is_storage:
            self.keys[name] = StorageKey(name=name, value=value)
            self.available_storage += 1
            return self.keys[name]
        
        self.keys[name] = Key(name=name, value=value)
        return self.keys[name]

