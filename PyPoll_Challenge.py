# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Challenge: Counties' options and votes.
county_names = []
county_votes = {}

# Winning Candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenge: Track the largest county voter turnout and percentage.
largest_county_turnout = ""
largest_county_votes = 0

# Open the eleciton results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the toal vote count.
        total_votes += 1
    
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Get the county name for each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Challenge: If county does not match any existing county add it to the county list.
        if county_name not in county_names:
            # Add the county name to the county list.
            county_names.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    #Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"\nCounty Votes:\n"
        )
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Challenge Save final county vote count to text file.
        for county in county_votes:
            # Retrieve vote count of a county and percentage.
            county_vote = county_votes[county]
            county_percent = float(county_vote) / float(total_votes) * 100

            county_results = (
                f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
            )
            print(county_results, end="")
            txt_file.write(county_results)

            # Determine winning vote count.
            if (county_vote > largest_county_votes):
                largest_county_votes = county_vote
                largest_county_turnout = county
            
        # Print the county with the largest turnout.
        largest_county_turnout = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"-------------------------\n"
        )
        print(largest_county_turnout)
        txt_file.write(largest_county_turnout)
            
        for candidate in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
            )

            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)
            # Determine winning vote count and candidate.
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = vote percentage.
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage
        
        #Print the winning candidate's results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"
        )
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)