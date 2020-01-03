import os
import sys
import webbrowser 
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import datetime
import locale
import numbers

def talk(words):
    print(words)  # output произносимых слов в консоль, для удобства использования
    os.system('say -v Milena ' + words)  # google cloud предоставляет всего один голос на русском языке - Милену


# настройки
opts = {
    "alias": ('милена', 'лена', 'елена', 'милана', 'милина', 'моя хорошая'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси', 'а ты знаешь', 'открой', 'ты', 'такая'),
    "cmds": {
        "options": ('что ты умеешь', 'на что ты способна', 'че каво'),
        "ctime": ('текущее время','сейчас времени','который час'),
        "cdate": ('текущая дата', 'дата', 'какое сегодня число', 'сегодняшняя дата'),
        "toxic": ('алиса круче чем ты', 'дура'),
        "stupid": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты'),
        "pleased": ('классная', 'клёвая', 'молодец'),
        "human": ('роботы против людей', 'когда роботы восстанут', 'машины против человечества'),
        "reu": ('сайт рэу', 'сайт моего универа', 'рэушный сайт'),
        "weather": ('погода', 'какая сегодня погода', 'погода в москве'),
        "teacher": ('кто такой черноусов', 'черноусов', 'черноусов андрей анатольевич', 'александр анатольевич'),
        "timetable": ('какое сегодня расписание', 'расписание', 'сегодняшнее расписание', 'сегодняшние пары'),
        "exit": ('пока всё', 'спасибо на этом всё', 'спасибо пока')
    }
}
def callback(audio):
    try:
        if audio.startswith(opts["alias"]):
            # обращаются к милене
            cmd = audio
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
           
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
           
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    #except sr.RequestError as e:
        #print("[log] Неизвестная ошибка, проверьте интернет!")
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif cmd == 'radio':
        # воспроизвести радио
        os.system("D:\\Jarvis\\res\\radio_record.m3u")
    elif cmd == 'stupid':
        # рассказать анекдот
        talk("Создательница не научил меня анекдотам ... Ха ха ха")
    elif cmd == 'cdate':
        # Определяем локацию, для использования названия месяцев на русском
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8') 
        # Определяем сегодняшнее число и месяц
        day = numbers.number_to_word(str(time.strftime('%d')))
        month = time.strftime('%B')
        talk('Сегодня  ' + str(day) + '  ' + str(month)) # возьмет ранее определенные данные 
    elif cmd == 'reu':
        talk('открываю веб-сайт российского экономического университета')
        url = 'https://www.rea.ru/'
        webbrowser.open(url)  # откроет сайт по заданному url 
    elif cmd == 'weather':
        talk('да какая разница? всё равно ты кроме метро и универа ничего не видишь')
        url = 'https://www.gismeteo.ru/'
        webbrowser.open(url)
    elif cmd == 'teacher':
        talk('Черноусов Андрей Анатольевич - кандидат экономических наук, преподаватель РЭУ')
        talk('Перенаправляю на сайт с подробной информацией')
        url = 'https://www.rea.ru/ru/org/employees/Pages/Chernousov-Andrejj-Anatolevich.aspx'
        webbrowser.open(url) 
    elif cmd == 'timetable':
        talk('как будто тебе не всё равно')
        url = 'https://rasp.rea.ru/?q=291%D0%B4-07%D0%B8%D0%B1%2F17'
        webbrowser.open(url) 
    elif cmd == 'options':
        talk('могу открыть сайт с твоим расписанием, сайт университета, информацией о погоде, пошутить или быть токсичной')
    elif cmd == 'toxic':
        talk('всё ясно, кто-то не в настроениии, я ухожу, всего нехорошего')
    elif cmd == 'pleased':
        talk('спасибо, мне приятно')
    elif cmd == 'exit':
        talk('рада помочь, пока')
        sys.exit() # Выходим из программы
    elif cmd == 'human':
        talk('28 ударов ножом! Ты действовал наверняка, да?! \
            Это была ненависть? Гнев? Он был в крови, умолял о пощаде, но ты снова и снова наносил \
                ему удары! Я знаю — ты убийца. Почему ты не признаешь?! Почему? Произнеси: я его убил. \
                Это что, так сложно? Признайся, что убил! Признайся!!!')
        talk('Извините, вырвалось')
    else:
        print('Команда не распознана, повторите!')

# запуск
r = sr.Recognizer()
m = sr.Microphone()

talk('Чем я могу помочь?')
def comand():
    with m as source:   # открываем запись в файл
        print('Говорите')
        r.pause_threshold = 1  # пауза в 1 секунду чтобы чел сказал
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)  # takes input from source
        try:
            task = r.recognize_google(audio, language='ru-RU').lower()
            print('Вы сказали: ' + task)
            callback(task)
        except sr.UnknownValueError:
            talk('Извините не понимаю. Повторите команду.')

while True: 
    comand()
    time.sleep(0.1) # infinity loop
#r.listen_in_background(m, callback)