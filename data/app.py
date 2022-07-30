 
import csv
import imp
import random 

# field names 
fields = ['Learner gender', 'Teachers Gender', 'Teachers Age',
          'Community Outreach', "Next of kin has a degree", "Know Career path",
          "has access to internet at home", "learning material preferred", "type of school"] 
    
# data rows of csv file

gender = ["Male", "Female"]
# print(random.choice(gender))
    
# name of csv file 
filename = "data_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
    for i in range(1000):
        age = random.randint(24, 65)
        yes_no = random.choice(["YES", "NO"])
        type_of_matterial_prefarred = random.choice(["Books", "YouTube","Google search", "Teachers explanation", "peer to peer"])
        type_of_school = random.choice(["Model C", "Model B", "Model A"])
        rown = [[str(random.choice(gender)),str(random.choice(gender)) , age, yes_no, yes_no, yes_no, yes_no,type_of_matterial_prefarred , type_of_school]]
        csvwriter.writerows(rown)