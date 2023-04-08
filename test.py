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
        print("Test 1 completed")
    def test_tags(self):
        response = requests.get(self.ENDPOINT + "/tags/TagId")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"<h1>Tags</h1>",response.content)
        self.assertIn(b" <!-- This is tags page -->",response.content)
       
        #self.assertIn(response.data,b'<html>')
        print("Test 2 completed")
        #print(response.json)    #<bound method Response.json of <Response [200]>>
        #print(response.text)    # whole html
        #print(response.content)
        #print(response.headers)
        
            
if __name__ == '__main__':
    tester = TestAPI()
    tester.test_base()
    tester.test_tags()
    
    
# python3 test.py
# python -m coverage run -m unittest
# python -m coverage report 