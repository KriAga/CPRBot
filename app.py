from flask import Flask

app = Flask(__name__)


buy_indicator_R1 = False
buy_indicator_PDH = False
sell_indicator_S1 = False
sell_indicator_PDL = False

buy_indicator = False
sell_indicator = False

@app.route('/greater_R1')
def greater_R1():
    buy_indicator_R1 = True
    return 'greater_R1'

@app.route('/lower_R1')
def lower_R1():
    buy_indicator_R1 = False
    return 'lower_R1'

@app.route('/greater_PDH')
def greater_PDH():
    buy_indicator_PDH = True
    return 'greater_PDH'

@app.route('/lower_PDH')
def lower_PDH():
    buy_indicator_PDH = False
    return 'lower_PDH'

@app.route('/greater_S1')
def greater_S1():
    sell_indicator_S1 = True
    return 'greater_S1'

@app.route('/lower_S1')
def lower_S1():
    sell_indicator_S1 = False
    return 'lower_S1'

@app.route('/greater_PDL')
def greater_PDL():
    sell_indicator_PDL = True
    return 'lower_PDL'

@app.route('/lower_PDL')
def lower_PDL():
    sell_indicator_PDL = False
    return 'lower_PDL!'

if __name__ == '__main__':
    app.run()