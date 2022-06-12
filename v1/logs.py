import config, time

from datetime import datetime

day = int(datetime.now().day)
month = int(datetime.now().month)
year = int(datetime.now().year)

def send_log():
    f = open('logs.txt', 'a')
    f.write(f'Dia {day}/{month}/{year}: ' + str(config.retweeted_today))
    f.close
    config.retweeted_today = 0
    print(f'{datetime.now()} | Logs do dia {day} registradas com sucesso!')
    return True

def logs():
    print('Sistema de logs iniciado')
    while True:
        if int(datetime.now().hour) == 0:
            print(f'{datetime.now()} | Registrando logs do dia {day}...')
            send_log()
            time.sleep(3600)
        time.sleep(15)
