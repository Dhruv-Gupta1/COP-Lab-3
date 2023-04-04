import unittest
from flask import url_for, request
from app import create_app, db
from app.models import User

class LoginTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        # Create a test user
        self.user = User(username='test_user', email='test_user@example.com')
        self.user.set_password('password')
        db.session.add(self.user)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_login(self):
        # Send a POST request to the login endpoint with valid credentials
        response = self.client.post(url_for('auth.login'), data={
            'username': 'test_user',
            'password': 'password'
        })
        
        # Check that the response is successful and redirects to the homepage
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, url_for('main.index', _external=True))
        
        # Check that the user is logged in
        with self.client:
            self.client.get(url_for('main.index'))
            self.assertTrue(current_user.is_authenticated)
        
        # Send a POST request to the login endpoint with invalid credentials
        response = self.client.post(url_for('auth.login'), data={
            'username': 'test_user',
            'password': 'wrong_password'
        })
        
        # Check that the response is unsuccessful and displays an error message
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)
