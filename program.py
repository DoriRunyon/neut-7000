import os

from key import KeyName, Key, StorageKey
from enum import Enum


# run all tests: python3 -m unittest discover -s neut -p '*test_'

PATH_TO_STORAGE = "/home/pi/Desktop/neut_files/"

def program():
    neut = Program()
    
    power_key = neut.create_key(name="power", key_value="0", is_storage=False)
    neut_key = neut.create_key(name="neut", key_value="1", is_storage=False)
    op_1_key = neut.create_key(name="op-1", key_value="2", is_storage=False)
    storage_1 = neut.create_key(name="storage-1", key_value="3")
    
    # neut.create_allowed_command(ProgramState.power_off, [power_key.key_value])
    
    print("Available storage: ", neut.available_storage)
    if not os.path.isdir(PATH_TO_STORAGE):
        os.mkdir(PATH_TO_STORAGE)
        create_storage(neut)
    else:
        load_storage(neut)
    
    
    while neut.state == ProgramState.power_off:
        key_press = input()
        # if neut.is_valid_command(key_press):
        if key_press == 0:
            print("powering on!")
            neut.state = ProgramState.power_on
            
    key_press = input()
    
    if key_press == "xyz":
        print("powering off")
        os.popen("sudo poweroff")
    # if key press is power off and "x" seconds passes,
    # key value is "sudo poweroff + enter"


    # Run setup:
        # Turn on raspberry pi and mount OP
        # set up keys - switch lights on for keys where needed (all keys - blinking lights during setup)
        # set up file paths & audio based on SD card contents
    
    # actions after power on:
        # Neut + storage key = save from OP to neut*, erase from OP
        # OP + storage key = save from neut to OP*, erase from neut (turn off light)
        # hold down storage key for 3 seconds = play audio held in key
        
        # *blinking light while saving
        
        # power off / power on = reset, do this if you're unclear what state you're in
        # (all keys - blinking lights during shut down)
        
        # Neut + OP = "last key" goes from neut to OP (visa versa)
        # no "last key" + storage key quick press = no change to state, no action
        
        # power off = unmount OP and shutdown raspberry pi
        # (all keys - blinking lights during shut down)
    
    pass

def power_on():
    pass

def power_off():
    pass

def create_storage(neut):
    """Create storage from scratch"""
    neut_keys = neut.keys.values()
    
    for key in neut_keys:
        if isinstance(key, StorageKey):
            file_path = PATH_TO_STORAGE + key.name
            os.mkdir(file_path)
            key.file_path = file_path
            print("STORAGE CREATED!!", key.file_path)
            
def load_storage(neut):
    neut_keys = neut.keys.values()
    
    for key in neut_keys:
        if isinstance(key, StorageKey):
            file_path = PATH_TO_STORAGE + key.name
            assert os.path.isdir(file_path) is True
            key.file_path = file_path
            print("FILE PATH LOADED!!", key.file_path)
    

class ProgramState(Enum): # maybe these aren't necessary
    power_on = "power_on"
    power_off = "power_off"
    ready_for_commands = "ready_for_commands"
    files_incoming = "files_incoming"
    files_outgoing = "files_outgoing"
    
class Program:
    
    def __init__(self, name=""):
        self.name = name
        self.state = ProgramState.power_off
        self.last_key_press = None
        self.keys = {}
        self.available_storage = 0
        self.allowed_commands = {}
        
    def create_allowed_command(self, args*):
        pass

#     def is_valid_command(self, key_press):
#         
#         if key_press in self.allowed_commands[self.state]:
#             return True
#         
#         return False
        
    def create_key(self, name, key_value, is_storage=True):
        
        if is_storage:
            self.keys[name] = StorageKey(name=name, key_value=key_value)
            self.available_storage += 1
            return self.keys[name]
        
        self.keys[name] = Key(name=name, key_value=key_value)
        return self.keys[name]
    


# Oct 13 to do
# write tests for functions created !! (create a separate test file too)
        
            
# ideas
## lights for errors
## lights for low battery
## would be cool to have full key pad animation during audio - at the end blink 3x
# to tell user where the files are for that audio
