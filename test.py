import unittest
from app import User

class TestUser(unittest.loader):

    def setUp(self):
        """
        method to run before each test case
        """
        self.new_user = User()

    def test_init(self):
        """
        test if the object is initialized properly
        """ 
        self.assertEqual(self.new_user.username)

        self.assertEqual(self.new_user.password)

        self.assertEqual(self.new_user.email)   

    def test_save_user(self):
        """
        test if the user object is saved into the user list
        """

        self.new_user.save_user()
    







if __name__ == '__main__':
    unittest.main()