from typing import ClassVar


import csv
file = open("csv-sample.csv")
reader = csv.reader(file)
lines= len(list(reader))

print(lines)

