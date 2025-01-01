import sys
import csv

# Adapted from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# In this program, we'll build up to a full program that searches through
# patient records to find any patients matching a search criteria.
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
# You've got this!

def read_patient_logs(filename:str):
    '''
    Note: Some diagnoses in the csv have leading spaces, so you'll need to strip these
    out. Experiment with using the Python str.strip() function to do this for you.
    
    Work on getting basic data read in from the csv first. Once you achieve this 
    milestone, then you can modify the function to add additional data processing.
    '''
    entries = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for entry in csv_reader:
            entry = {
                'id': entry[0],
                'name': entry[1],
                'age': entry[2],
                'gender': entry[3],
                'symptoms': entry[4],
                'diagnosis': entry[5].strip()
            }
            entries.append(entry)
    return entries

def find_commonalities(entries: list, symptom: str):
    # Iterate through entries. Add any entries containing target "symptom" to a list.
    matching = [] # create destination list outside for loop
    for entry in entries:
        if symptom in entry['symptoms']:
            matching.append(entry)
    return matching

def find_freq(outcomes: list):
    '''
    Given a list of outcomes, returns a dictionary of unique outcomes, and their
    odds (frequency).
    E.g. 
    >>> find_freq(['a', 'a', 'b', 'a'])
        {'a': 3, 'b': 1}
    '''
    # Create a dict for storing each unique outcome and its count (frequency)
    uniques = {}
    for outcome in outcomes:
        if outcome in uniques:
            # Exists in dict. Increment count by 1.
            uniques[outcome] += 1
        else:
            # Doesn't exist in dict yet. Create new key->value pair, count = 1
            uniques[outcome] = 1
    return uniques

def get_probabilities_from_freq(outcomes: dict) -> dict:
    # Count up total number of outcomes by summing the freq of each outcome
    num_outcomes = 0
    for outcome in outcomes:
        num_outcomes += outcomes[outcome]
    
    # Rescale each outcome to probability
    probabilities = {}
    for outcome in outcomes:
        probabilities[outcome] = outcomes[outcome] / num_outcomes
    return probabilities


def write_entries_to_file(symptom, entries):
    # Handle if entries are empty (e.g. if no matches were found.)
    if not entries:
        return
    
    
    with open(f"{symptom}.csv", mode='w') as file:
        fieldnames = list(entries[0])
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)
    return


def main(target_file, target_symptom):
    print("\nDifferential Diagnosis")

    # Step 1: Read in data from each csv file (e.g. data/patient_records_yyyy.csv )
    entries = read_patient_logs(target_file)
    #print(entries)
    # ^^ Uncomment when you are ready to test this function
    # Don't be afraid to put temporary "print" statements to verify your data
    # and help with visualizing its structure for each next step!

    # Step 2: Create a new list containing only entries that match the symptom
    matching_entries = find_commonalities(entries, target_symptom)
    #print(matching_entries)

    # Step 4 (Do this later): Output the matching entries to a file.
    # Name the file according to the target symptom, e.g. "cough.csv"
    write_entries_to_file(target_symptom, matching_entries)

    # Step 3: For each diagnosis in the list, get its frequency & probability
    # In other words, we are finding P(diagnosis | symptom)
    #
    # You'll need to do some data manipulation before calling find_freq() and 
    # get_probabilities_from_freq(), to get your data in a list form, e.g.:
    #   ['common cold', 'common cold', 'flu', 'common cold', 'flu', 'tuberculosis', ...]
    
    # Get data into list form of only diagnoses
    diagnoses = []
    for entry in matching_entries:
        diagnoses.append(entry['diagnosis'])
    # Find frequencies & probabilities
    frequencies = find_freq(diagnoses)
    probabilities = get_probabilities_from_freq(frequencies)
    
    # Print outputs
    print(f"{'Diagnosis':<17} | {'Frequency':<8} | {'P(Diagnosis|Symptom)':<8}")
    for diagnosis in frequencies:
        print(f"{diagnosis:<20} {frequencies[diagnosis]:<6} {probabilities[diagnosis]:10.2f}")

    # Handle if no matches were found
    if not diagnoses:
        print("\nNo matching entries found. No output written.")
    else:    
        print(f"\nMatching entries saved to {target_symptom}.csv")

if __name__ == '__main__':
    # Step 0: Process command-line arguments, if provided, before calling main
    # If no arguments are given, print usage instructions and then quit.
    # differential_diagnosis.py [file] [target_symptom]
    args = sys.argv[1:]
    if len(args) == 0:
        print("""
        No arguments specified...
              
              Call this program with arguments as:
                    program.py <patient_records_yyyy.csv> [symptom]

              For example:
              $ program.py patient_records_2018.csv cough
              $ program.py patient_records_2018.csv "scratchy throat"

              If no symptom is given, all symptoms will be matched.
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