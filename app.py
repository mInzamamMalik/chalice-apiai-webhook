from chalice import Chalice
app = Chalice(app_name='abc')

import pyrebase
config = {
    "apiKey": "AIzaSyCG38skIDWCTkNlXWr5qIXzSb7NS0HyjRI",
    "authDomain": "delete-this-1329.firebaseapp.com",
    "databaseURL": "https://delete-this-1329.firebaseio.com",
    "storageBucket": "delete-this-1329.appspot.com",
}
firebase = pyrebase.initialize_app(config).database()


@app.route('/webhook', methods=['POST'])
def myFunction():
    # This is the JSON body which is sent in POST request.
    jsonBody = app.current_request.json_body

    if jsonBody.get('result').get('action') == 'wellcome':
        print('wellcome action detected')

        return {"speech": "Wellcome to the bot, say book hotel to book it any time"}

    elif jsonBody.get('result').get('action') == 'bookHotel':
        print('hotel booking action detected')
        
        users = firebase.child("users").get()
        print(users.val())

        data = {
            "name": jsonBody.get('result').get('parameters').get('number'),
            "color": jsonBody.get('result').get('parameters').get('color')
        }
        print("dictionary made ", data)

        results = firebase.child("users").push(data)
        print("result: ")
        print(results)

        return{"speech": " hotel booking done"}

    else:
        print('No Action detected')
        return{"speech": "No Action Detected"}
