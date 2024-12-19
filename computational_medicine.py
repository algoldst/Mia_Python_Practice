import backend

def reverse_symptoms(symptoms: str) -> str:
    """
    Write a function that takes in a string of patient symptoms (e.g., 
    'fever cough headache') and returns the symptoms in reverse order, but 
    not reversing the words themselves (i.e., 'headache cough fever').
    """
    # Placeholder logic to be filled in later
    pass

def find_missing_vaccinations(received_vaccines: list, all_vaccines: list) -> list:
    """
    Write a function that takes in a list of vaccinations a patient has 
    received (e.g., ['MMR', 'Hepatitis B', 'Flu']) and returns a list of 
    vaccinations that are still missing from a complete vaccination schedule 
    (e.g., ['Polio', 'HPV'])
    """
    pass

def identify_high_cost_treatments(treatments: dict, threshold: float) -> dict:
    """
    Write a function that takes in a dictionary of medical treatments and their associated
    costs (e.g., 'gene therapy': 50000, 'chemotherapy': 2000) and returns a dictionary with
    only those treatments whose cost is above a certain threshold. 
    
    This information will be used in our lab to focus our research toward high-cost treatments
    that need lower-cost, affordable alternatives developed.
    """
    pass

def find_patient_commonalities(search_term: str):
    """
    Write a function that searches patient data for a search term (e.g.,
    a specific disease or symptom). The function should return all rows 
    (patients) containing that search term."
    """
    pass


def count_symptom_frequency(symptom: str, report: str) -> dict:
    """
    Write a function that takes in a string of clinical data (such as a list
    of patient-reported symptoms) and returns a dictionary where the keys are
    symptoms, and the values are the number of times each symptom appears across
    the dataset. This can be used to track the prevalence of different symptoms 
    in a cohort of patients.

    Example:
        count_symptom_frequencies("fever, headache, cough, fever, fatigue")
    Output: 
        {"fever": 2, "headache": 1, "cough": 1, "fatigue": 1}
    """
    pass



