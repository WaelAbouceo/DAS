from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://emr_user:your_password@104.236.69.146/emr_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Define a simple model to represent a patient
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(15))

    def __repr__(self):
        return f'<Patient {self.name}>'

# Home route
@app.route('/')
def home():
    return "Welcome to the EMR System!"

# Route to get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{'id': patient.id, 'name': patient.name, 'dob': patient.dob.strftime('%Y-%m-%d'), 'address': patient.address, 'phone': patient.phone} for patient in patients])

# Route to add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], dob=data['dob'], address=data['address'], phone=data['phone'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully'}), 201

# Route to get a specific patient by ID
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify({'id': patient.id, 'name': patient.name, 'dob': patient.dob.strftime('%Y-%m-%d'), 'address': patient.address, 'phone': patient.phone})

# Route to update a patient
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()
    patient = Patient.query.get_or_404(id)
    patient.name = data['name']
    patient.dob = data['dob']
    patient.address = data['address']
    patient.phone = data['phone']
    db.session.commit()
    return jsonify({'message': 'Patient updated successfully'})

# Route to delete a patient
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
