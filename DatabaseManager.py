import pyrebase

firebaseConfig = {'apiKey': "AIzaSyBn_P1TGDIP7afg8Wi1kTJDI8OgtlLBpT4",
                  'authDomain': "ble-localization-84b97.firebaseapp.com",
                  'projectId': "ble-localization-84b97",
                  'databaseURL': "https://ble-localization-84b97-default-rtdb.europe-west1.firebasedatabase.app/",
                  'storageBucket': "ble-localization-84b97.appspot.com",
                  'messagingSenderId': "1011608324550",
                  'appId': "1:1011608324550:web:61387086a89926eea68ac7",
                  'measurementId': "G-PHXPPQ5G2W"}

# initialize the app
firebase = pyrebase.initialize_app(firebaseConfig)

# for realtime database
db = firebase.database()


def addDeviceToDatabase(id, posX, posY, time):
    data = {'posX': posX, 'posY': posY}
    db.child("Devices").child(id).child(time).set(data)


def takeInfoFromDatabase():
    f = open("C://Users//pelsi//OneDrive//Masaüstü//LOCATIONS.txt", "w+")
    devices = db.child("Devices").get()
    numOfDatas = len(db.child('Devices').child("1").get().val())
    f.write(str(numOfDatas))
    f.write("\n")
    for device in devices.each():
        data = str(device.val())
        counter = 0
        for ch in data:
            f.write(ch)
            if ch == '}':
                counter += 1
            else:
                counter = 0
            if counter == 2:
                f.write("\n")
    f.close()
