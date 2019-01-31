from flask import *
import controller
app = Flask(__name__)
f = "Ber"
# Proportions for the mix
agar = 0
glyc = 0
water= 0
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/library")
def library():
    return render_template('library.html')

@app.route("/prepare")
def prepare():
    return render_template('prepare.html')

@app.route("/mixing")
def mixing():
    global agar
    global glyc
    global water
    agar = int(request.args.get('agar', 0, type=float)*10)
    glyc = int(request.args.get('glyc', 0, type=float)*10)
    water = int(request.args.get('water', 0, type=float)*10)
    print("content",agar,glyc,water)
    #controller.check_led()
    #print("stage 1")
    #controller.turn_on_pot()
    #print("stage 2")
    #controller.show()
    #print("stage 3")
    #c = 0
    #f = controller.show()
    return jsonify(result=agar + water)

@app.route("/mix")
def mix():
    controller.send_proportions(agar,water,glyc)
    return render_template('mixing.html', agarq = agar, waterq = water, glycq = glyc)

@app.route('/_add_numbers')
def _add_numbers():
    print("here")
    """
    agar = request.args.get('agar', 0, type=int)
    glyc = request.args.get('glycerine', 0, type=int)
    water= request.args.get('water',0,type=int)
    tag  = request.args.get('tag',0,type=str)
    print(agar,glyc,water,tag)
    data = jsonify(agar,glyc,water,tag)
    """
    a = request.args.get('a',0,type=int)
    b = request.args.get('b',0,type=int)
    result = a + b

    return render_template('mixing.html', result = result)

@app.route('/_showing')
def show():
    print ("showing")
    f = controller.show()
    print(f)
    return jsonify(temp=f)

if __name__ ==  "__main__":
    app.run(debug = True, host = "0.0.0.0", port= 80)

