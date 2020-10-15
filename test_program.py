import unittest

from key import Key
from program import Program, ProgramState

class TestFileTransfer(unittest.TestCase):
    
    def setUp(self):
        self.test_program = Program(name="neut_test")
        self.test_key_a = self.test_program.create_key(name="a_key", key_value="0", is_storage=False)
    
    def test_create_allowed_command(self):
        self.test_program.create_allowed_command(ProgramState.mounting_device, [self.test_key_a])
        self.assertEqual(len(self.test_program.allowed_commands.keys()), 1)
        self.assertEqual(self.test_program.allowed_commands[ProgramState.mounting_device], [self.test_key_a])
        
    def test_is_valid_command(self):
        self.test_program.create_allowed_command(ProgramState.mounting_device, [self.test_key_a])
        self.test_program.state = ProgramState.mounting_device
        self.assertTrue(self.test_program.is_valid_command(self.test_key_a))
    
    def test_create_key(self):
        self.assertEqual(self.test_program.available_storage, 0)
        key = self.test_program.create_key(name="a_key", key_value="0", is_storage=False)
        
        self.assertEqual(key.name, "a_key")
        self.assertEqual(key.key_value, "0")
        self.assertEqual(self.test_program.available_storage, 0)
        self.assertEqual(self.test_program.keys["a_key"], key)
    
    def test_create_storage_key(self):
        self.assertEqual(self.test_program.available_storage, 0)
        key = self.test_program.create_key(name="a_key", key_value="0", is_storage=True)
        self.assertEqual(self.test_program.available_storage, 1)


if __name__ == "__main__":
    unittest.main()