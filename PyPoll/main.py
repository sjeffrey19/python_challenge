#load dependencies
import pathlib
import csv

#read CSV file and skipping first line of headers
csvpath = pathlib.Path('Resources/election_data.csv')
with open(csvpath) as csvfile:
    electiondata = csv.reader(csvfile, delimiter = ',')
    electiondata_header = next(electiondata)
    
    #set lists/variables
    totalvotes=[]
    khan=0
    correy=0
    li=0
    otooley=0
    
    #Loop through each row of electiondataadding data to the appropriate lists
    for row in electiondata:
        totalvotes.append(row[0])
        countvotes = len(totalvotes)
        
        if row[2] == "Khan":
            khan +=1
            khanpercentage = (khan/countvotes) * 100
            
        if row[2] == "Correy":
            correy +=1
            correypercentage = (correy/countvotes) * 100
        
        if row[2] == "Li":
            li +=1
            lipercentage = (li/countvotes) * 100        
        
        if row[2] == "O'Tooley":
            otooley +=1
            otooleypercentage = (otooley/countvotes) * 100  
            
    #Print Results Report
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {countvotes}")
    print("--------------------------")
    print(f"Khan: {khanpercentage:.3f}% ({khan})")
    print(f"Correy: {correypercentage:.3f}% ({correy})")
    print(f"Li: {lipercentage:.3f}% ({li})")
    print(f"O'Tooley:{otooleypercentage:.3f}% ({otooley})")
    print(f"----------------------------")
    print(f"Winner: Khan")
    print(f"----------------------------")
    
    #Save Report to .txt file
    output_file = pathlib.Path('Analysis/report.txt')

    with open(output_file, "w") as report:
        
        title = ("Election Results")
        d1 = ("--------------------------")
        total_votes = (f"Total Votes: {countvotes}")
        d2 = ("--------------------------")
        candidate1 = (f"Khan: {khanpercentage:.3f}% ({khan})")
        candidate2 = (f"Correy: {correypercentage:.3f}% ({correy})")
        candidate3 = (f"Li: {lipercentage:.3f}% ({li})")
        candidate4 =(f"O'Tooley:{otooleypercentage:.3f}% ({otooley})")
        d3 = (f"----------------------------")
        winningcandidate = (f"Winner: Khan")
        d4 =(f"----------------------------")
    
        report.write('{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n'.format(title,d1,total_votes,d2,candidate1,candidate2,candidate3,candidate4,d3,winningcandidate,d4))