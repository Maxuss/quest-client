from mimetypes import init
import requests;
from dataclasses import dataclass
from uuid import UUID

@dataclass
class RegStageUser:
    """Все данные одного пользователя до полного процесса регистрации"""
    card_hash: str
    id: UUID

    def __init__(self, card_hash: str, id: UUID):
        self.card_hash = card_hash
        self.id = id

@dataclass
class UserData:
    """Все данные одного пользователя"""
    card_hash: str
    id: UUID
    username: str
    telegram_chat_id: int

    def __init__(self, card_hash: str, id: UUID, username: str, telegram_chat_id: int):
        self.card_hash = card_hash
        self.id = id
        self.username = username
        self.telegram_chat_id = telegram_chat_id

class Controller():
    def __init__(self, url: str):
        """
        Создает новый контроллер для API, который
        позволет получать данные игроков

        @param url: URL текущей сессии API. На данный момент не является постоянным, потому что сервер работает на ngrok
        """
        self.url = url
        self.default_headers = {
            'User-Agent': 'Quest-Client/0.1.0',
            'ngrok-skip-browser-warning': 'letmein'
        }
    
    def user_data(self, user_hash: str) -> UserData:
        """
        Пытается получить доступ к данным пользователя.

        Возвращает [None] если пользователь не регистрировался.

        @param user_hash: SHA256 хэш данных пользователя
        """
        resp = requests.get(f"{self.url}/user/get/{user_hash}", headers=self.default_headers).json()
        if not resp['success']:
            return None
        return UserData(resp['card_hash'], UUID(resp['id']), resp['username'], resp['telegram_chat_id'])

    def register(self, user_hash: str) -> RegStageUser:
        """
        Начинает процесс регистрации для пользователя с предоставленным хэшем 

        @param user_hash: SHA256 хэш данных карты пользователя
        """
        resp = requests.post(f"{self.url}/user/register", json={'card_hash': user_hash}, headers=self.default_headers).json()
        if not resp['success']:
            return None
        return RegStageUser(resp['card_hash'], UUID(resp['id']))

