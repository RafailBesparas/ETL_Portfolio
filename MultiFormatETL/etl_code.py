import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt" 

target_file = "transformed_data.csv" 

# process the data from csv
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

# process the data from json
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines = True)
    return dataframe

# process the data to xml
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name,  "height":height, "weight" : weight }])], ignore_index = True)
    return dataframe

# Function neede to identify which function to call on basis on the data file
def extract():
    extracted_data = pd.DataFrame(columns = ['name', 'height', 'weight']) # create an empty data frame to hold extracted data

    # process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index = True)
    
    # Process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 

    # process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 

    return extracted_data

# transform the data to approprate form
def transform(data):

    'Convert inches to meters and round of to two decimal places'

    data['height'] = round(data.height * 0.0254,2)

    'Convert pounds to kilograms and round off to two decimal places'

    data['weight'] = round(data.weight * 0.45359237, 2)

    return data

# loading and logging

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

# create a function for logging the messages for start and finish of each process
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timespamp
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')


# Testing the ETL operations and log the progess for each task

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 

