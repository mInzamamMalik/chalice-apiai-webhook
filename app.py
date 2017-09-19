from chalice import Chalice
import requests

app = Chalice(app_name='abc')

r = requests.get('https://delete-this-1329.firebaseio.com/users.json')
print("r.status_code: ", r.status_code)
print("r.headers['content-type']: ", r.headers['content-type'])
print("r.encoding: ", r.encoding)
print("r.json(): ", r.json())

for key in r.json():
    print("key: ", key)
    print("value: ", r.json()[key])

@app.route('/hello', methods=['GET'])
def abcfunc():
    return {"message": "hello world"}


@app.route('/', methods=['GET'])
def abcfuncaa():
    return {"message": "slash hello world"}


@app.route('/webhook', methods=['POST'])
def myFunction():
    # This is the JSON body which is sent in POST request.
    jsonBody = app.current_request.json_body

    if jsonBody.get('result').get('action') == 'wellcome':
        print('wellcome action detected')

        return {"speech": "Wellcome to the bot, say book hotel to book it any time"}

    elif jsonBody.get('result').get('action') == 'bookHotel':
        print('hotel booking action detected')

        data = {
            "name": jsonBody.get('result').get('parameters').get('number'),
            "color": jsonBody.get('result').get('parameters').get('color')
        }
        print("dictionary made ", data)

        result = requests.post('https://delete-this-1329.firebaseio.com/tests.json', data = data)
        print("result: ", result)
        
        return{"speech": " hotel booking done"}

    else:
        print('No Action detected')
        return{"speech": "No Action Detected"}
