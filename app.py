from flask import Flask
from flask import request, url_for, redirect
import json
app = Flask(__name__)


buy_indicator_R1 = False
buy_indicator_PDH = False
sell_indicator_S1 = False
sell_indicator_PDL = False

buy_indicator = False
sell_indicator = False

buy_indicator_S2 = False
sell_indicator_R2 = False

@app.route('/crossing_up_R1', methods=['POST'])
def crossing_up_R1():
    global buy_indicator, buy_indicator_PDH, buy_indicator_R1
    buy_indicator_R1 = True
    data = json.loads(request.data.decode('utf-8'))
    if buy_indicator_PDH:
        buy_indicator = True
    if buy_indicator:
        print("BUY", data["close"])
    print('crossing_up_R1', buy_indicator, buy_indicator_PDH, buy_indicator_R1)
    return ('crossing_up_R1')

@app.route('/crossing_down_R1', methods=['POST'])
def crossing_down_R1():
    global buy_indicator, buy_indicator_R1
    buy_indicator_R1 = False
    buy_indicator = False
    print('crossing_down_R1')
    return ('crossing_down_R1')

@app.route('/crossing_up_PDH', methods=['POST'])
def crossing_up_PDH():
    global buy_indicator, buy_indicator_R1, buy_indicator_PDH
    buy_indicator_PDH = True
    data = json.loads(request.data.decode('utf-8'))
    if buy_indicator_R1:
        buy_indicator = True
    if buy_indicator:
        print("Buy", data["close"])
    print('crossing_up_PDH', buy_indicator, buy_indicator_R1)
    return ('crossing_up_PDH')

@app.route('/crossing_down_PDH', methods=['POST'])
def crossing_down_PDH():
    global buy_indicator, buy_indicator_PDH
    buy_indicator_PDH = False
    buy_indicator = False
    print('crossing_down_PDH')
    return ('crossing_down_PDH')

@app.route('/crossing_up_S1', methods=['POST'])
def crossing_up_S1():
    global sell_indicator, sell_indicator_S1
    sell_indicator_S1 = False
    sell_indicator = False
    print('crossing_up_S1')
    return ('crossing_up_S1')

@app.route('/crossing_down_S1', methods=['POST'])
def crossing_down_S1():
    global sell_indicator, sell_indicator_PDL, sell_indicator_S1
    sell_indicator_S1 = True
    data = json.loads(request.data.decode('utf-8'))
    if sell_indicator_PDL:
        sell_indicator = True
    if sell_indicator:
        print("Sell:", data["close"])
    print('crossing_down_S1')
    return ('crossing_down_S1')

@app.route('/crossing_up_PDL', methods=['POST'])
def crossing_up_PDL():
    global sell_indicator, sell_indicator_PDL
    sell_indicator_PDL = False
    sell_indicator = False
    print('crossing_up_PDL')
    return ('crossing_up_PDL')

@app.route('/crossing_down_PDL', methods=['POST'])
def crossing_down_PDL():
    global sell_indicator, sell_indicator_S1, sell_indicator_PDL
    sell_indicator_PDL = True
    data = json.loads(request.data.decode('utf-8'))
    if sell_indicator_S1:
        sell_indicator = True
    if sell_indicator:
        print("Sell:", data["close"])
    print('crossing_down_PDL')
    return ('crossing_down_PDL')

@app.route('/crossing_down_S2', methods=['POST'])
def crossing_down_S2():
    global buy_indicator, buy_indicator_S2
    buy_indicator_S2 = True
    data = json.loads(request.data.decode('utf-8'))
    buy_indicator = True
    if buy_indicator:
        print("Buy", data["close"])
    print('crossing_down_S2')
    return ('crossing_down_S2')

@app.route('/crossing_up_R2', methods=['POST'])
def crossing_up_R2():
    global sell_indicator, sell_indicator_R2
    sell_indicator_R2 = True
    sell_indicator = True
    data = json.loads(request.data.decode('utf-8'))
    if sell_indicator:
        print("Sell", data["close"])
    print('crossing_up_R2')
    return ('crossing_up_R2')

if __name__ == '__main__':
    app.run(debug=True)