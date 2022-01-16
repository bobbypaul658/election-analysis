print("Hello World!")
print(type(3))
print(type(2019))
ballots = 1341
print(type(ballots))
print(type(73.81))
print(type('Hello World'))
print(type(True))

print("------------")
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16- 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
print("------------")
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / (2 - 4)))






counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[1])
print(counties[2])
print(counties[-1])
print(counties[-2])
print(counties[-3])

print("--------------")
print(len(counties))
print("--------------")
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
print(counties[1:3])
print("--------------")

counties.append("El Paso")
counties.insert(2, "El Paso")
print(len(counties))
print(counties)

counties.remove("El Paso")
print(len(counties))
print(counties)

counties.pop(3)
#counties.pop(-1)
print(counties)

print("-------Update-------")
counties[2] = "El Paso"
print(counties)
print("----------------------")



counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
print(counties)
counties.remove("Denver")
counties.insert(2,"Denver")
counties.append("Arapahoe")
print(counties)
print("----------------")


counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print("------------------")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict["Arapahoe"])
print(counties_dict["Denver"])
print(counties_dict["Jefferson"])
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print("---------------")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data[0]["county"])
print(voting_data[0].get("county"))
print(voting_data[0]["registered_voters"])
print(voting_data[0].get("registered_voters"))

voting_data.append({"county": "El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.pop(0)
voting_data.pop(0)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
print("------------------")

# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# print("-"* 100)
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# print("--------------")

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

x = 0
while x <= 5:
    print(x)
    x = x +1
print("---------------")

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)
print("---------------")

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
print("---------------")

for num in range(5):
    print(num)
print("---------------")

for i in range(len(counties)):
    print(counties[i])
print("---------------")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
print("------Keys------")

for county in counties_dict.keys():
    print(county)
print("---------------")

print("Values")
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

print("Items")
# for key, value in dictionary_name.items():
    # print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county, " county has ", voters, " registered voters ")

    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# tedious; try not to use this method very much. more efficient ways to do the process
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)import csv
 import os
 from pip._internal.models import candidate

 # Assign a variable to load a file from a path.
 file_to_load = os.path.join("Resources", "election_results.csv")
 # print(file_to_load)
 # Assign a variable to save the file to a path.
 file_to_save = os.path.join("analysis", "election_analysis.txt")

 # Initialize a total vote counter.
 total_votes = 0

 # Candidate options and candidate votes.
 candidate_options = []
 candidate_votes = {}

 # Challenge: County Options County Votes
 county_names = []
 county_votes = {}

 # Track the winning candidate vote count and percentage
 winning_candidate = ""
 winning_count = 0
 winning_percentage = 0

 # Challenge: Track the largest county voter turnout and its percentage
 largest_county_turnout = ""
 largest_county_vote = 0

 with open(file_to_load) as election_data:
     reader = csv.reader(election_data)

     # Read the header row.
     header = next(reader)

     # Loop each row in the CSV file.
     for row in reader:
         # Add to the total vote count.
         total_votes = total_votes + 1
         # Get the candidate name from each row.
         candidate_name = row[2]
         # Get the county name from each row.
         county_name = row[1]

         # If the candidate does not match any existing candidate
         # add it to the list
         if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
             candidate_options.append(candidate_name)
             # And begin tracking that candidate's voter count.
             candidate_votes[candidate_name] = 0
         # Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1

         # Challenge
         if county_name not in county_names:
             # Add it to the list of county
             county_names.append(county_name)

             # Begin tracking the county votes
             county_votes[county_name] = 0

         county_votes[county_name] += 1

 # Save the results to our text file.
 with open(file_to_save, "w") as txt_file:
     # Print the final vote count to the terminal.
     election_results = (
         f"\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"-------------------------\n"
         f"County Votes:\n"
     )
     print(election_results, end="")    
     # Save the final vote count to the text file.
     txt_file.write(election_results)

     # Challenge save final county vote count to text file
     for county in county_votes:
         # retreive vote count and percentage
         county_vote = county_votes[county]
         county_percent = int(county_vote)/int(total_votes) * 100
         county_results = (
             f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
         )
         print(county_results, end="")
         txt_file.write(county_results)

         # Determine winning vote count.
         if (county_vote > largest_county_vote):
             largest_county_vote = county_vote
             largest_county_turnout = county

     # Print the county with the largest turnout.
     largest_county_turnout = (
         f"-------------------------\n"
         f"Largest County Turnout {largest_county_turnout}\n"
         f"-------------------------\n"
     )
     print(largest_county_turnout)
     txt_file.write(largest_county_turnout)

     # Save the final candidate results to the text file.
     for candidate in candidate_votes:
         # Retrieve vote count and percentage.
         votes = candidate_votes[candidate]
         vote_percentage = int(votes)/int(total_votes) * 100
         candidate_results = (
             f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
         )

         # Print each candidate's voter count and percentage to the terminal.
         print(candidate_results)
         txt_file.write(candidate_results)

         # Determine winning vote count, winning percentage, and winning candidate.
         if(votes > winning_count) and (vote_percentage > winning_percentage):
             winning_count = votes
             winning_candidate = candidate
             winning_percentage = vote_percentage

     # Print the winning candidate's results to the terminal.
     winning_candidate_summary = (
         f"-------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"-------------------------\n"
         )
     print(winning_candidate_summary)