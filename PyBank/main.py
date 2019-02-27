import os
import csv

budget_csv = os.path.join("..","Resources","budget_data.csv")
print(budget_csv)

# Open the CSV
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the summary info
    for row in csvreader:
            csvreader.next(csv_reader, None)