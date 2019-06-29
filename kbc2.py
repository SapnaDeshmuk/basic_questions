question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options_list = [["Four", "Nine", "Seven", "Eight"],
	["Chandigarh", "Bhopal", "Chennai", "Delhi"]
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
	print options_list
	s=int (raw_input("enter a number"))
	if (solution_list[i==s]):