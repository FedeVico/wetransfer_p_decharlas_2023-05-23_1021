from django.test import TestCase
from django.test import Client
from .models import Password, User, Message

from http.cookies import SimpleCookie



class GetTests (TestCase):


    def test_nocookie(self):
        c = Client()
        response = c.get('/decharlas/')
        self.assertEqual(response.status_code, 302)


    def test_login(self):
        c = Client()
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)


    def test_root(self):
        c = Client()
        Password.objects.create(valid_pwd='pass_1')
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)

        response = c.post('/decharlas/login', {'login_pwd': 'pass_1'})
        self.assertEqual(response.status_code, 302)

        self.client.cookies = SimpleCookie({'userID': User.objects.filter(id=1)})
        response = c.get('/decharlas/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<title>DeCharlas</title>', content)


    def test_config(self):
        c = Client()
        Password.objects.create(valid_pwd='pass_1')
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)

        response = c.post('/decharlas/login', {'login_pwd': 'pass_1'})
        self.assertEqual(response.status_code, 302)

        self.client.cookies = SimpleCookie({'userID': User.objects.filter(id=1)})
        response = c.get('/decharlas/config')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<label for="config_name">Name</label>', content)


    def test_help(self):
        c = Client()
        Password.objects.create(valid_pwd='pass_1')
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)

        response = c.post('/decharlas/login', {'login_pwd': 'pass_1'})
        self.assertEqual(response.status_code, 302)

        self.client.cookies = SimpleCookie({'userID': User.objects.filter(id=1)})
        response = c.get('/decharlas/help')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        # self.assertIn('<label for="config_name">Name</label>', content)


    def test_room(self):
        c = Client()
        Password.objects.create(valid_pwd='pass_1')
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)

        response = c.post('/decharlas/login', {'login_pwd': 'pass_1'})
        self.assertEqual(response.status_code, 302)

        self.client.cookies = SimpleCookie({'userID': User.objects.filter(id=1)})

        response = c.post('/decharlas/', {'roomname': 'test_room'})
        self.assertEqual(response.status_code, 302)

        response = c.get('/decharlas/test_room')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<label for="content">Enter Message</label>', content)


    def test_dynroom(self):
        c = Client()
        Password.objects.create(valid_pwd='pass_1')
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)

        response = c.post('/decharlas/login', {'login_pwd': 'pass_1'})
        self.assertEqual(response.status_code, 302)

        self.client.cookies = SimpleCookie({'userID': User.objects.filter(id=1)})

        response = c.post('/decharlas/', {'roomname': 'test_room'})
        self.assertEqual(response.status_code, 302)

        response = c.get('/decharlas/dyn/test_room')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>DYNAMIC ROOM</p>', content)


    def test_logout(self):
        c = Client()
        Password.objects.create(valid_pwd='pass_1')
        response = c.get('/decharlas/login')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<p>LOGIN DECHARLAS</p>', content)

        response = c.post('/decharlas/login', {'login_pwd': 'pass_1'})
        self.assertEqual(response.status_code, 302)

        self.client.cookies = SimpleCookie({'userID': User.objects.filter(id=1)})

        response = c.get('/decharlas/logout')
        self.assertEqual(response.status_code, 302)



