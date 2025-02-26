import unittest


from sampleflaskapp import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_root(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "This is the root page.")
    
    def test_hello1(self):
        response = self.app.get('/hello1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "hello1")
    
    def test_hello2(self):
        response = self.app.get('/hello2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "hello2")
    
    def test_hello3(self):
        response = self.app.get('/hello3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "hello3")
    
    def test_hello4(self):
        response = self.app.get('/hello4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "hello4")

if __name__ == '__main__':
    unittest.main()

