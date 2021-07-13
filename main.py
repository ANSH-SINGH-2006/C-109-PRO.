import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

writingScore= df["writing score"].tolist()
mathScore= df["math score"].tolist()
readScore= df["reading score"].tolist()

mean= statistics.mean(writingScore)
median=statistics.median(writingScore)
mode=statistics.mode(writingScore)

mean2= statistics.mean(mathScore)
median2=statistics.median(mathScore)
mode2=statistics.mode(mathScore)

mean3= statistics.mean(readScore)
median3=statistics.median(readScore)
mode3=statistics.mode(readScore)

print("Mean of the writing scores is {}".format(mean2))
print("Median of the writing scores is {}".format(median2))
print("Mode of the writing scores is {}".format(mode2))

print("..............................................")

print("Mean of the math scores is {}".format(mean))
print("Median of the math scores is {}".format(median))
print("Mode of the math scores is {}".format(mode))

print("..............................................")

print("Mean of the reading scores is {}".format(mean3))
print("Median of the reading scores is {}".format(median3))
print("Mode of the reading scores is {}".format(mode3))

print("..............................................")
print("..............................................")

std_dev=statistics.stdev(writingScore)
print("Standard Deviation of the writing scores is {}".format(std_dev))

first_std_dev_start, first_std_dev_end= mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end= mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean-(3*std_dev), mean+(3*std_dev)

list_of_data_within_1_std_dev= [result for result in writingScore if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev= [result for result in writingScore if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_3_std_dev= [result for result in writingScore if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(writingScore)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(writingScore)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(writingScore)))

print("..............................................")

std_dev=statistics.stdev(mathScore)
print("Standard Deviation of the math scores is {}".format(std_dev))

first_std_dev_start, first_std_dev_end= mean2-std_dev, mean2+std_dev
second_std_dev_start, second_std_dev_end= mean2-(2*std_dev), mean2+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean2-(3*std_dev), mean2+(3*std_dev)

list_of_data_within_1_std_dev= [result for result in mathScore if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev= [result for result in mathScore if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_3_std_dev= [result for result in mathScore if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(mathScore)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(mathScore)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(mathScore)))

print("..............................................")

std_dev=statistics.stdev(readScore)
print("Standard Deviation of the reading scores is {}".format(std_dev))

first_std_dev_start, first_std_dev_end= mean2-std_dev, mean2+std_dev
second_std_dev_start, second_std_dev_end= mean2-(2*std_dev), mean2+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean2-(3*std_dev), mean2+(3*std_dev)

list_of_data_within_1_std_dev= [result for result in readScore if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev= [result for result in readScore if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_3_std_dev= [result for result in readScore if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(readScore)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(readScore)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(readScore)))