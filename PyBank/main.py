#Dependencies
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Variables/lists to hold data
month = 0
cash = 0
previous = 0
diff_list = []
month_list = []
#open the csv file, read headers
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")

#Loop Through data
    for row in csv_reader:
        month += 1 #adds up all the months
        current = int(row[1]) 
        cash += current #sums the cash
        month_list.append(row[0]) #add a new month to the end of the months_list
        #calculate the difference in profit/loss bewteen each month
        if previous != 0: # if the pervious month is not equal to 0
            difference = current - previous #then calculate the difference by taking the current difference subtracting the pervious 
            previous = current #the previous difference is the current differnce, this will give us the change for each month
        else:
            difference = 0 #if the difference is 0 then the pervious is 0 the previous difference is the current amount 
            previous = current  
        diff_list.append(difference) #add the differences from each month to the end of the diff_list
    #find the average change of profit/lost between each month    
    average = round(sum(diff_list) / (month - 1),2) 

#locate greatest increase/decrease in profits
greatest_increase = max(diff_list)
greatest_decrease = min(diff_list)

#locate months of greatest increase/decrease in profits
greatest_month_inc = diff_list.index(greatest_increase)
greatest_month_dec = diff_list.index(greatest_decrease)

    
#get month from index values
month_greatest = month_list[greatest_month_inc]
month_lowest = month_list[greatest_month_dec]

#Summary table to terminal
print("")
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {month}")
print(f"Total: ${cash}")
print(f"Average Change: $ {average} ")
print(f"Greatest Increase in Profits: {month_greatest} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_lowest} (${greatest_decrease})")
print()


#export to a text file
analysis = os.path.join("Analysis", "PyBank_anaylsis.txt") #sets path & names file
with open(analysis, "w") as output:

    output.write("Financial Analysis\n")
    output.write("-----------------------\n")
    output.write(f"Total Months: {month}\n")
    output.write(f"Total: ${cash}\n")
    output.write(f"Average Change: $ {average}\n")
    output.write(f"Greatest Increase in Profits: {month_greatest} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {month_lowest} (${greatest_decrease})\n")

