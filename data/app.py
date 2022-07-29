 
import csv 
    
# field names 
fields = ['Learner gender', 'Teachers Gender', 'Teachers Age',
          'Community Outreach', "Next of kin has a degree", "Know Career path",
          "has access to internet at home", "learning material preferred", "type of school"] 
    
# data rows of csv file

gender = ["Male", "Female"]
rown = [["male", "female", "40", "NO", "YES", "YES", "YES", "BOOKS", "MODEL C"]]
    
# name of csv file 
filename = "data_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
    for i in range(100):
    # # writing the data rows 
        csvwriter.writerows(rown)