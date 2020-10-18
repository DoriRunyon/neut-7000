import os
import shutil

from key import Key, StorageKey
from enum import Enum
from transfer_files import transfer_files
from utils import add_file_to_directory


# run all tests: python3 -m unittest discover -s neut -p '*test_'

# raspberry pi paths
# PATH_TO_STORAGE = "/home/pi/Desktop/neut_files"
# PATH_TO_DEVICE = "/media/pi/backup/caperbunny"

# mac paths
# PATH_TO_STORAGE = "/Users/dorirunyon/Desktop/neut/test_folders/neut_files/"
# PATH_TO_DEVICE = "/Users/dorirunyon/Desktop/neut/test_folders/test_op_1/"

PATH_TO_STORAGE = "/tmp/neut_files/"
PATH_TO_DEVICE = "/tmp/test_op_1/"

def program_setup():

    shutil.rmtree(PATH_TO_DEVICE)
    shutil.rmtree(PATH_TO_STORAGE)
    print("initializing!")
    neut = Program()

    # neut_key = neut.create_key(name="neut", value="1", is_storage=False)
    op_1_key = neut.create_key(name="op-1", value="3", is_storage=False)
    
    storage_1 = neut.create_key(name="storage-1", value="a")
    storage_2 = neut.create_key(name="storage-2", value="b")
    storage_3 = neut.create_key(name="storage-3", value="c")

    storage_keys = [storage_1, storage_2, storage_3]

    for storage_key in storage_keys:
        neut.create_allowed_command(op_1_key.value, storage_key.value)
        neut.create_allowed_command(storage_key.value, op_1_key.value)
    
    if not os.path.isdir(PATH_TO_STORAGE):
        os.mkdir(PATH_TO_STORAGE)
        neut.create_storage()
    else:
        neut.load_storage()
    neut.state = ProgramState.ready_for_device
    return neut

def listen_for_device(neut):
    while neut.state == ProgramState.ready_for_device:
        # for testing:
        if not os.path.isdir(PATH_TO_DEVICE):
            os.mkdir(PATH_TO_DEVICE)
        add_file_to_directory(PATH_TO_DEVICE)
        # end for testing
        if os.path.isdir(PATH_TO_DEVICE):
            op_1_key = neut.keys["3"]
            op_1_key.file_path = PATH_TO_DEVICE
            print("ready for commands!")
            neut.state = ProgramState.ready_for_commands
            return neut

def program(neut=None):

    if not neut:
        neut = program_setup()
    
    if neut.state == ProgramState.ready_for_device:
        neut = listen_for_device(neut)
            
    elif neut.state == ProgramState.ready_for_commands:
        key_value = input() 
        if neut.is_valid_command(key_value):
            # need to update this to add and remove available storage 
            neut.last_input = key_value
            second_key_value = input()
            if neut.is_valid_command(second_key_value):
                source_file_path = neut.keys[key_value].file_path
                target_file_path = neut.keys[second_key_value].file_path
                transfer_files(source_file_path, target_file_path)
                neut.last_input = None
    else:
        raise Exception("Unknown program state")
    program(neut)


class ProgramState(Enum):
    ready_for_device = "ready_for_device"
    ready_for_commands = "ready_for_commands"


class Program:
    
    def __init__(self):
        self.state = None
        self.last_input = None
        self.keys = {}
        self.key_name_to_value_mapping = {}
        self.available_storage = 0
        self.allowed_commands = {}

    def create_storage(self):
        neut_keys = self.keys.values()
        for key in neut_keys:
            if isinstance(key, StorageKey):
                file_path = PATH_TO_STORAGE + key.name + "/"
                os.mkdir(file_path)
                key.file_path = file_path
            
    def load_storage(self):
        for key in self.keys.values():
            if isinstance(key, StorageKey):
                file_path = PATH_TO_STORAGE + key.name
                assert os.path.isdir(file_path) is True
                key.file_path = file_path
    
    def create_allowed_command(self, first_key, second_key):
        allowed_second_keys = self.allowed_commands.get(first_key, set())
        allowed_second_keys.add(second_key)
        self.allowed_commands[first_key] = allowed_second_keys

    def is_valid_command(self, key_value):
        print(self.allowed_commands)
        if not self.last_input:
            if key_value in self.allowed_commands:
                return True
        else:
            if key_value in self.allowed_commands[self.last_input]:
                return True
        
        return False
        
    def create_key(self, name, value, is_storage=True):
        if is_storage:
            self.keys[value] = StorageKey(name=name, value=value)
            self.available_storage += 1
            return self.keys[value]
        
        self.keys[value] = Key(name=name, value=value)
        self.key_name_to_value_mapping[name] = value
        return self.keys[value]



