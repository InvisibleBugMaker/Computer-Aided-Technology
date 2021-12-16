from flask import Flask, jsonify,request
app = Flask(__name__)

car_dict = {
        'make' : 'nissan',
        'model' : 'rogue',
        'year' : '2017',
        'color' : 'sliver',
        'number of seats' : '4',
        'owner' : 'JY',
        'odometer' : 3000,
        'passengers' : 'Tom, Jack, Mary',
        'trip' : [['Tom, Jack, 1000'], ['Mary, Eric, John, 80']]
    }
@app.route("/")
def a():
    '''return dictionary as a srting'''
    return str(car_dict)

@app.route("/car")
def b():
    '''return dictionary as a json'''
    return car_dict

@app.route("/car/make")
def c():
    '''return the specification of the car'''
    return str(car_dict['make'])
@app.route("/car/model")
def d():
    '''return the specification of the car'''
    return str(car_dict['model'])
@app.route("/car/year")
def e():
    '''return the specification of the car'''
    return str(car_dict['year'])
@app.route("/car/color")
def f():
    '''return the specification of the car'''
    return str(car_dict['color'])
@app.route("/car/number of seats")
def g():
    '''return the specification of the car'''
    return str(car_dict['number of seats'])
@app.route("/car/owner")
def h():
    '''return the specification of the car'''
    return str(car_dict['owner'])
@app.route("/car/odometer")
def i():
    '''return the specification of the car'''
    return str(car_dict['odometer'])
@app.route("/car/passengers")
def j():
    '''return the specification of the car'''
    return str(car_dict['passengers'])


@app.route("/trips", methods = ['GET','POST'])
def k():
    '''return the trips, and add a new trip'''
    if request.method == 'POST':
        data = request.get_json()
        car_dict['trip'].append(data['new'])
    return jsonify(car_dict['trip'])
    
    
if __name__ == "__main__":
    app.run(debug=True)