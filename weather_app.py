from flask import Flask, request
app = Flask(__name__)

# ...
data = {
    "Boston" : "85.6",
    "New York" : "88.0",
    "San Francisco" : "81.3",
    "Los Angeles" : "84.2",
    "Chicago" : "72.3"
}


@app.route('/temperature', methods=['GET'])
def search():
    args = request.args
    city = args.get('city', default='')
    unit = args.get('celcius', default='fahrenheit')

    if city not in data.keys():
        return  "Unsupported city"
    else:
        return data[city]
