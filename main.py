import pandas as pd
import csv
import statistics

df = pd.read_csv("StudentsPerformance.csv")
gender_list = df["gender"].to_list()

#Find the mean
gender_mean = statistics.mean(gender_list)

#Finding the SD
gender_stdev = statistics.stdev(gender_list)
print("\nStandard Deviation of gender is:\n", gender_stdev)

#Finding SD for 1, 2 and 3 sigma
gender_first_std_start, gender_first_std_end = gender_mean - gender_stdev, gender_mean + gender_stdev
gender_second_std_start, gender_second_std_end = gender_mean - (2*gender_stdev), gender_mean + (2*gender_stdev)
gender_third_std_start, gender_third_std_end = gender_mean - (3*gender_stdev), gender_mean + (3*gender_stdev)

gender_list_of_data_within_1_std = [result for result in gender_list if result > gender_first_std_start and result < gender_first_std_end]
gender_list_of_data_within_2_std = [result for result in gender_list if result > gender_second_std_start and result < gender_second_std_end]
gender_list_of_data_within_3_std = [result for result in gender_list if result > gender_third_std_start and result < gender_third_std_end]

#Printing all info
print("{}% of data for gender lies within 1 standard deviation".format(len(gender_list_of_data_within_1_std)*100.0/len(gender_list)))
print("{}% of data for gender lies within 2 standard deviation".format(len(gender_list_of_data_within_2_std)*100.0/len(gender_list)))
print("{}% of data for gender lies within 3 standard deviation".format(len(gender_list_of_data_within_3_std)*100.0/len(gender_list)))