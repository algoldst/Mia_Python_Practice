import backend

# Adapted from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Intro dictionary (dict) exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# Try to complete as many functions as you can! ❤
# Keep an eye out for surprises in the output when you 
# get all tests in a function correct!


# A. Researching Cheaper Alternatives
# The CEO here is new, and is trying to avoid being shot like the last guy. They've 
# decided to focus our lab's research toward developing lower-cost, more affordable 
# treatment alternatives. Healthcare is just too damn expensive!
#
# To this end, we've compiled a dictionary of medical treatments and their associated costs,
# in thousands of dollars, e.g.
# {'gene therapy': 50, 'chemotherapy': 2}
# 
# Please filter this data to return a smaller dictionary of only those treatments whose
# cost is between a certain percentage (inclusive) of the most expensive options.
# 
# Example: To filter for only treatments between the 70% and 100% range of all possible
# treatments, we want to run:
# >>> identify_high_cost_treatments({'prayer': 66.60, 'vaccine': 90, 'massage': 69}, 70, 100)
#
# Returns: {'vaccine': 100}
# because this is the only treatment in the 70% - 100% price range of all considered treatments.
#
# Note: The function call below has a slightly different structure than you may recognize. 
# It doesn't actually change anything for you, but is an alternative format that you 
# should get used to seeing in practice. 
# So what's different? Well, it's a more explicit function definition. It supplies 
# additional information about the function arguments and return type that can
# be expected.
# The equivalent function would be written
#       identify_high_cost_treatments(treatments, min_percent, max_percent):
# and is simply non-explicit about what types of variables "treatments" and "min/max_percent" are.
# From this more explicit definitiion, we know that treatments is a dict, min/max are floats
# (that is, decimal values), and that the output is a dictionary.
#
def identify_treatments_in_range(treatments: dict, min_percent: float, max_percent: float) -> dict:
    # Find most expensive treatment available, for calculating threshold value
    max_cost_found = 0
    for treatment in treatments:
        treatment_cost = treatments[treatment]
        if treatment_cost > max_cost_found:
            max_cost_found = treatment_cost
        else:
            continue
    PERCENT = 0.01
    min_value = min_percent * PERCENT * max_cost_found
    max_value = max_percent * PERCENT * max_cost_found

    # Find keys to return
    ranged_treatments = {}
    for treatment in treatments:
        cost = treatments[treatment]
        if cost >= min_value and cost <= max_value:
            ranged_treatments[treatment] = cost
    
    return ranged_treatments


# A2. Treatment Binning
# Great work on the previous function! You can use your functions to build up larger
# functionality in your programs. Let's see how powerful this can be!
#
# We want to identify how many treatments are available in various price ranges. 
# Use your previous function to "slice" the dictionary into various percentile ranges:
# E.g. [0, 25, 50, 75, 100]  --> 0-25%, 25-50%, 50-75%, 75-100%
#
# Then, count up the number of options available in each range, and return this
# as a list.
#
# Hint: You may find that iterating through the elements of "percentiles"
# >>> for cost_range in percentiles:
# won't work as easily here, because you need to reference multiple adjacent elements
# of `percentiles` at the same time. 
# Instead, consider using the indices of percentiles on each iteration, like so:
#
# >>> for index in range( len(percentiles) ):
#
# which will give index = 0,1,2,3,4...[ len(percentiles) -1 ]  on each successive iteration.
# Then, you can reference the current index, AND the next index, at the same time:
# >>>     percentiles[index]     # => percentiles[0]
# >>>     percentiles[index+1]   # => percentiles[1]
#
# Note: The # => comment can be read as "evaluates to", as in saying
# " percentiles[index] evaluates to percentiles[0] "
#
def count_treatments_per_range(treatments: dict, percentiles: float) -> list:
    # Variable to hold number of options available in each percentile range
    num_options = []

    # Iterate ranges (pairs) from percentiles, up to 2nd-to-last element
    for index in range( len(percentiles) - 1 ):
        min_percent = percentiles[index]
        max_percent = percentiles[index+1]
        # Get dict of treatments within range, from previously-defined function
        ranged_treatments = identify_treatments_in_range(treatments, min_percent, max_percent)
        # Count it and store into the num_options list
        num_options.append( len(ranged_treatments) )
    
    return num_options

# B. Automatic Reporting
# Help! Our medical wing is full of patients, and insurance needs to know how
# many of each symptom we are treating. We can't afford to sit around counting up 
# how many patients have a cough, or a fever, or are nauseous...This is going
# to take FOREVER!!
#
# Wait — Mia! Didn't you say you could do some ~magic~ with data? Can you make this faster?
#
# ...
# Your mission: The hospital keeps logs of all active patients and their symptoms.
# This is stored as a nested list. (One list per patient, in the format <name> [symptoms].
# For each symptom you see, log it in a dict as a <key>, and track the frequency as
# the <value>.
#
# For example, if you see the following:
# [["John", "fever", "cough", "covid", "fatigue"],
#  ["Alice", "rash", "fever", "fatigue"]]
#
# Return a dict:-
# {'cough': 1, 'covid': 1, 'fatigue': 2, 'fever': 2, 'rash': 1}
#
# If you can do this, then we can count any number of patient symptoms!
def count_symptom_frequency(hospital_logs: list) -> dict:
    symptoms = {}
    for patient in hospital_logs:
        patient_symptoms = patient[1:]
        for patient_symptom in patient_symptoms:
            if patient_symptom in symptoms:
                symptoms[patient_symptom] += 1
            else:
                symptoms[patient_symptom] = 1
    return symptoms
    



