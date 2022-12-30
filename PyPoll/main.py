#first I need to create the import section bit
import os
import csv
#show where the file path is
csvlocation =os.path.join('.', 'Resources', 'election_data.csv')

with open(csvlocation, newline='') as csvfile:

    # this csv reader will have the delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    candidate_list = [candidate[2] for candidate in csvreader]
    
# have to calculate total votes, unique votes and put out the first candidate as the winner 
total_votes = len(candidate_list)
canditates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

# finally print the results, the screenshot showed it wanted 4 lots of "----" breaks 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")


#  like PyBank, when I print the final results and export to text i need to set my path again cause its a different file 
filepath = os.path.join('.', 'Resources', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditates_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)

