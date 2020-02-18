import requests
import vk_api

vk_session = vk_api.VkApi(token='594f2b057f3522a78490fb6c3b30906765e42d79d36bc4b03d19a59ce0c18194cecb55f51bec37ba1fd2b')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'q' or event.text == 'Привет': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='q'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='q'
		)
                import datetime

                vk.messages.send(
                    user_id=event.user_id,
                    message='Московское время: ' + str(now.strftime("%H:%M"))
                )