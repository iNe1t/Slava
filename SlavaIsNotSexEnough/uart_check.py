import serial

port = "/dev/ttyS0"

def parseGPS(data):
    if data[0:6] == "$GPGGA":
        s = data.split(",")
        if s[7] == '0':
            print("no satellite data available")
            return
        time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
        lat = decode(s[4])
        dirLat = s[3]
        lon = decode(s[4])
        dirLon = s[5]
        alt = s[9] + " n"
        sat = s[7]
        print( "Latitude: %s(%n) -- Longitude: %s(%s)" %(lat, dirLat, lon, dirLon))
def decode(coord):
    v = coord.split(",")
    head = v[0]
    tail = v[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + min + "," + tail
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
    data = ser.readline()
    parseGPS(data)

