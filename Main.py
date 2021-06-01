import PositioningAlgorithms
import math
import datetime
import DatabaseManager


def readDatabaseRSSI():
    i = 0
    allRssiValues = DatabaseManager.takeRSSIFromDatabase()  # burdan gelen değer [rssi1,rssi2,rss3,deviceId] contentine sahip bi list (bütün deviceların boş olanlar dahil)
    devicesRssi = []
    deviceId = []
    while i <= 4:  # 5 device varmış gibi düşündüm şimdilik
        if allRssiValues[i][0] != None:  # boş olanları ignore edip dolu onları alıyoruz
            rssiVals = allRssiValues[i]  # sırayla her listi tek tek alıyorum
            rssiVals = rssiVals[:3]  # her bir device için bir list oluşturup içine atıyorum sırayla
            devicesRssi.append(
                rssiVals)  # oluşturuduğum rssi listlerini de teker teker bir listte toplutıorum aşağıda düzenleme yaptıum
            id = allRssiValues[i][3]
            deviceId.append(id)
        i += 1

    return devicesRssi, deviceId


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
            allRssiValues, allRssiDevice = readDatabaseRSSI()
            # angleValues, angleDevice = readFileANGLE()
            i = 0
            while True:
                if i >= len(allRssiDevice):
                    break
                else:
                    x, y = PositioningAlgorithms.rssiBased(allRssiValues[i])
                    time = start.strftime("%H:%M:%S")
                    DatabaseManager.addDeviceToDatabase(allRssiDevice[i], x, y, time)
                    print(x)
                    print(y)
                i += 1
            # m, h = PositioningAlgorithms.angleOfArrival(angleValues)
            # print(m)
            # print(h)
            time = start.strftime("%H:%M:%S")
            # DatabaseManager.addDeviceToDatabase(1, m, h, time)
            # DatabaseManager.addDeviceToDatabase(2, x, y, time)
            start = datetime.datetime.now()
            DatabaseManager.takeInfoFromDatabase()
