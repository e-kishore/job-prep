def get_water_bill(num_gallons):
    if num_gallons <8001:
        bill = int(num_gallons/1000) * 5
    elif num_gallons >8000 and num_gallons <22001:
        bill = int(num_gallons/1000) * 6
    elif num_gallons >22000 and num_gallons <30001:
        bill = int(num_gallons/1000) * 7
    else:
        bill = int(num_gallons/1000) * 10
    return bill
print(get_water_bill(90000))