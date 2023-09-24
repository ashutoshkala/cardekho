from flask import Flask,render_template,request
import pandas as pd
from joblib import load
clf0 = load('pipe0.joblib')
clf1= load('pipe1.joblib')
clf2= load('pipe2.joblib')

app = Flask(__name__)
col=['car_name', 'vehicle_age', 'km_driven', 'seller_type', 'fuel_type','transmission_type', 'mileage', 'engine', 'max_power', 'seats']
car_name=['Maruti Alto', 'Hyundai Grand', 'Hyundai i20', 'Ford Ecosport','Maruti Wagon R', 'Hyundai i10', 'Hyundai Venue', 'Maruti Swift','Hyundai Verna', 'Renault Duster','Mini Cooper', 'Maruti Ciaz','Mercedes-Benz C-Class', 'Toyota Innova', 'Maruti Baleno',
       'Maruti Swift Dzire', 'Volkswagen Vento', 'Hyundai Creta',
       'Honda City', 'Mahindra Bolero', 'Toyota Fortuner', 'Renault KWID',
       'Honda Amaze', 'Hyundai Santro', 'Mahindra XUV500',
       'Mahindra KUV100', 'Maruti Ignis', 'Datsun RediGO',
       'Mahindra Scorpio', 'Mahindra Marazzo', 'Ford Aspire', 'Ford Figo',
       'Maruti Vitara', 'Tata Tiago', 'Volkswagen Polo', 'Kia Seltos',
       'Maruti Celerio', 'Datsun GO', 'BMW 5', 'Honda CR-V',
       'Ford Endeavour', 'Mahindra KUV', 'Honda Jazz', 'BMW 3', 'Audi A4',
       'Tata Tigor', 'Maruti Ertiga', 'Tata Safari', 'Mahindra Thar',
       'Tata Hexa', 'Land Rover Rover', 'Maruti Eeco', 'Audi A6',
       'Mercedes-Benz E-Class', 'Audi Q7', 'BMW Z4', 'BMW 6', 'Jaguar XF',
       'BMW X5', 'MG Hector', 'Honda Civic', 'Isuzu D-Max',
       'Porsche Cayenne', 'BMW X1', 'Skoda Rapid', 'Ford Freestyle',
       'Skoda Superb', 'Tata Nexon', 'Mahindra XUV300',
       'Maruti Dzire VXI', 'Volvo S90', 'Honda WR-V', 'Maruti XL6',
       'Renault Triber', 'Lexus ES', 'Jeep Wrangler', 'Toyota Camry',
       'Hyundai Elantra', 'Toyota Yaris', 'Mercedes-Benz GL-Class',
       'BMW 7', 'Maruti S-Presso', 'Maruti Dzire LXI', 'Hyundai Aura',
       'Volvo XC', 'Maserati Ghibli', 'Bentley Continental', 'Honda CR',
       'Nissan Kicks', 'Mercedes-Benz S-Class', 'Hyundai Tucson',
       'Tata Harrier', 'BMW X3', 'Skoda Octavia', 'Jeep Compass',
       'Mercedes-Benz CLS', 'Datsun redi-GO', 'Toyota Glanza',
       'Porsche Macan', 'BMW X4', 'Maruti Dzire ZXI', 'Volvo XC90',
       'Jaguar F-PACE', 'Audi A8', 'ISUZU MUX', 'Ferrari GTC4Lusso',
       'Mercedes-Benz GLS', 'Nissan X-Trail', 'Jaguar XE', 'Volvo XC60',
       'Porsche Panamera', 'Mahindra Alturas', 'Tata Altroz', 'Lexus NX',
       'Kia Carnival', 'Mercedes-AMG C', 'Lexus RX', 'Rolls-Royce Ghost',
       'Maserati Quattroporte', 'Isuzu MUX', 'Force Gurkha']
values=[]
predictedvalues=[]

def predictt():
    data = dict(zip(col, values))
    values.clear()
    X_test = pd.DataFrame(data, index=[0])
    pred0=clf0.predict(X_test)
    pred1=clf1.predict(X_test)
    pred2=clf2.predict(X_test)
    pred=pred0+pred1+pred2
    pred=pred/3
    x=int(pred[0])
    predictedvalues.append(x)
    return predictedvalues[-1]

@app.route('/' ,methods =["GET", "POST"])

def main():
    if request.method == "POST":
        car = request.form.get("cars")
        values.append(car_name[int(car)])
        age = request.form.get("age")
        values.append(int(age))
        km = request.form.get("km")
        values.append(int(km))
        seller = request.form.get("seller")
        values.append(seller)
        fuel = request.form.get("fuel")
        values.append(fuel)
        transmission=request.form.get("trans")
        values.append(transmission)
        mileage=request.form.get("mileage")
        values.append(float(mileage))
        engine=request.form.get("engine")
        values.append(int(engine))
        max_power=request.form.get("pow")
        values.append(float(max_power))
        seats=request.form.get("seats")
        values.append(int(seats))
        ans="Value for your used "+ values[0] +" is Rs."
        x=predictt()
        ans=ans+str(x)
        return ans
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run()

