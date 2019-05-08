"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def on_the_phone(phone, calls):
    time_spent = 0
    for call in calls:
        if phone == call[0]:
            time_spent += int(call[3])
        elif phone == call[1]:
            time_spent += int(call[3])
    return time_spent

def unique_telephone_numbers(calls):
    phones = []
    for call in calls:
        phones.append(call[0])
        phones.append(call[1])
    return set(phones)

def total_time_spent(calls):
    phones = unique_telephone_numbers(calls)
    time_spent = []
    for phone in phones:
        time_spent.append(on_the_phone(phone, calls))
    phone_spent = zip(time_spent, phones)
    winner = max(phone_spent)
    return winner[1] + " spent the longest time, "+ str(winner[0]) +" seconds, on the phone during September 2016."
        
    
print(total_time_spent(calls))
