from faker import Faker
import pandas as pd
import random
import csv
import sys

# Quit if not right call
if len(sys.argv) == 1:
    print("Call with: \n\t fake_data.py [output_file.csv] [num_rows]")
    sys.exit(1)

# Arguments:
output_file = sys.argv[1]
rows = int( sys.argv[2] )

fake = Faker()

# Read in diseases from CSV
csv_file_path = 'data/diseases.csv'
data_list = []
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data_list.append(row)

# Create symptoms list from relative frequencies
diseases_list = [] # from above
for entry in data_list:
    for i in range(int(entry[0])):
        diseases_list.append(entry[1:])
for entry in diseases_list:
    print(entry)

# Create fake data. Sample from symptoms/diagnoses.
patient_data = []
for _ in range(rows):
    patient_id = fake.unique.bothify('???-#####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    name = fake.name()
    age = random.randint(1, 100)
    sex = random.choice(["Male", "Female", "Male", "Female", "Male", "Female", "Other"])
    
    # Pick a random disease row from the list
    disease = random.choice(diseases_list)
    diagnosis = disease[0].lower()
    symptoms = disease[1:]
    symptoms = [s.strip().lower() for s in symptoms]
    symptoms = random.sample(symptoms, k=random.randint(1,len(symptoms)))
    symptoms = ",".join(symptoms)
    
    patient_data.append([patient_id, name, age, sex, symptoms, diagnosis])

print(patient_data)

with open(output_file, mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Patient ID", "Name", "Age", "Sex", "Diagnosis", "Symptoms"])
    writer.writerows(patient_data)
    
    

