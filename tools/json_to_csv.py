import os
import csv 
import json 

current_dir = os.getcwd()
csvFilePath = os.path.join(current_dir, 'filename.csv')
jsonFilePath = os.path.join(current_dir, 'filename.json')

def json_to_csv(jsonFilePath, csvFilePath):

    with open(jsonFilePath, encoding='utf-8') as json_file:
        data = json.load(json_file)

    users = data['users']
 
    # now we will open a file for writing
    data_file = open(csvFilePath, 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for user in users:
        if count == 0:
    
            # Writing headers of CSV file
            header = user.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(user.values())
    
    data_file.close()


json_to_csv(jsonFilePath, csvFilePath)