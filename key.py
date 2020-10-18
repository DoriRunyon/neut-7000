from enum import Enum

class Key:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.file_path = ""
        self.led_color = ""
        self.led_on = False
        self.hold_value = ""
        self.hold_seconds = 0
    
class StorageKey(Key):
    
    def __init__(self, **kwds):
        self.audio = ""
        super().__init__(**kwds)
    
    def is_empty(self):
        pass
    
    def transfer_files_in(self):
        pass
    
    def transfer_files_out(self):
        pass

    def play_audio(self):
        pass
