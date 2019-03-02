import os
import csv
#Initialize Variable
months_count=0
total_profit_loss=0
budget_csv = os.path.join("..","Resources","budget_data.csv")

# Open the CSV
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Counts the Total Rows
    rows_values=[r for r in csvreader]
    # Default values starting from row 1 bypassing headers
    profit_change = 0 #int(rows_values[1][1])
    
    greatest_increase_row=rows_values[1]
    greatest_decrease_row=rows_values[1]

    #Looping to calculate number of months, profit change, minimum, maximum
    for i in range(1,len(rows_values)):
        months_count=months_count+1
        row=rows_values[i]
        total_profit_loss= total_profit_loss + int(row[1]) 

        if i > 1:
            profit_change=profit_change + (int(row[1])-int(rows_values[i-1][1]))
         #Finding Max and Min Profits
        if int(greatest_increase_row[1]) < int(row[1]):
            greatest_increase_row=row

        if int(greatest_decrease_row[1]) > int(row[1]):
            greatest_decrease_row=row  

    average_profit_loss= int(total_profit_loss /months_count)
    average_profit_change=int(profit_change/months_count)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: $ {average_profit_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_row[0]} $ {greatest_increase_row[1]}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_row[0]} $ {greatest_decrease_row[1]}")
  
  
    output_file = open("PyBank.txt","w") 
 
output_file.write("Financial Analysis"+ '\n') 
output_file.write("----------------------------"+ '\n')
output_file.write(f"Total Months: {months_count}"+ '\n')
output_file.write(f"Total: ${total_profit_loss}"+ '\n')
output_file.write(f"Average Change: ${average_profit_change}"+ '\n')
output_file.write(f"Greatest Increase in Profits: {greatest_increase_row[0]} $ {greatest_increase_row[1]}"+ '\n')
output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_row[0]} $ {greatest_decrease_row[1]}"+ '\n')
 
output_file.close() 

    