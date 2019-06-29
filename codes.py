user_input=intput("inter year")
if user_input <0:
	print "negative number" 
elif user_input>0 and user_input<=100:
	print "1 century"
elif user_input%100==0:
	print  user_input/100"century"
else:
	print user_input/100"century"

