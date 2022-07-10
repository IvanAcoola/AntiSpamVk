import config
from vk_api.bot_longpoll import VkBotEventType
import methods


def main():
    while True:
        try:
            for event in config.longpool.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.message['attachments']:
                        if event.message['attachments'][0]['type'] == 'wall':
                            from_group_post = abs(event.message['attachments'][0]['wall']['to_id'])
                            group_name = config.session2.method("groups.getById", {"group_id": from_group_post})[0]['name']
                            if methods.is_black_listed(group_name):
                                target_id = event.message['from_id']
                                msg_id = event.message['conversation_message_id']
                                peer_id = event.message['peer_id']
                                methods.delete_msg(msg_id, peer_id)
                                methods.send_msg_chat(peer_id, f'@id{target_id}(Нахал) не уступил мне место'
                                                               f', да еще и чушь рассылает!\n\n'
                                                               f'Получай палкой!')
                                methods.kick_from_chat(target_id, event.chat_id)
        except:
            pass


if __name__ == '__main__':
    main()
