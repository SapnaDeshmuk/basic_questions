user_input1=raw_input("enter the string:")
user_input2=raw_input("enter the string:")
i=0
j=0
a=len(user_input1)
b=len(user_input2)
while i<a:
	if user_input1[i]==user_input2[j] and a==b:
		print "anagram hain"
		break
		j=j+1
	i=i+1

else:
	print "anagram nahi hain"
