import os
import csv
import operator
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
empids=[]
first_name=[]
last_name=[]
date=[]
ssn_masked=[]
state_postal_code=[]
employee_csv = os.path.join("..","Resources","employee_data.csv")

# Open the CSV
with open(employee_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        empids.append(row[0])
        first_name.append(row[1].split(" ")[0])
        last_name.append(row[1].split(" ")[1])
        date.append(row[2].split("-")[1]+"/"+row[2].split("-")[2]+"/"+row[2].split("-")[0])
        ssn_masked.append("***-**-"+row[3].split("-")[2])
        state_postal_code.append(us_state_abbrev[row[4]])

with open("PyBoss.csv","w", newline="") as csvfile:
    csvwriter =csv.writer(csvfile, delimiter = ",")
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN", "State"])
    for listitems in zip(empids,first_name,last_name,date,ssn_masked,state_postal_code):
        csvwriter.writerow(listitems)

