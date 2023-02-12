import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://tifr-atas-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "110202":
        {
            "name": "Garv Jhangiani",
            "major": "Computer",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "101201":
        {
            "name": "Prerak Moolchandani",
            "major": "Computer",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "101101":
        {
            "name": "Muskan Hassanandani",
            "major": "EXTC",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)