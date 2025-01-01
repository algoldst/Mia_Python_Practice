import sys
import csv

# Adapted from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# In this program, we'll build up to a full program that searches through
# patient records (from any patient_records_yyyy.csv file in the data/ folder) 
# to find all entries where the patient had a given symptom.
#
# From there, the program will:
# a) output all of the matching entries to a new csv file in the data/ folder
#       For example:
#           Given a search term "cough", all entries in the original csv where
#           a patient had "cough" will end up in the output file: data/cough.csv
# b) find all diagnoses that the given symptom might indicate, tabulating
#    the probability of each
#       For example:
#           Given the symptom "cough", the program may find:
#               Common Cold........... 56% likelihood
#               Flu....................34% likelihood
#               Asthma.................7% likelihood
#               Tuberculosis...........3% likelihood
#
# Workflow tip: don't build the whole program at once. Get it to an
# intermediate milestone and print your data structure, then sys.exit(0).
# When that's working, try for the next milestone.
# The main() program is written in parts to implement this functionality
# piecemeal.
#
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# 
# You've got this! :) ❤ ❤ ❤

def read_patient_logs(filename:str) -> list:
    '''
    Takes in a filename string (e.g. "data/patient_records_2018.csv") and reads the
    data from the csv into a single list of dicts:
    e.g.
    [ 
      {
        'id': 'IHA-03280', 
        'name': 'Amanda Santiago', 
        'age': '11', 
        'gender': 'Male', 
        'symptoms': 'watering eyes,cough,scratchy throat,sore throat', 
        'diagnosis': 'common cold'
      },
      {
        'id': 'XWY-74119', 
        'name': 'Michael Wilson', 
        'age': '28', 
        'gender': 'Female', 
        'symptoms': 'rash,itching,swelling,swollen lymph nodes', 
        'diagnosis': 'allergic reaction'
      },
      .... etc.
    ]

    Note: Some diagnoses in the csv have leading spaces, so you'll need to strip these
    out. Experiment with using the Python str.strip() function to do this for you.
    
    Work on getting basic data read in from the csv first. Once you achieve this 
    milestone, then you can modify the function to add additional data processing.
    '''
    return []

def find_commonalities(entries: list, target_symptom: str) -> list:
    """
    Accepts a list of entries dictionaries, and returns a filtered list containing
    only the dictionary entries that have the target symptom listed in their symptoms.
    
    We're only going to accept a single symptom for search, not multiple symptoms,
    so no need to split the symptoms apart.

    (Although, that would be cool! Maybe at the end you could add this functionality;
    if so, it would go in this function here. :)
    """
    return []

def write_entries_to_file(symptom:str, entries:list) -> None:
    """
    Writes entries to a file named [symptom].csv
    Optional: You could modify the arguments of the function, so that it accepts
    the year, and then the name can be [symptom]_[year].csv
    """
    return

def find_freq(outcomes: list) -> dict:
    '''
    Given a list of outcomes, returns a dictionary of unique outcomes, and their
    odds (frequency).
    E.g. 
    >>> find_freq(['a', 'a', 'b', 'a'])
        {'a': 3, 'b': 1}
    '''
    return

def get_probabilities_from_freq(outcomes: dict) -> dict:
    """
    Finds relative probabilities from given frequencies.
    For example, given a dictionary of the form:
        {'a': 3, 'b': 1}
    Returns:
        {'a': 0.75, 'b': 0.25}
    """
    return {}




def main(target_file, target_symptom):
    """
    For the most part, you shouldn't have to edit anything in here, except for step 4.
    """

    print("\nDifferential Diagnosis")

    # Step 1: Read in data from each csv file (e.g. data/patient_records_yyyy.csv )
    entries = read_patient_logs(target_file)
    # print(entries)
    # ^^ Uncomment to test this function!
    #    Make sure the output matches the format specified in the function docstring.
    #    You can also put print statements inside the function, to see what the intermediate
    #    state of your working data is. :)

    # Step 2: Create a new list containing only entries that match the target symptom
    matching_entries = find_commonalities(entries, target_symptom)
    #print(matching_entries)

    # Step 3: Output the matching entries to a file.
    # Name the file according to the target symptom, e.g. "cough.csv"
    write_entries_to_file(target_symptom, matching_entries)

    # Step 4: For each diagnosis in the list, get its frequency & probability
    # In other words, we are finding P(diagnosis | symptom)
    #
    # You'll need to do some data manipulation before calling find_freq() and 
    # get_probabilities_from_freq(), to get your data in a list form, e.g.:
    #   ['common cold', 'common cold', 'flu', 'common cold', 'flu', 'tuberculosis', ...]
    #
    # I've broken this out into steps below to help somewhat :)
    
    # a) Get data into list form of only the diagnoses
    
    
    # b) Find frequencies & probabilities
    
    
    # c) Print outputs according to the structure of this print statement
    print("Diagnosis | Frequency | P(Diagnosis|Symptom)")
    


# This part is done for you! :)
if __name__ == '__main__':
    # Step 0: Process command-line arguments, if provided, before calling main
    # If no arguments are given, print usage instructions and then quit.
    # A proper calling of the file should go:
    #       $ python differential_diagnosis.py [file] [target_symptom]

    args = sys.argv[1:]
    if len(args) == 0:
        print("""
        No arguments specified...
              
              Call this program with arguments as:
                    diagnosis.py <patient_records_yyyy.csv> [symptom]

              For example:
              $ diagnosis.py patient_records_2018.csv cough
              $ diagnosis.py patient_records_2018.csv "scratchy throat"

              If no symptom is given, all symptoms will be matched (target_symptom = "")
              """)
        sys.exit(0)
    
    target_file = args[0]

    if len(args) == 2:
        target_symptom = args[1]
    elif len(args) == 1:
        # Assume target_file given, default "" wildcard search
        target_symptom = ""

    # Run program
    main(target_file=target_file, target_symptom=target_symptom)