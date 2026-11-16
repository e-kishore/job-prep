import pandas as pd
import json
data1 = json.load(open('tickets.json'))
reader = pd.read_csv('tickets.csv')
data = list(reader)
tickets= data + data1


def validate(tickets):
    for ticket in tickets:
        if 'id' not in ticket or 'ticket_id' not in ticket :
            return (False)
        else:
            return (True)

for ticket in tickets:
    print(ticket)
    if validate([ticket]) == True:
        print("valid")
    elif validate([ticket]) == False:
        print("not valid")

