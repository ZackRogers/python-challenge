import csv

f = open("analysis/election-analysis.txt", "w")

with open('Resources/election_data.csv') as csvFile:

    next(csvFile)
    csvRead = csv.reader(csvFile) 
    totalVotes = 0
    candidates = {}
    candidatesVotes = 0
    winner = 0
    for i, row in enumerate(csvRead):
        totalVotes += 1

        #If canadidate is not in List add them
        if(row[2] not in candidates):
            #Add candidate and first vote
            candidates[row[2]] = 1
        else:
            #Get candidates current votes
            candidatesVotes = candidates[row[2]]
            #Increment candidate votes
            candidatesVotes += 1
            #Update Dictionary
            candidates[row[2]] = candidatesVotes
    
#Create a Sorted Tuple with candidate Dictonary
sortedTuples = sorted(candidates.items(), key=lambda item: item[1], reverse = True)
#Add sorted Tuple to Dictionary
sortedDict = {k: v for k, v in sortedTuples}
#Get first key in the sorted Dictonary 
winner = next(iter(sortedDict))

#Output total votes
output = (
f'\nElection Results\n\
----------------------------\n\
Total Votes: {totalVotes}\n\
----------------------------\n')

#Add all candidates found with formated total votes to output
for key in sortedDict:
    output += key + ': ' + str("{:.3%}".format(candidates[key]/totalVotes)) + ' (' + str(candidates[key]) + ')\n' 

#Add winner to output
output += (
f'----------------------------\n\
Winner: {winner} \n\
----------------------------\n')

print(output)

f.write(output)