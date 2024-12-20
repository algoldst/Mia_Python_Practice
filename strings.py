import backend

# An Adaptation from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# Try to complete as many functions as you can! ❤

# STRINGS

# A. Blood Pressure
# Given an int count of a number for blood pressure, return a string
# of the form 'Blood pressure: <systolic>/<diastolic>', substituting the number
# passed in. However:
#
#   - if the reading is high, then also say 'HIGH!'
#   - if the reading is much too high, then also say "HIGH! -- GET JAKE!!"
# 
# Don't worry about all the intricacies -- this is a "dumb" blood pressure monitor,
# so we'll define:
#
#   - "high" = systolic > 120, AND diastolic > 80,
#   - "too high" = systolic > 140, OR diastolic > 90
#
# Examples:
# >>> blood_pressure(110,70) returns 'Blood Pressure: 110/70'
# >>> blood_pressure(125,85) returns 'Blood Pressure: 125/85 HIGH!'
# >>> blood_pressure(180,100) returns 'Blood Pressure: 180/100 HIGH! -- GET JAKE!!'

def blood_pressure(systolic, diastolic):
    bp_string = "Blood Pressure: " + str(systolic) + "/" + str(diastolic)
    if (systolic > 120) and (diastolic > 80):
        bp_string += " HIGH!"
    if (systolic > 140) or (diastolic > 90):
        bp_string += " -- GET JAKE!!"
    return bp_string


# B. Genetic Markers
# Red alert! We've identified a new strain of cancer that
# can be caught early with biomarkers at the beginning and
# end of a short genetic sequence!!
# 
# Given a string of DNA code, return a string made of the first 2
# and the last 2 chars of the original string, so 'AAGCTT' yields 'AATT'. 
# 
# However, if the string length is less than 4, return instead an empty string ''.
def genetic_markers(genetic_string):
    first_last = ''

    if len(genetic_string) < 4:
        return first_last

    for i in range( len(genetic_string) ):
        if (i < 2) or ( i >= len(genetic_string) - 2 ):
            first_last += genetic_string[i]
    return first_last

# C. Unreasonable HIPPA Compliance
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# Examples:
# >>> hippa('Andrew Zidan') yields 'Andrew Zid*n'
# >>> hipp('Gigi Zidan') yields 'Gi*i Zidan'
#
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
# Try this in the Python interpreter if you want to test it out.
def hippa(s):
    # Set up temporary variable to hold first letter of s
    s1 = s[0]
    # Replace all occurrences of first letter s[0] with '*'
    s = s.replace(str.upper(s1),'*')
    s = s.replace(str.lower(s1),'*')
    # Get the first letter of original s, then add remaining part of altered s
    s = s1 + s[1:]
    return s


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first char of each string.
# e.g.
#   'mix', pod' -> 'pix mod'
#   'dag', 'nabbit' -> 'nag dabbit'
# Assume a and b are length 2 or more.
#
# Note: This has zero medical applicability, but if you don't bring spoonerisms
# to your work, do you even love what you do?

def spooner(a, b):
    # Store the first letters in variables
    a1 = a[0]
    b1 = b[0]

    a = b1 + a[1:]
    b = a1 + b[1:]
    return a + " " + b


# E. Genetic Palindromes
# In genetics, palindromic sequences are common in DNA, where they often
# form part of recognition sites for restriction enzymes or play important 
# roles in the regulation of genes. 

# A palindromic sequence is one that reads the same forwards and backwards 
# (e.g., 'GAATTC' is a palindrome because its reverse complement is also 'GAATTC').

# The lab boss needs YOU to write a function that takes in a DNA sequence and checks 
# whether it is a palindrome. 
#     - The function should account for the complementary base pairs in DNA
#         (A <---> T, and C <---> G). 
# If the sequence is a valid palindrome, return the original and palindrome.
# Otherwise, return "N/A"
# Examples:
# >>> identify_genetic_palindrome('ATCCTGCA')
#   
def identify_genetic_palindrome(gene_seq):
    reverse = gene_seq[::-1]
    # Convert letters to A-T C-G complements
    rev_pal = ''
    for letter in reverse:
        if letter == 'A':
            rev_pal += 'T'
        elif letter == 'T':
            rev_pal += 'A'
        elif letter == 'C':
            rev_pal += 'G'
        elif letter == 'G':
            rev_pal += 'C'

    if rev_pal == gene_seq:
        return gene_seq + " is a palindrome"
    else:
        return gene_seq + " is NOT a palindrome"
    return rev_pal


