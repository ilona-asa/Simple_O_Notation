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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def unique_telephone_numbers(texts, calls):
    phones = []
    for text in texts:
        phones.append(text[0])
        phones.append(text[1])
    for call in calls:
        phones.append(call[0])
        phones.append(call[1])
    phones_set = set(phones)
    return "There are " + str(len(phones_set)) + " different telephone numbers in the records."

print(unique_telephone_numbers(texts, calls))