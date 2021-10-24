 from pymongo import MongoReplicaSetClient
from flask import Flask, render_template, request
app = Flask(__name__)

connect_db = MongoReplicaSetClient('mongodb://localhost:27017/')
db = connect_db.sign_up
db_data = db.details
# for i in db_data:
#     print(i)

@app.route('/TRAVELS')
def TRAVELS():
    return render_template('TRAVELS.html')


@app.route('/Booking')
def Booking():
    return render_template("Booking.html")

@app.route('/Booking', methods=['POST'])
def sign_up():
    Passenger_name = request.form["name"]
    mobile = request.form["Mobile"]
    From = request.form["From"]
    To =request.form["To"]
    Adhar_num = request.form["Adhar"]
    Mail = request.form["Mail"]
    data = {"name":Passenger_name,"Mobile":mobile,"From":From,"To":To,"Adhar":Adhar_num,"Mail":Mail}
    d = db_data.insert_one(data)
    
    return render_template('Booking.html')

@app.route('/Details')
def Details():
    all_data= db_data.find({})
    data = list(all_data)
    return render_template('Details.html',data=data)

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Timings')
def Timings():
   return render_template("Timings.html")


# @app.route('/about')
# def about():
#     return render_template("about.html")

# @app.route('/showdata') 
# def showdata():
#     return render_template("showdata.html")

if __name__ == "__main__":
    app.run(debug=True)

connect_db.close()

