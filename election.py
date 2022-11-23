# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes =0
candidates = []
candidate_votes = {}
# {"name":"","votes":0}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        total_votes += 1
        candidate = row[2]
        #check if in candidate list
        if candidate not in candidates:
            candidates.append(candidate)

            #add to candidate votes
            candidate_votes[candidate] =0

        candidate_votes[candidate] +=1


print(f'Total Votes: {total_votes}')
print(f'We had {len(candidates)} candidates')
print(candidate_votes)

for candidate in candidates:
    print(candidate)
    print(f'Votes {round((candidate_votes[candidate] / total_votes)*100)}%')

