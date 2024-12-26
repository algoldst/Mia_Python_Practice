from faker import Faker
import random
import csv
fake = Faker()

'''
I have a csv file with the following:
relative_odds, disease, symptom, symptom, symptom (variable number of symptoms)
I want to read this into a list structure like so:
[relative_odds, disease, [symptoms]]

Python, how do I do it?
'''
symptoms_list = [] # from above
for symptom in symptoms_list:
    

rows = 433
patient_data = []
for _ in range(rows):
    patient_id = fake.unique.uuid4()
    name = fake.name()
    age = random.randint(1, 100)
    sex = random.choice(["Male", "Female", "Male", "Female", "Male", "Female", "Other"])
    diagnosis, symptoms = random.choice(symptoms_list)
    patient_data.append({
        "Patient ID": patient_id,
        "Name": name,
        "Age": age,
        "Sex": sex,
        "Symptoms Reported": ", ".join(symptoms),
        "Diagnosis": diagnosis
    })

# Convert to DataFrame and save as CSV
df_less_common = pd.DataFrame(patient_data)
file_path_less_common = "/mnt/data/less_common_patient_data.csv"
df_less_common.to_csv(file_path_less_common, index=False)

file_path_less_common