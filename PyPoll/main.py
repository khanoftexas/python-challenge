import os
import csv
#Initialize Variable
vote_count=0

election_csv = os.path.join("..","Resources","election_data.csv")

# Open the CSV
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        vote_count = vote_count + 1

print(f"Election Results") 
print(f"-------------------------")
print(f"Total Votes: {vote_count}")
print(f"-------------------------")

print(f"-------------------------")   
print(f"Winner: $"+ '\n')
print(f"-------------------------")



output_file = open("PyPoll.txt","w") 
 
output_file.write("Election Results"+ '\n') 
output_file.write("-------------------------"+ '\n')
output_file.write(f"Total Votes: {vote_count}"+ '\n')
output_file.write("-------------------------"+ '\n')

output_file.write("-------------------------"+ '\n')   
output_file.write(f"Winner: $"+ '\n')
output_file.write("-------------------------"+ '\n')
output_file.close() 