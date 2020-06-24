# import Modules
import os
import csv
# placeholders for month, profit/loss, and profit/loss change
candidate = [] # store a complete list of candidates who received votes
names = [] # stroe all the names
vote_count =[] # store vote count for each candidate
percent=[] # store the percentage of votes each candidate won



# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis","election_result.txt")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Loop through each row, grab each field and store in a new list
    for row in csvreader:
        names.append(row[2])
    
    # total number of votes
    total=int(len(names))

    # store candidate names in a list without deplicates
    [candidate.append(i) for i in names if i not in candidate]
    
    # calculate vote count and vote percentage for each candidate
    for i in range(len(candidate)):
        vote_count.append(names.count(candidate[i]))
        percent.append(int(vote_count[i])/total)
    
    # find the winner's name
    winner=candidate[vote_count.index(max(vote_count))]

# create strings for printing result
str1= f"Election Results\n"             \
      f"-------------------------\n"    \
      f"Total Votes: {total:,.0f}\n"    \
      f"-------------------------\n"

# for i in range(len(candidate)):
    # output2=(f"{candidate[i]}: {percent[i]:.3%} ({vote_count[i]:,.0f})")
    # print(output2)

str2 = [f"{candidate[i]}: "
         f"{percent[i]:.3%} "
         f"({vote_count[i]:,.0f})\n"
         for i in range(len(candidate))]
    

str3= f"-------------------------\n"   \
      f"Winner: {winner}\n"            \
      f"-------------------------\n"  

# one way to print the output 
output1=(f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total:,.0f}\n"
        f"-------------------------\n"
        f"{''.join(str2)}"
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
# print (output1)

# another way to print the output
output2=str1+f"{''.join(str2)}"+str3

print(f"\n{output2}\n")

with open(file_to_output, "w") as txt_file:
     txt_file.write(output2)