# Simple test function to compare what is returned vs. what should be returned.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
        function_works = True
    else:
        prefix = '  X '
        function_works = False
    print('%s \tgot: %s \n\texpected: %s' % (prefix, repr(got), repr(expected)))
    return function_works

def main():

    # Stores results of function tests
    results = []

    backend.title_sequence('Researching Cheaper Alternatives')
    # Each line calls blood_pressure(), compares its result to the expected for that call.
    treatments = {
        'oral medication' : 24,
        'insulin therapy' : 60,
        'continuous glucose monitor' : 75,
        'dietary counseling' : 2.5,
        'bariatric surgery' : 20,
        'lifestyle changes' : 5,
        'heart disease meds' :  36,
        'CABG surgery' : 100,
        'angioplasty' : 40,
        'implantable devices': 50
    }
    results.append( test(identify_treatments_in_range(treatments, 0, 25), {'oral medication': 24, 'dietary counseling': 2.5, 'bariatric surgery': 20, 'lifestyle changes': 5}) )
    results.append( test(identify_treatments_in_range(treatments, 25, 50), {'heart disease meds': 36, 'angioplasty': 40, 'implantable devices': 50}) )
    results.append( test(identify_treatments_in_range(treatments, 50, 75), {'insulin therapy': 60, 'continuous glucose monitor': 75, 'implantable devices': 50}) )
    results.append( test(identify_treatments_in_range(treatments, 75, 100), {'continuous glucose monitor': 75, 'CABG surgery': 100}) )
    
    if min(results) == 1:
        print(backend.decrypt('\x14Yp*my\x7f|}o6*k*r\x7fq*s}*kv\x81k\x83}*p|oo8*Us}}o}*~yy8*Km~\x7fkvv\x836*\x81rk~*\x81y\x7fvnx1~*S*ny*py|*\x83y\x7fII*❮*'))

    backend.title_sequence('Count Em Up!')
    results = [test( count_treatments_per_range(treatments, [0, 25, 50, 75, 100]), [4,3,3,2] )]

    if min(results) == 1:
        print(backend.decrypt('\x14Xok~6*r\x7frI*Sx*yxv\x83*k*po\x81*vsxo}6*\x83y\x7f*wkno*}ywo*zy\x81o|p\x7fv*p\x7fxm~syxkvs~\x83+*Qs\x80ox*~ro*~swo6*' +
                            '\x83y\x7f*mkx*myno*z|o~~\x83*w\x7fmr*kx\x83~rsxq*\x83y\x7f*mkx*swkqsxo+'))
        print(backend.decrypt('\x14L\x83*~ro*\x81k\x836*kwk\x84sxq*\x81y|u+*^rs}*s}*xy~*ok}\x83*}~\x7fpp*~y*zsmu*\x7fz6*}y*S*mkx*~ovv*\x83y\x7f1|o*z\x7f' +
                            '~~sxq*sx*k*vy~*yp*oppy|~8*D3*S1w*\x80o|\x83*z|y\x7fn*yp*\x83y\x7f+*❮*'))


    backend.title_sequence('Automatic Reporting')
    hospital_logs = [['John', 'fever', 'covid', 'swelling', 'joint pain', 'fatigue'],
                    ['Alice', 'covid', 'fatigue', 'cough'],
                    ['Deborah', 'swelling', 'cramps', 'hypertension'],
                    ['Mark', 'covid', 'fever', 'migraine', 'fatigue'],
                    ['Emily', 'cough', 'fever', 'fatigue'],
                    ['James', 'joint pain', 'hypertension', 'fatigue'],
                    ['Sophia', 'migraine', 'cough', 'swelling'],
                    ['David', 'covid', 'fever', 'joint pain', 'fatigue'],
                    ['Lucas', 'swelling', 'hypertension', 'fatigue'],
                    ['Olivia', 'cough', 'fatigue', 'fever', 'migraine']]
    result = [test(count_symptom_frequency(hospital_logs), {'fever': 5, 'covid': 4, 'swelling': 4, 'joint pain': 3, 'fatigue': 8, 'cough': 4, 'cramps': 1, 'hypertension': 3, 'migraine': 3})]

    if min(results) == 1:
        print(backend.decrypt('\x14Q|ok~*\x81y|u+*Xy\x81*wkuo*}\x7f|o*\x83y\x7f*k}u*py|*k*|ks}o*77*^rs}*nsm~*ksx1~*p|oo+'))

    print("\n\n")

# Standard boilerplate to call main() function
if __name__ == '__main__':
    main()






