from config import session, names_black_list
from random import randint


def send_msg_chat(_id, text):
    random_id = randint(0, 1000000000)
    session.method("messages.send", {"peer_id": _id, "message": text, "random_id": random_id})


def is_black_listed(msg):
    for name in names_black_list:
        if name in msg.lower():
            return 1
    return 0


def kick_from_chat(_id, chat_id):
    session.method("messages.removeChatUser", {"chat_id": chat_id, "user_id": _id})


def delete_msg(msg_id, peer_id):
    session.method("messages.delete", {"cmids": msg_id, "peer_id": peer_id, "delete_for_all": 1})
