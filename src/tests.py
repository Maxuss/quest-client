from unittest import TestCase, main
from api import Controller
from hashlib import sha256

class APITests(TestCase):
    def test_user_data(self):
        controller = Controller("https://9ad0-2a00-f940-2-4-2-00-4047.eu.ngrok.io")
        resp = controller.user_data(sha256(b"Hello, World!").hexdigest())
        self.assertIsNone(resp)

if __name__ == "__main__":
    main()