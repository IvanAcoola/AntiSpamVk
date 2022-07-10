import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


names_black_list = ['fataliti', 'fatality', 'warface', 'варфейс']

token = ''
session = vk_api.VkApi(token = token)
longpool = VkBotLongPoll(session, )

token_2 = ''
# токен юзера (для получения имен сообществ)
session2 = vk_api.VkApi(token = token_2)

