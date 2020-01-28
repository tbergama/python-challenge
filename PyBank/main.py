import csv
import sys

def main():
	csv_path = "budget_data.csv"

	with open(csv_path) as csvfile:
		
		# Create csv.reader object
		csvreader = csv.reader(csvfile, delimiter=',')
		
		# Skip header
		next(csvreader)

		# Intialize stats using first line
		first_row = next(csvreader)
		num_months = 1
		total_profit = int(first_row[1])
		max_increase = first_row
		max_decrease = first_row

		# print(num_months)
		# print(total_profit)
		# print(max_increase)
		# print(max_decrease)

		for row in csvreader:
			num_months += 1  # increment number of months
			total_profit += int(row[1])  # add value to total profit

			# Update greatest increase if necessary
			if int(max_increase[1]) < int(row[1]):
				max_increase = row

			# Update greatest decrease if necessary
			if int(max_decrease[1]) > int(row[1]):
				max_decrease = row

		# Print results to console
		print("Financial Analysis")
		print("----------------------------")
		print(f"Total Months: {num_months}")
		print(f"Total: ${total_profit}")
		print(f"Average Change: ${total_profit/num_months}")
		print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
		print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")

		# Set standard out to a text file
		sys.stdout = open("./financial_analysis.txt", "w")

		# Reprint results
		print("Financial Analysis")
		print("----------------------------")
		print(f"Total Months: {num_months}")
		print(f"Total: ${total_profit}")
		print(f"Average Change: ${total_profit/num_months}")
		print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
		print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")


if __name__ == '__main__':
	main()
