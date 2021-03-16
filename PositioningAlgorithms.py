import Position
import BLEDevice
import math


# rssi = []
# rssiValues = []
# angle = []
# angleValues = []
# estimatedPosition = []
# lastPosition = []

# def __init__(self, rssi, rssiValues, angle, angleValues, estimatedPosition, lastPosition):
#     self.rssi = rssi
#     self.rssiValues = rssiValues
#     self.angle = angle
#     self.angleValues = angleValues
#     self.estimatedPosition = estimatedPosition
#     self.lastPosition = lastPosition


def triangulation(z, angleValues):
    angle = 180 - angleValues[0] - angleValues[1]
    a = z * math.sin(angleValues[0]) / math.sin(angle)
    h = math.sin(angleValues[1] / a)
    m = h / math.cos(angleValues[1])
    m = z - m
    return m, h


def triangulation2(z, angleValues):
    # angle = 180 - angleValues[0] - angleValues[1]
    # k = (z*cotB)/(cotB+cotA)
    k = (z * (math.cos(angleValues[1]) / math.sin(angleValues[1]))) / (
            (math.cos(angleValues[1]) / math.sin(angleValues[1])) + (
            math.cos(angleValues[0]) / math.sin(angleValues[0])))
    m = z - k
    h = k / (math.cos(angleValues[1]) / math.sin(angleValues[1]))
    return m, h


def angleOfArrival(angleValues):
    x1 = 0
    y1 = 0
    x2 = 10
    y2 = 10
    z = math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)
    z = math.sqrt(z)
    m, h = triangulation(z, angleValues)
    return m, h


def trilateration(x1, x2, x3, y1, y2, y3, rssiValues):
    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = math.pow(rssiValues[0], 2) - math.pow(rssiValues[1], 2) - math.pow(x1, 2) + math.pow(x2, 2) - math.pow(y1,
                                                                                                               2) + math.pow(
        y2, 2)
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = math.pow(rssiValues[1], 2) - math.pow(rssiValues[2], 2) - math.pow(x2, 2) + math.pow(x3, 2) - math.pow(y2,
                                                                                                               2) + math.pow(
        y3, 2)
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)
    return x, y


def rssiBased(rssiValues):
    x1 = 0
    y1 = 0
    x2 = 10
    y2 = 10
    x3 = 0
    y3 = 10
    x, y = trilateration(x1, x2, x3, y1, y2, y3, rssiValues)
    return x, y


def resultOfAlgorithms(self, rssiPos, anglePos):
    positonX = input("Enter x coordiante: ")
    positonY = input("Enter x coordiante: ")
    counter = 0
    if (rssiPos.get_positionX - positonX > anglePos.get_positionX - positonX):
        counter += 1
    elif (rssiPos.get_positionX - positonX < anglePos.get_positionX - positonX):
        counter -= 1
    if (rssiPos.get_positionY - positonY > anglePos.get_positionY - positonY):
        counter += 1
    elif (rssiPos.get_positionY - positonY < anglePos.get_positionY - positonY):
        counter -= 1
    if (counter > 0):
        return "Rssi Based Algorithm is better."
    elif (counter < 0):
        return "Angle of Arrival Algorithm is better."
    else:
        return "Both algorithms give results with the same accuracy."


if __name__ == '__main__':
    # device bilgisini çekip, rssi valuelarını rssiValues listine atıcaz
    # sonra rssi listine device ve rssiValues listini atıcaz

    # device = BLEDevice(1)
    rssi1 = (int)(input("Enter first rssi value: "))
    rssi2 = (int)(input("Enter second rssi value: "))
    rssi3 = (int)(input("Enter third rssi value: "))
    rssiValues = [rssi1, rssi2, rssi3]

    # device bilgisini çekip, angle valuelarını angleValues listine atıcaz
    # sonra angle listine device ve angleValues listini atıcaz

    angle1 = (int)(input("Enter first angle value: "))
    angle2 = (int)(input("Enter second angle value: "))
    angleValues = [angle1, angle2]

    x, y = rssiBased(rssiValues)
    m, h = angleOfArrival(angleValues)
    print(x)
    print(y)
    print(m)
    print(h)
