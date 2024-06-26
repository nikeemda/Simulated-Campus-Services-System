from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify

import firebase_admin
from firebase_admin import credentials, firestore

import nfcHandler

aid_android = [0xF0, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06]


app = Flask(__name__)

cred = credentials.Certificate("uwallet-firebase-sdk.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

#reader = nfc.Reader()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)



@app.route('/check-nfc')
def check_nfc():
    try:
        uid = nfcHandler.select_application(aid_android)
        if uid:
            user_ref = db.document(f"users/{uid}/person/meal_plan")
            user_doc = user_ref.get()
            if user_doc.exists:
                meal_plan_data = user_doc.to_dict()
                dining_dollars = meal_plan_data.get("dining_dollars", 0)
                return jsonify(status='ok', uid=uid, dining_dollars=dining_dollars)
            else:
                return jsonify(status='error', message='No meal plan found.')
        else:
            return jsonify(status='waiting')
    except Exception as e:
        return jsonify(status='error', message=str(e))

@app.route('/check-meal-swipes')
def check_meal_swipes():
    try:
        uid = nfcHandler.select_application(aid_android)  # Replace 'aid_android' with actual NFC data
        if uid:
            user_ref = db.document(f"users/{uid}/person/meal_plan")
            user_doc = user_ref.get()
            if user_doc.exists:
                meal_plan_data = user_doc.to_dict()
                swipes = meal_plan_data.get("swipes", 0)
                guest_swipes = meal_plan_data.get("guest_swipes", 0)
                return jsonify(status='ok', uid=uid, swipes=swipes, guest_swipes=guest_swipes)
            else:
                return jsonify(status='error', message='No meal plan found.')
        else:
            return jsonify(status='waiting')
    except Exception as e:
        return jsonify(status='error', message=str(e))
    

@app.route('/pos', methods=['GET', 'POST'])
def point_of_sale():
    
    try:
        uid = nfcHandler.select_application(aid_android)
    except Exception as e:
        uid = None

    dining_dollars = 0  # Default value if UID is not fetched

    if uid:
        path = "users/" + uid + "/person/meal_plan"
        user_ref = db.document(path)
        user_doc = user_ref.get()
       
        if user_doc.exists:
            meal_plan_data = user_doc.to_dict()
            dining_dollars = float(meal_plan_data.get("dining_dollars", 0))

    if request.method == 'POST' and uid:
        sale_amount = float(request.form['sale-amount'])
        new_dining_dollars = dining_dollars - sale_amount
       
        if new_dining_dollars < 0:
            return "Insufficient dining dollars."
       
        user_ref.update({"dining_dollars": new_dining_dollars})
        return redirect(url_for('point_of_sale'))

    return render_template('pos.html', dining_dollars=dining_dollars, uid=uid or "N/A")
    


@app.route('/meal-swipes', methods=['GET', 'POST'])
def meal_swipes():
    try:
        uid = nfcHandler.select_application(aid_android)
    except Exception as e:
        uid = None

    swipes, guest_swipes = 0, 0  # Default values if UID is not fetched

    if uid:
        path = "users/" + uid + "/person/meal_plan"
        document_ref = db.document(path)
        document = document_ref.get()

        if document.exists:
            data = document.to_dict()
            swipes = int(data.get("swipes", 0))
            guest_swipes = int(data.get("guest_swipes", 0))

    if request.method == 'POST' and uid:
        if 'use-meal-swipe' in request.form:
            swipes = max(0, swipes - 1)
            document_ref.update({"swipes": swipes})
       
        elif 'use-guest-swipe' in request.form:
            guest_swipes = max(0, guest_swipes - 1)
            document_ref.update({"guest_swipes": guest_swipes})

        return redirect(url_for('meal_swipes'))

    return render_template('meal-swipes.html', swipes=swipes, guest_swipes=guest_swipes, uid=uid)
    
    
@app.route('/door-access')
def door_access():
    return render_template('door-access.html')

@app.route('/dorm')  # Route for dorm selection page
def dorm():
    return render_template('dorm.html')

@app.route('/dooly', methods=['GET', 'POST'])
def dooly_access():
    if request.method == 'POST':
        room_number = request.form['room_number']
        uid = nfcHandler.select_application(aid_android)
        if uid:
            path = f"users/{uid}/Dooly/{room_number}"
            user_ref = db.document(path)
            user_doc = user_ref.get()
            
            if user_doc.exists:
                access_status = f"Access granted to room: {room_number}"
            else:
                access_status = f"Access denied to room: {room_number}"
        else:
            access_status = "NFC activity not detected"
        
        return render_template('dooly.html', access_status=access_status)
    
    return render_template('dooly.html', access_status="No NFC activity detected")


@app.route('/whitten', methods=['GET', 'POST'])
def whitten_access():
    if request.method == 'POST':
        room_number = request.form['room_number']
        uid = nfcHandler.select_application(aid_android)
        if uid:
            path = f"users/{uid}/Whitten/{room_number}"
            user_ref = db.document(path)
            user_doc = user_ref.get()
            
            if user_doc.exists:
                access_status = f"Access granted to room: {room_number}"
            else:
                access_status = f"Access denied to room: {room_number}"
        else:
            access_status = "NFC activity not detected"
        
        return render_template('whitten.html', access_status=access_status)
    
    return render_template('whitten.html', access_status="No NFC activity detected")


@app.route('/mcarthur', methods=['GET', 'POST'])
def mcarthur_access():
    if request.method == 'POST':
        room_number = request.form['room_number']
        uid = nfcHandler.select_application(aid_android)
        if uid:
            path = f"users/{uid}/McArthur/{room_number}"
            user_ref = db.document(path)
            user_doc = user_ref.get()
            
            if user_doc.exists:
                access_status = f"Access granted to room: {room_number}"
            else:
                access_status = f"Access denied to room: {room_number}"
        else:
            access_status = "NFC activity not detected"
        
        return render_template('mcarthur.html', access_status=access_status)
    
    return render_template('mcarthur.html', access_status="No NFC activity detected")


@app.route('/eaton', methods=['GET', 'POST'])
def eaton_access():
    if request.method == 'POST':
        room_number = request.form['room_number']
        uid = nfcHandler.select_application(aid_android)
        
        if uid:
            path = f"users/{uid}/person/dorm"
            user_ref = db.document(path)
            user_doc = user_ref.get()
            
            if user_doc.exists:
                data = user_doc.to_dict()
                room_no = int(data.get("room_no"))
                dorm_name = data.get("dorm_name")
                
                if room_no == int(room_number) and dorm_name == "Eaton Residential College":
                    access_status = f"Access granted to room: {room_number}"
                else:
                    access_status = f"Access denied to room: {room_number}"
            else:
                access_status = "User document not found"
        else:
            access_status = "NFC activity not detected"
        
        return render_template('eaton.html', access_status=access_status)
    
    return render_template('eaton.html', access_status="No NFC activity detected")

@app.route('/lakeside', methods=['GET','POST'])
def lakeside_access():
    if request.method == 'POST':
        room_number = request.form['room_number']
        uid = nfcHandler.select_application(aid_android)
        
        if uid:
            path = f"users/{uid}/person/dorm"
            user_ref = db.document(path)
            user_doc = user_ref.get()
            
            if user_doc.exists:
                data = user_doc.to_dict()
                room_no = int(data.get("room_no"))
                dorm_name = data.get("dorm_name")
                
                if room_no == int(room_number) and dorm_name == "Lakeside Village":
                    access_status = f"Access granted to room: {room_number}"
                else:
                    access_status = f"Access denied to room: {room_number}"
            else:
                access_status = "User document not found"
        else:
            access_status = "NFC activity not detected"
        
        return render_template('lakeside.html', access_status=access_status)
    
    return render_template('lakeside.html', access_status="No NFC activity detected")



@app.route('/mahoney', methods=['GET', 'POST'])
def mahoney_access():
    if request.method == 'POST':
        room_number = request.form['room_number']
        uid = nfcHandler.select_application(aid_android)
        
        if uid:
            path = f"users/{uid}/person/dorm"
            user_ref = db.document(path)
            user_doc = user_ref.get()
            
            if user_doc.exists:
                data = user_doc.to_dict()
                room_no = int(data.get("room_no"))
                dorm_name = data.get("dorm_name")
                
                if room_no == int(room_number) and dorm_name == "Mahoney Residential College":
                    access_status = f"Access granted to room: {room_number}"
                else:
                    access_status = f"Access denied to room: {room_number}"
            else:
                access_status = "User document not found"
        else:
            access_status = "NFC activity not detected"
        
        return render_template('mahoney.html', access_status=access_status)
    
    return render_template('mahoney.html', access_status="No NFC activity detected")

if __name__ == "__main__":
    app.run(debug=True)