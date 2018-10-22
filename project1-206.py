import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	inFile = open(file, "r")
	line_list = inFile.readlines()
	dictList = []
	for x in range(1,len(line_list)):
		line = line_list[x]
		data_dict = {}
		values = line.split(",")
		firstName = values[0]
		lastName = values[1]
		email = values[2]
		Class = values[3]
		birthday = values[4]

		data_dict['First'] = firstName
		data_dict['Last'] = lastName
		data_dict['Email'] = email 
		data_dict['Class'] = Class
		data_dict['DOB'] = birthday
		dictList.append(data_dict)          

		line = inFile.readline()
	return dictList


def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	
	sorted_col = sorted(data, key=lambda data_dict: data_dict[col])
	dic = sorted_col[0]
	return dic['First'] + ' ' + dic['Last']
	

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	
	class_dict = {}
	for dict in data:
		grade = dict['Class']
		class_dict[grade] = class_dict.get(grade,0) + 1

	sorted_class = sorted(class_dict.items(), key=lambda t: t[1], reverse = True)

	return sorted_class


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	month_dict = {}
	for dict in a:
		birthday = dict["DOB"]
		split_data = birthday.split("/")
		month = split_data[0]
		month_dict[month] = month_dict.get(month, 0) + 1

	sorted_month = sorted(month_dict.items(), key=lambda m: m[1], reverse = True)
	tuple_month = sorted_month[0]

	return int(tuple_month[0])

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	output = open(fileName, 'w')
	sorted_col = sorted(a, key=lambda data_dict: data_dict[col])
	for dict in sorted_col:
		output.write(dict['First'] + ',' + dict['Last'] + ',' + dict['Email'] + '\n')
	output.close()                                                  #results in the same as output.csv, just a weird difference in character comparison

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
