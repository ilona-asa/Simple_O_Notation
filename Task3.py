"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import re

# Part A
def find_Bangalore_caller(calls):
    codes = []
    for call in calls:
        if '(080)' in call[0]:
            match = re.search("\([0-9]+\)", call[1])
            if match:
                code = match.group(0)
                codes.append(code[1:-1])
            elif re.search("^[7-9]", call[1]):
                match = re.search("^[0-9]*", call[1])
                codes.append(match.group(0))
    return sorted(set(codes))

print("The numbers called by people in Bangalore have codes:")
print(find_Bangalore_caller(calls))


# Part B
def percent_Bangalore(calls):
    total = float(len(calls))
    count = 0
    for call in calls:
        if '(080)' in call[0] and '(080)' in call[1]:
            count += 1
    percentage = (count/total)*100
    return percentage
    
from_B_to_B = percent_Bangalore(calls)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(from_B_to_B,2)))
