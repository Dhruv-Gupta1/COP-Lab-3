# import requests

# ENDPOINT = "http://127.0.0.1:8034/"

# def test_base():
#     response = requests.get(ENDPOINT + "")
#     assert response.status_code == 200
#     print("hello")
    
# # python3 -m pytest -v -s .\unittest.py::test_base

import requests
import unittest

class TestAPI(unittest.TestCase):
    ENDPOINT = "http://127.0.0.1:8034/"
    def test_base(self):
        response = requests.get(self.ENDPOINT + "")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<!-- This is base.html -->",response.content)
        print("Test 1 completed")

    def test_tags(self):
        response = requests.get(self.ENDPOINT + "/tags/TagId")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<!-- This is tags.html -->",response.content)
        print("Test 2 completed")

    def test_logout(self):
        response = requests.get(self.ENDPOINT + "/logout")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<!-- This is base.html -->",response.content)
        print("Test 3 completed")

    def test_questions(self):
        response = requests.get(self.ENDPOINT + "/questions/QuesScore")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<!-- This is questions.html -->",response.content)
        print("Test 4 completed")

    def test_users(self):
        response = requests.get(self.ENDPOINT + "/users/UserId")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<!-- This is users.html -->",response.content)
        print("Test 5 completed")    

    def test_login(self):
        response = requests.get(self.ENDPOINT + "/login")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<!-- This is login.html -->",response.content)
        print("Test 6 completed")    
    
            
if __name__ == '__main__':
    tester = TestAPI()
    tester.test_base()
    tester.test_tags()
    tester.test_logout()
    tester.test_questions()
    tester.test_users()
    tester.test_login()
    
# python3 test.py
# python -m coverage run -m unittest
# python -m coverage report 