import config, time

from datetime import datetime

day = int(datetime.now().day)
month = int(datetime.now().month)
year = int(datetime.now().year)
hour = int(datetime.now().hour)

def update_variables():
    day = int(datetime.now().day); month = int(datetime.now().month)
    year = int(datetime.now().year); hour = int(datetime.now().hour)
    return True

def send_log():
    f = open('logs.txt', 'a')
    f.write(f'Dia {day}/{month}/{year}: ' + str(config.retweeted_today) + ' tweets retweetados\n')
    f.close
    update_variables()
    config.retweeted_today = 0
    print(f'{datetime.now()} | Logs do dia {day} registradas com sucesso!')
    return True

def logs():
    print('Sistema de logs iniciado')
    if hour == 0:
        time.sleep(4000)
    while True:
        if int(datetime.now().hour) == 0:
            print(f'{datetime.now()} | Registrando logs do dia {day}...')
            send_log()
            time.sleep(4000)
        time.sleep(15)
