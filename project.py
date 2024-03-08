# #import csv
# #import numpy as np


# # Creating lists to store values from the file
# age_list = []
# sex_list = []
# bmi_list = []
# children_list = []
# smoker_list = []
# region_list = []
# charges_list = []

# ins_dict = {}
# #Importing data and storing it to a dictionary
# with open('insurance.csv') as ins_file:
#     ins_data = csv.DictReader(ins_file)
#     for x in ins_data:
#         age_list.append(int(x['age']))
#         sex_list.append(x['sex'])
#         bmi_list.append(float(x['bmi']))
#         children_list.append(int(x['children']))
#         smoker_list.append(x['smoker'])
#         region_list.append(x['region'])
#         charges_list.append(float(x['charges']))
#     # for x in range(len(age_list)):
#     #     ins
# #Exploration 1: Determining average insurance costs using NumPy
# avg_age = np.mean(age_list)
# print("The average age of the stored users is: {}".format(round(avg_age)))
# #1a: Determining average costs by sex
# #1b: Determining average costs by region
# #1c: Determining average costs for smoker/non-smoker

# #Exploration 2: Using NumPy to calculate averages, medians and other percentage statistics of other columns

# #This is a new comment. Commit!