from unittest import TestCase, main
from api import Controller
from hashlib import sha256

API_URL = "https://quest.maxus.space"


class APITests(TestCase):
    def test_user_data(self):
        user_hash = sha256(b"Hello, World!").hexdigest()
        controller = Controller(API_URL)
        resp = controller.user_data(user_hash)
        print(resp)
        self.assertEqual(user_hash, resp.card_hash)

    def test_register(self):
        user_hash = sha256(b"Hello, World!").hexdigest()
        controller = Controller(API_URL)
        resp = controller.register(user_hash)
        # none, because already registered
        self.assertIsNone(resp)

    def test_avatar(self):
        user_hash = sha256(b"Hello, World!").hexdigest()
        controller = Controller(API_URL)
        user = controller.user_data(user_hash)
        controller.avatar(user.id, "avatar.png")


if __name__ == "__main__":
    main()
