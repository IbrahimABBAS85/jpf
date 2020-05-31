import unittest
import pytest
from pathlib import Path

from structure.setting import Setting
from structure.setting_element import SettingElement
from jpf import FileManager

class Test_File_Manager_Pickle(unittest.TestCase):
    
    pytest.fullPath = str((Path(__file__).parent.parent / 'test_files' / 'setting_test.set').absolute())
     
    def test_save_file_using_pickle_argument(self):
        setting = self.getSetting()
        self.assertEqual(FileManager.save(setting, pytest.fullPath, 'pickle'), True, "File is not Saved")       

    def test_get_file_using_pickle_argument(self):
        setting = self.getSetting()        
        self.assertIsNotNone(FileManager.get(pytest.fullPath, 'pickle'), "File is not Saved")
    
    
    
    def getSetting(self):
        return Setting(SettingElement('setting_element_1', 20, True), True)

def suite():
    suite = unittest.TestSuite()  
    suite.addTest(Test_File_Manager_Pickle('test_save_file_using_pickle_argument'))
    suite.addTest(Test_File_Manager_Pickle('test_get_file_using_pickle_argument'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())