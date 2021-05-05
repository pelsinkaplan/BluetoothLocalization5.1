import PositioningAlgorithms
import math
import datetime
import DatabaseManager


def readFileRSSI():
    file = open('C://Users//pelsi//OneDrive//Masaüstü//BLE_RSSI.txt', 'r')
    count = 0
    lines = []
    device = 0
    while True:
        line = file.readline()
        if not line:
            break
        if count != 0:
            rssi = int(line.rstrip('\n'))
            lines.append(rssi)
        else:
            device = int(line.rstrip('\n'))
        count += 1
    file.close()
    return lines, device


def readFileANGLE():
    file = open('C://Users//pelsi//OneDrive//Masaüstü//BLE_ANGLE.txt', 'r')
    count = 0
    lines = []
    device = 0
    while True:
        line = file.readline()
        if not line:
            break
        if count != 0:
            angle = math.radians(int(line.rstrip('\n')))
            lines.append(angle)
        else:
            device = int(line.rstrip('\n'))
        count += 1
        print("Line{}: {}".format(count, line.strip()))
    file.close()
    return lines, device


if __name__ == '__main__':
    # DatabaseManager.takeInfoFromDatabase()
    start = datetime.datetime.now()
    while True:
        end = datetime.datetime.now()
        if (end - start).total_seconds() > 3:
            rssiValues, rssiDevice = readFileRSSI()
            angleValues, angleDevice = readFileANGLE()
            x, y = PositioningAlgorithms.rssiBased(rssiValues)
            m, h = PositioningAlgorithms.angleOfArrival(angleValues)
            print(x)
            print(y)
            print(m)
            print(h)
            time = start.strftime("%H:%M:%S")
            DatabaseManager.addDeviceToDatabase(1, m, h, time)
            DatabaseManager.addDeviceToDatabase(2, x, y, time)
            start = datetime.datetime.now()
            DatabaseManager.takeInfoFromDatabase()
