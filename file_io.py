import backend

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

def find_patient_commonalities(search_term: str) -> :
    """
    Write a function that searches patient data from a file for a search
    (e.g., a specific disease or symptom). The function should return 
    all rows (patients) containing that search term.
    """
    pass


def main():
    # Step 0: Parse command-line arguments
    #           [--output file.txt] <symptom>
    # Step 1: Read in text from each file ( patient_records_[year].csv )
    # Step 2: Extract to tuples (name, age, patient_id, [symptoms], diagnosis)
    # Step 3: Check for matching symptom; if match, add to list -> return
    # Step 4: Output pretty (command-line or file, depending on args): 
    # Step 5: Get frequency % for each matching diagnosis