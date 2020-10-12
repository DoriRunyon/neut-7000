from keys import build_key_dict, KeyName

def program():
    
    LAST_KEY_PRESS = None
    POWER_ON = False
    key_dict = build_key_dict()
    
    while POWER_ON is False:
        # wait some seconds
        print("please enter a key id")
        key_press = input()
        print("key id: {}".format(key_press))
        if int(key_press) == key_dict[KeyName.power].key_id:
            print("powering on!")
            POWER_ON = True
        
        # program()
        
    
    # power on = run_setup()
    
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

def setup_storage_keys():
    pass

# ideas
## lights for errors
## lights for low battery
## would be cool to have full key pad animation during audio - at the end blink 3x
# to tell user where the files are for that audio