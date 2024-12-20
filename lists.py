import backend

# Adapted from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# Try to complete as many functions as you can! ❤
# Keep an eye out for surprises in the output when you 
# get all tests in a function correct!

# A. Feedback Form
# Given a list of customer feedback strings, return the count of the
# number of strings where the customer has a lot to say! We want to process
# these and make sure we account for them.
# We'll define "a lot to say" as a string length of 10 or more.
# Note: python does not have a ++ operator, but += works, such that
# >>> x = 5
# >>> x += 2
# >>> # is functionally equivalent to
# >>> x = x + 2
def count_big_feedback(feedback_form):
    num_big_feedback = 0
    for feedback in feedback_form:
        if len(feedback) >= 15:
            num_big_feedback += 1
    return num_big_feedback


# B. Differential Diagnosis
# Given a list of strings, return a list with the strings
# in sorted order. 
# The MAs have written out a list of symptoms reported by your patients. The
# provider has asked you to alphabetize the symptoms to make differential diagnosis
# easier. 
#
# However, some items will have an underscore "_" preceding. These are very important!!
# The doctor wants these placed first. Therefore, alphabetize these items first, and
# group them before all the rest; then follow up with the remaining alphabetized items. 
# Strip off the underscore from any items that have it.
#
# Example:
# >>> diff_diagnose(['fever', 'rash', 'cough', '_vomiting', '_nausea'])
# outputs:
#   ['nausea', 'vomiting', 'cough', 'fever', 'rash']
#
# Hint: Programming languages usually have built-in functions for basic data
# manipulations, like len(), range(), str.upper(), str.lower(), etc.
# Always consider built-in functions! You can usually write your own
# implementation, but why not leverage the work of others who came before?
# In this case, the function you'll want to use is called sorted(). 
# Investigate how you might find this by googling, if you didn't know it existed.
#
# Hint 2: part of this task can be done by making 2 lists from the given 
# symptoms list, and sorting each of these before combining them.
def alphabetize(symptoms):
    priority_symptoms = []
    secondary_symptoms = []
    for symptom in symptoms:
        if symptom[0] == '_':
            priority_symptoms.append(symptom[1:])
        else:
            secondary_symptoms.append(symptom)
    
    priority_symptoms = sorted(priority_symptoms)
    secondary_symptoms = sorted(secondary_symptoms)
    sorted_symptoms = priority_symptoms + secondary_symptoms

    return sorted_symptoms


