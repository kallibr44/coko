import requests
import time
import os, sys

access_token = ''


def hello():
    send_message("Я включился!")


def send_message(text):
    req = requests.get(
        'https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&chat_id=1' % (access_token, text))
    req1 = requests.get(
        'https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&user_id=168331752' % (
        access_token, text))
    re2 = requests.get('https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&user_id=189931403' % (
    access_token, text))
    re3 = requests.get('https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&user_id=441239018' % (
        access_token, text))
    re4 = requests.get('https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&user_id=142703152' % (
        access_token, text))
    re5 = requests.get('https://api.vk.com/method/messages.send?v=5.52&access_token=%s&message=%s&user_id=67610974' % (
        access_token, text))
    time.sleep(2)
    print ("Сообщение отправлено в беседу успешно!" + req.text)
    print ("Сообщение Александра Серова отправлено успешно!" + req1.text)
    print ("Сообщение Вова Солодилов отправлено успешно!" + re2.text)
    print ("Сообщение Darya Evgenyevna отправлено успешно!" + re3.text)
    print ("Сообщение Павел Куприенко отправлено успешно!" + re4.text)
    print ("Сообщение Оксана Повалева отправлено успешно!" + re5.text)


def timer():
 i = 3600
 while i > 0:
   print("Time remaining before next check: " + str(i) + "sec.")
   os.system("clear")
   i = i-1
   time.sleep(1)
