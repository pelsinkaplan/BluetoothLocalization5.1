import math


def triangulation(c, angleValues):
    A = angleValues[0]
    B = angleValues[1]
    C = 180 - angleValues[0] - angleValues[1]
    b = c * math.sin(B) / math.sin(C)
    h = math.sin(A) * b
    m = math.sqrt(math.pow(b, 2) - math.pow(h, 2))
    return m, h


def angleOfArrival(angleValues):
    x1 = 0
    x2 = 460
    c = x2 - x1
    m, h = triangulation(c, angleValues)
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
    x2 = 580
    y2 = 0
    x3 = 0
    y3 = 460
    x, y = trilateration(x1, x2, x3, y1, y2, y3, rssiValues)
    return x, y

# def resultOfAlgorithms(self, rssiPos, anglePos):
#     positonX = input("Enter x coordiante: ")
#     positonY = input("Enter y coordiante: ")
#     counter = 0
#     if (rssiPos.get_positionX - positonX > anglePos.get_positionX - positonX):
#         counter += 1
#     elif (rssiPos.get_positionX - positonX < anglePos.get_positionX - positonX):
#         counter -= 1
#     if (rssiPos.get_positionY - positonY > anglePos.get_positionY - positonY):
#         counter += 1
#     elif (rssiPos.get_positionY - positonY < anglePos.get_positionY - positonY):
#         counter -= 1
#     if (counter > 0):
#         return "Rssi Based Algorithm is better."
#     elif (counter < 0):
#         return "Angle of Arrival Algorithm is better."
#     else:
#         return "Both algorithms give results with the same accuracy."