# C. Missing Vaccinations
# Oh golly! The dirt is really moving slowly today! 
# We'll never get all the patients seen today at the rate we're going!
# Luckily, you can see from the schedule that most of the delay is for vaccinations.
# 
# Write a function that takes in a list of vaccinations a patient has already
# received (e.g., ['MMR', 'Hepatitis B', 'Flu']) and returns the list of
# vaccinations that are missing from their complete vaccination schedule.
#
# For example:
# >>> find_missing_vaccinations(['polio', 'hpv'], ['polio', 'hpv', 'covid', 'rsv', 'ipv', 'var', 'hepA'])
# Output:
#       ['covid', 'rsv', 'ipv', 'var', 'hepA']
#
# For simplicity, don't worry about age or anything like that...
# This is a communist clinic — everyone is getting the same vaccinations!! ⚒ ⚒ ⚒
def find_missing_vaccinations(received_vaccines, all_vaccines):
    vaccines_needed = []
    for vaccine in all_vaccines:
        if vaccine not in received_vaccines:
            vaccines_needed.append(vaccine)
    return vaccines_needed


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

    backend.title_sequence('Feedback Form')
    # Each line calls blood_pressure(), compares its result to the expected for that call.
    results.append(test( count_big_feedback(['Great service', '2/10 service, Jake not there :(', 'lol this ur bf']), 1 ))
    results.append(test( count_big_feedback(['meh', 'I really liked Mia she\'s amazing!', 'Cool place', "I think the trainer here works really hard!"]), 2 ))
    results.append(test( count_big_feedback(['I liked it', 'Whatever', 'It\'s cool I guess']), 1 ))

    if min(results) == 1:
        print(backend.decrypt('\x14Nok|*Wsk6*\x81o*k|o*o\x82ms~on*~y*}rk|o*yxo*yp*y\x7f|*~yz*mvsxsm*|o\x80so\x81}' +
                              '+*\x14\x14O\x82mo|z~*p|yw*mvsxsm*|o\x80so\x81*py|wD*\x14O\x80o|\x83*~swo*S*qo~*~ro*' +
                              'mrkxmo6*S*k}u*~y*lo*}oox*l\x83*Wsk8*]ro1}*t\x7f}~*~ro*lo}~+*S*kw*}y*swz|o}}on*l\x83*'+
                              'ro|*z|ypo}}syxkvs}w*kxn*o\x82moz~syxkv*mk|o8*Zv\x7f}6*S*rok|n*}ro1}*vok|xsxq*ry\x81' +
                              '*~y*myno*sx*Z\x83~ryxI*Kwk\x84sxq+*ark~*k*lyvn6*y\x7f~qysxq6*kxn*o\x82ms~sxq*zo|}yx' +
                              'kvs~\x838*Zv\x7f}6*}ro*vyyu}*qyyn*77*kw*S*kvvy\x81on*~y*\x81|s~o*~rk~*yx~y*k*poonlkm'+
                              'u*py|wI*]y||\x836*s~1}*~|\x7fo*~ry\x7fqr888'))


    backend.title_sequence('Differential Diagnosis')
    results = []
    symptoms_list = [['_fever', '_cough', 'chills', 'loss of appetite'],
                    ['headache', 'dizziness', '_nausea', '_vomiting'],
                    ['chest pain', 'shortness of breath', '_palpitations', 'fatigue'],
                    ['rash', 'itching', 'swelling in legs', 'joint pain'],
                    ['blurred vision', 'sensitivity to light', '_eye pain', 'headache']]
    
    symptoms_list_alphabetized = [['cough', 'fever', 'chills', 'loss of appetite'],
                    ['nausea', 'vomiting', 'dizziness', 'headache'],
                    ['palpitations', 'chest pain', 'fatigue', 'shortness of breath'],
                    ['itching', 'joint pain', 'rash', 'swelling in legs'],
                    ['eye pain', 'blurred vision', 'headache', 'sensitivity to light']]

    for i in range( len(symptoms_list) ):
        results.append(test( alphabetize(symptoms_list[i]), symptoms_list_alphabetized[i]) )

    if min(results) == 1:
        print(backend.decrypt('\x141^rkxu}*py|*nysxq*~rs}*py|*wo+*Kxn*}y*{\x7fsmuv\x836*~yy+*cy\x7f1|o*sxm|onslvo+1' +
                              '\x1477*1Kr6*xy*z|ylvow+*S~*yxv\x83*~yyu*k*}om+1'))


    backend.title_sequence('The Dirt!!')
    all_vaccinations = ['polio', 'hpv', 'covid', 'rsv', 'ipv', 'var', 'hepA']
    results.append(test( find_missing_vaccinations(['polio', 'hpv'], all_vaccinations), ['covid', 'rsv', 'ipv', 'var', 'hepA']))
    results.append(test( find_missing_vaccinations(['hpv', 'hepA', 'rsv', 'covid'], all_vaccinations), ['polio', 'ipv', 'var']))
    results.append(test( find_missing_vaccinations(['hpv', 'covid', 'polio', 'rsv' ], all_vaccinations), ['ipv', 'var', 'hepA'] ))
    results.append(test( find_missing_vaccinations(['rsv', 'ipv', 'var', 'polio', 'hpv', 'covid', 'hepA'], all_vaccinations), []))
    
    if min(results) == 1:
        print(backend.decrypt('\x14ay\x816*o\x80o|\x83yxo*qy~*}oox*~ynk\x83+*cy\x7f*nsn*k*q|ok~*tyl*uoozsxq*o\x80o|\x83~' +
                              'rsxq*}rsz7}rkzo+*Q|ok~*\x81y|u6*~rkxu*\x83y\x7f*}y*w\x7fmr+'))

    print("\n\n")

# Standard boilerplate to call main() function
if __name__ == '__main__':
    main()