import csv
import numpy as np

#Importing Data and storing it to a dictionary.
with open('insurance.csv') as ins_file:
    ins_data = csv.DictReader(ins_file)
    for x in ins_data:
        print(x)
    #Exploration time!
    # First, determining average age, bmi and charges using NumPy. When using the list comprehension, I changed data type to be numerical so it works with NumPy.
    age_list = [int(x['age']) for x in ins_data]
    avg_age = np.mean(age_list)
    bmi_list = [x['bmi'] for x in ins_data]
    print(bmi_list)
    #avg_bmi = np.mean(bmi_list)
    charges_list = [float(x['charges']) for x in ins_data]
    #avg_charges = np.mean(charges_list)
    print('The average age of the people stored in this data set is: {}'.format(round(avg_age)))
    #print('The average BMI of the people stored in this data set is: {}'.format(round(avg_bmi, 2)))
    #print('The average charge value stored in this data set is: ${}'.format(round(avg_charges, 2)))