# Simple test function to compare what was is returned vs. what should be returned.
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

    backend.title_sequence('Blood Pressure')
    # Each line calls blood_pressure(), compares its result to the expected for that call.
    results.append(test(blood_pressure(110, 70), 'Blood Pressure: 110/70'))
    results.append(test(blood_pressure(130,80), 'Blood Pressure: 130/80'))
    results.append(test(blood_pressure(110,85), 'Blood Pressure: 110/85'))
    results.append(test(blood_pressure(125,87), 'Blood Pressure: 125/87 HIGH!'))
    results.append(test(blood_pressure(155,87), 'Blood Pressure: 155/87 HIGH! -- GET JAKE!!'))
    results.append(test(blood_pressure(185,163), 'Blood Pressure: 185/163 HIGH! -- GET JAKE!!'))

    if min(results) == 1:
        print(backend.decrypt('\x14ao*vy\x80o*Tkuo++*Kxn*Tkuo*vy\x80o}*\x83y\x7f+*D3*^rkxu*\x83y\x7f*py|*uoozsxq*\x83y\x7f|*zk~sox~}*}kpo+'))

    backend.title_sequence('Genetic String')
    results = []
    results.append( test(genetic_markers("CAACTTAGCCGAT"), 'CAAT') )
    results.append( test(genetic_markers("CAGATCGGTCAAACTTGATT"), 'CATT') )
    results.append( test(genetic_markers("AGG"), '') )
    results.append( test(genetic_markers("ATAGGCCGAC"), 'ATAC') )

    if min(results) == 1:
        print(backend.decrypt("\x14YR*Wc*QYN*S^]*MK_]ON*Lc*MK^]+*^RO*MK^]*K\\O*K^^KMUSXQ+++"))

    backend.title_sequence('Unreasonable HIPPA Compliance')
    results = []
    results.append( test(hippa('Andrew Zidan'), 'Andrew Zid*n'))
    results.append( test(hippa('Gigi Zidan'), 'Gi*i Zidan'))
    results.append( test(hippa('Dan Zidan'), 'Dan Zi*an'))
    results.append( test(hippa('Alex Goldstein'), 'Alex Goldstein'))

    if min(results) == 1:
        print(backend.decrypt('\x14arknn\x83k*wokx6*~ro\x83*my\x7fvnx1~*|okn*s~I*\x14888*aovv6*}s|6*s~*\x81k}*oxm|\x83z~on8'))

    backend.title_sequence('Spoons!')
    results = []
    results.append( test(spooner('box', 'cutter'), 'cox butter'))
    results.append( test(spooner('kitty', 'hawk'), 'hitty kawk'))
    results.append( test(spooner('sad', 'ballad'), 'bad sallad'))
    results.append( test(spooner('west', 'bank'), 'best wank'))

    if min(results) == 1:
        print(backend.decrypt('\x14]zyyxo|I*L\x7f~*S*lk|ov\x83*uxy\x81*ro|+*Rkrrkrkkrrkrkkrk*rkkrkrkrkrk*rkrrkrkkk+*8888**D2'))

    backend.title_sequence('Genetic Palindromes')
    results = []
    results.append( test(identify_genetic_palindrome('ACTGGCCAGT'), 'ACTGGCCAGT is a palindrome') )    
    results.append( test(identify_genetic_palindrome('GTAGATCTAC'), 'GTAGATCTAC is a palindrome') )
    results.append( test(identify_genetic_palindrome('GGATTAATTCC'), 'GGATTAATTCC is NOT a palindrome') )
    results.append( test(identify_genetic_palindrome('CGATTAATTCG'), 'CGATTAATTCG is NOT a palindrome') )
    results.append( test(identify_genetic_palindrome('AATACGTATT'), 'AATACGTATT is a palindrome') )


    if min(results) == 1:
        print(backend.decrypt('\x14K^^K^^KKMKMK++*^|\x83*}k\x83sxq*^RK^*?*~swo}*pk}~+*DN*\x14aro\x81+*Swkqsxo*nysxq*~rk~*\x81s~ry\x7f~*k*mywz\x7f~o|+'))

    print("\n\n")

# Standard boilerplate to call main() function
if __name__ == '__main__':
    main()