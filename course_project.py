import speech_recognition as sr 
import os
import sys
import webbrowser 
import time
import datetime

day = time.strftime('%d')
if  time.strftime('%B') == 'January':
    month = 'Январь'
def talk(words):
    print(words)  # output at console
    os.system('say -v Milena ' + words)

talk('Привет, я Милена. Ваш голосовой помощник. Я еще не всему научилась и медленно думаю. Пожалуйста, проявите терпение.')
talk('Чем я могу помочь?')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:   # открываем запись в файл
        print('Говорите')
        r.pause_threshold = 1  # пауза в 1 секунду чтобы чел сказал
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)  # takes input from source
    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print('Вы сказали: ' + task)
    except sr.UnknownValueError:
        talk('Извините не понимаю. Повторите команду.')
        task = command()
    return task 

def makeSomeNoise(task):
    # открывает сайт рэу
    if 'открой сайт рэу' in task:
        talk('открываю веб-сайт российского экономического университета')
        url = 'https://www.rea.ru/'
        webbrowser.open(url)
        time.sleep(10)
        talk('Что-то еще?')
    # о погоде
    elif 'какая сегодня погода' in task:
        talk('да какая разница? все равно ты кроме метро и универа ничего не видишь')
        url = 'https://www.gismeteo.ru/'
        webbrowser.open(url)
        time.sleep(10)
        talk('Что-то еще?')
    # о преподавателе
    elif 'кто такой черноусов' in task:
        talk('Черноусов Андрей Анатольевич - кандидат экономических наук, преподаватель РЭУ')
        talk('Перенаправляю на сайт с подробной информацией')
        url = 'https://www.rea.ru/ru/org/employees/Pages/Chernousov-Andrejj-Anatolevich.aspx'
        webbrowser.open(url) 
        time.sleep(10)
        talk('Что-то еще?')
    # дата
    elif 'какое сегодня число' in task:
        talk('Сегодняшнее число   ' + str(day) + '   месяц   ' + str(month))
        time.sleep(10)
        talk('Что-то еще?')
    # завершение работы
    elif 'стоп' in task: 
        talk('Завершаю работу. До свидания')
        sys.exit()
    return task
while True:
    makeSomeNoise(command())








