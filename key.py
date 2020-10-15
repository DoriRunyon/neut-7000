from enum import Enum

class Key:
    
    def __init__(self, name, key_value):
        self.name = name
        self.key_value = key_value
        self.led_color = ""
        self.led_on = False
        self.hold_value = ""
        self.hold_seconds = 0
    
class StorageKey(Key):
    
    def __init__(self, **kwds):
        self.file_path = ""
        self.audio = ""
        super().__init__(**kwds)
    
    def is_empty(self):
        pass
    
    def transfer_files_in(self):
        pass
    
    def transfer_files_out(self):
        pass

    def play_audio(self):
        # 5 second audio play
        pass
    
    def blink_led(self):
        # 3 second blink
        pass

class KeyName(Enum):
    power = "power"
    neut = "neut"
    op_1 = "op-1"
# on start - create the keys
# need 9 storage keys
# neut, OP-1, POWER are not storage keys
# def build_key_dict():
#     key_dict = {}
#     
#     for i in range(3, 11):
#         name = "storage_{}".format(i)
#         key = StorageKey(key_id=i, name=name)
#         key_dict[name] = key
#         
#     power = Key(key_id=0, name=KeyName.power)
#     key_dict[KeyName.power] = power
#     
#     neut = Key(key_id=1, name=KeyName.neut)
#     key_dict[KeyName.neut] = neut
#     
#     op_1 = Key(key_id=2, name=KeyName.op_1)
#     key_dict[KeyName.op_1] = op_1
#     return key_dict
    

# actions: save files to neut, save files to OP-1, power on/off, play audio file at key