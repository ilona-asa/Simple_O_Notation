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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import re
def find_telemarketers(calls, texts):
    telemarketers = list()
    receiver = all_call_receiver(calls)
    texter = all_text_participant(texts, 0)
    text_receiver = all_text_participant(texts, 1)
    for call in calls:
        caller = call[0]
        if re.search("^140", caller):
            telemarketers.append(caller)
        elif not (caller in receiver and caller in texter and caller in text_receiver):
            telemarketers.append(caller)
    return sorted(set(telemarketers))

def all_call_receiver(calls):
    receiver = list()
    for call in calls:
        receiver.append(call[1])
    return set(receiver)

def all_text_participant(texts, index):
    texter = list()
    for text in texts:
        texter.append(text[index])
    return set(texter)
        

print("These numbers could be telemarketers: ")
print(find_telemarketers(calls, texts))