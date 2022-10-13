from unittest import TestCase, main
from api import Controller
from hashlib import sha256

CURRENT_NGROK_URL = "https://9ad0-2a00-f940-2-4-2-00-4047.eu.ngrok.io"

class APITests(TestCase):
    def test_user_data(self):
        user_hash = sha256(b"Hello, World!").hexdigest()
        controller = Controller(CURRENT_NGROK_URL)
        resp = controller.user_data(user_hash)
        self.assertEqual(user_hash, resp.card_hash)

    def test_register(self):
        user_hash = sha256(b"Hello, World!").hexdigest()
        controller = Controller(CURRENT_NGROK_URL)
        resp = controller.register(user_hash)
        # none, because already registered
        self.assertIsNone(resp)

if __name__ == "__main__":
    main()