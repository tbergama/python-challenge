import csv
import sys

def pct_votes(votes, num_votes):
	return (votes/num_votes)*100




def main():
	csv_path = "election_data.csv"

	with open(csv_path) as csvfile:

		# Create csv.reader object
		csvreader = csv.reader(csvfile, delimiter=',')
		
		# Skip header
		next(csvreader)

		# Initialize dictionary to track votes
		votes_dict = {}
		num_votes = 0

		for row in csvreader:

			# Increment votes
			num_votes += 1

			# Add vote
			candidate = row[2]

			if candidate in votes_dict.keys():
				votes_dict[candidate] += 1
			else:
				votes_dict[candidate] = 1


		# Get winner
		winner = max(votes_dict, key=votes_dict.get)

		# Example output

		# Election Results
		# -------------------------
		# Total Votes: 3521001
		# -------------------------
		# Khan: 63.000% (2218231)
		# Correy: 20.000% (704200)
		# Li: 14.000% (492940)
		# O'Tooley: 3.000% (105630)
		# -------------------------
		# Winner: Khan
		# -------------------------

		print("Election results")
		print("-------------------------")
		print(f"Total Votes: {num_votes}")
		print("-------------------------")

		for c in votes_dict.keys():
			c_votes = votes_dict[c]
			print(f"{c}: {pct_votes(c_votes, num_votes):.3f}% ({c_votes})")

		print("-------------------------")
		print(f"Winner: {winner}")

		# Set standard out to a text file
		sys.stdout = open("./election_results.txt", "w")

		print("Election results")
		print("-------------------------")
		print(f"Total Votes: {num_votes}")
		print("-------------------------")

		for c in votes_dict.keys():
			c_votes = votes_dict[c]
			print(f"{c}: {pct_votes(c_votes, num_votes):.3f}% ({c_votes})")

		print("-------------------------")
		print(f"Winner: {winner}")


if __name__ == '__main__':
	main()
