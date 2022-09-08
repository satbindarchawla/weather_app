from flask import Flask, request
app = Flask(__name__)

# ...
data = {
    "India" : "INR",
    "Germany" : "EUR",
    "United States" : "USD",
    "AUSTRALIA" : "AUD",
    "CANADA" : "CAD",
    "DENMARK" : "DKK"
}


@app.route('/currencycode', methods=['GET'])
def search():
    args = request.args
    country = args.get('Country', default='')

    if country not in data.keys():
        return  "Unsupported country"
    else:
        return data[country]
