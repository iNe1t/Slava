import serial

SERIAL_PORT = "/dev/serial0"
running = True

# В сообщении NMEA позиция передается как: 
# DDMM.MMMMM, где DD обозначает градусы, а MM.MMMMM обозначает минуты.
# Однако я хочу преобразовать этот формат в следующий: 
# DD.MMMM. Этот метод преобразует переданную строку в желаемый формат

def formatDegreesMinutes(coordinates, digits):
    
    parts = coordinates.split(".")

    if (len(parts) != 2):
        return coordinates

    if (digits > 3 or digits < 2):
        return coordinates
    
    left = parts[0]
    right = parts[1]
    degrees = str(left[:digits])
    minutes = str(right[:3])

    return degrees + "." + minutes

# Этот метод читает данные из последовательного порта, к которому подключен ключ GPS, 
# и затем анализирует сообщения NMEA, которые он передает. 
# GPS это последовательный порт, который используется для связи с адаптером GPS
def getPositionData(gps):
    data = gps.readline()
    message = data[0:6]
    if (message == "$GPRMC"):
        # GPRMC = Рекомендуемые минимальные конкретные данные GPS / транзит
        # Чтение фиксированных данных GPS является альтернативным подходом, 
        # который также работает
        parts = data.split(",")
        if parts[2] == 'V':
            # V = Предупреждение, скорее всего, спутников нет в поле зрения ...
            print("GPS receiver warning")
        else:
            # Получить данные о местоположении, которые были переданы с сообщением GPRMC. 
            # В этом примере интересуют только долгота и широта. Для других значений можно
            # обратиться к http://aprs.gids.nl/nmea/#rmc
            longitude = formatDegreesMinutes(parts[5], 3)
            latitude = formatDegreesMinutes(parts[3], 2)
            print ("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
    else:
        # Обрабатывать другие сообщения NMEA и неподдерживаемые строки
        pass

print ("Application started!")
gps = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 0.5)

while running:
    try:
        getPositionData(gps)
    except KeyboardInterrupt:
        running = False
        gps.close()
        print ("Application closed!")
    except:
        # Вы должны сделать некоторую обработку ошибок здесь ...
        print ("Application error!")