import csv

items = []

with open("./day2.csv") as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        items.append(row)
    items.remove(items[0])

scores_1 = []
scores_2 = []

for row in items:
    if row[0] == 'A':
        if row[1] == 'X': scores_1.append(3+1)
        elif row[1] == 'Y': scores_1.append(6+2)
        else: scores_1.append(0+3)
    elif row[0] == 'B':
        if row[1] == 'X': scores_1.append(0+1)
        elif row[1] == 'Y': scores_1.append(3+2)
        else: scores_1.append(6+3)
    else: 
        if row[1] == 'X': scores_1.append(6+1)
        elif row[1] == 'Y': scores_1.append(0+2)
        else: scores_1.append(3+3)

print(f'solution 1: {sum(scores_1)}')

for row in items:
    if row[1] == "X":
        if row[0] == "A": scores_2.append(0+3)
        elif row[0] == "B": scores_2.append(0+1)
        else: scores_2.append(0+2)
    elif row[1] == "Y":
        if row[0] == "A": scores_2.append(3+1)
        elif row[0] == "B": scores_2.append(3+2)
        else: scores_2.append(3+3)
    else: 
        if row[0] == "A": scores_2.append(6+2)
        elif row[0] == "B" : scores_2.append(6+3)
        else: scores_2.append(6+1)

print(f"solution 2: {sum(scores_2)}")