import requests
import json

# URL for the Flask API
url = "http://127.0.0.1:5000/patients"

# List of 20 patients to add
patients = [
    {"name": "John Doe", "dob": "1980-01-01", "address": "123 Main St", "phone": "555-0001"},
    {"name": "Jane Smith", "dob": "1985-02-02", "address": "456 Elm St", "phone": "555-0002"},
    {"name": "Alice Johnson", "dob": "1990-03-03", "address": "789 Oak St", "phone": "555-0003"},
    {"name": "Bob Brown", "dob": "1975-04-04", "address": "321 Pine St", "phone": "555-0004"},
    {"name": "Charlie Davis", "dob": "1982-05-05", "address": "654 Maple St", "phone": "555-0005"},
    {"name": "Diana Evans", "dob": "1995-06-06", "address": "987 Cedar St", "phone": "555-0006"},
    {"name": "Edward Wilson", "dob": "1988-07-07", "address": "123 Birch St", "phone": "555-0007"},
    {"name": "Fiona Green", "dob": "1992-08-08", "address": "456 Walnut St", "phone": "555-0008"},
    {"name": "George Harris", "dob": "1978-09-09", "address": "789 Poplar St", "phone": "555-0009"},
    {"name": "Hannah Lewis", "dob": "1983-10-10", "address": "321 Aspen St", "phone": "555-0010"},
    {"name": "Ian Clark", "dob": "1991-11-11", "address": "654 Redwood St", "phone": "555-0011"},
    {"name": "Jasmine Lee", "dob": "1987-12-12", "address": "987 Spruce St", "phone": "555-0012"},
    {"name": "Kevin Walker", "dob": "1984-01-13", "address": "123 Fir St", "phone": "555-0013"},
    {"name": "Laura King", "dob": "1989-02-14", "address": "456 Cypress St", "phone": "555-0014"},
    {"name": "Michael Scott", "dob": "1981-03-15", "address": "789 Palm St", "phone": "555-0015"},
    {"name": "Nina Taylor", "dob": "1993-04-16", "address": "321 Magnolia St", "phone": "555-0016"},
    {"name": "Oscar Martinez", "dob": "1979-05-17", "address": "654 Olive St", "phone": "555-0017"},
    {"name": "Paula Wright", "dob": "1986-06-18", "address": "987 Chestnut St", "phone": "555-0018"},
    {"name": "Quincy Adams", "dob": "1982-07-19", "address": "123 Sycamore St", "phone": "555-0019"},
    {"name": "Rachel Baker", "dob": "1990-08-20", "address": "456 Hickory St", "phone": "555-0020"}
]

# Function to add patients
def add_patients():
    for patient in patients:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(patient))
        if response.status_code == 201:
            print(f"Added patient: {patient['name']}")
        else:
            print(f"Failed to add patient: {patient['name']}, Status Code: {response.status_code}, Error: {response.text}")

# Run the function to add patients
if __name__ == "__main__":
    add_patients()
