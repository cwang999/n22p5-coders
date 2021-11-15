import requests

@app.route('/betting/')
def betting():
    context = {}
    context.update(json)
    return render_template('betting.html', context)

headers = {
    'X-CMC_PRO_API_KEY' : "c6c90802-3933-45c8-85bf-19d3d560a7f1",
    'Accepts' : 'application/json'
}

params = {
    'start' : '1',
    'limit' : '5',
    'convert' : 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
json = requests.get(url, params=params, headers=headers).json()
response = requests.get(url, params=params, headers=headers)
print(response.text)
print(response.json())

coins = json['data']

for x in coins:
    print(x['symbol'], x['quote']['USD']['price'] )

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

context = {}
for x in datarequest():
    context.update(x)

coins = json['data']

def datarequest():
    crypto_data = json.loads('data')
    return crypto_data

x = json
a = json.loads(x)
context.update(a)




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


