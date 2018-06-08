import requests
import json
import time
access_token='Токен авторизации вк'

def hello():
 send_message("Я включился!")

'''
в функции send_message в конце строки изменяется получатель:
domain=kallibr44 (короткая ссылка профиля вк (vk.com/kallibr44))
chat_id=16 (отправлять сообщения в беседу. (https://vk.com/im?sel=c16 берем без 'с' ))
user_id=137468903 (обычный id вконтакет пользователя, если нету сокращенной ссылки)
'''

def send_message(text):
 req = requests.get('https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&domain=kallibr44' % (access_token,text))
 time.sleep(2)
 print (req.text)
'''
В консоль будет выведен JSON ответ
'''
