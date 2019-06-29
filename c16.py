list1=[5,10,15,9,6,12,30,50,13,21]
i=0
count=0
new=[]
counter=0
old=[]
while i<=len(list1):
	if list1[i]%5==0:
		print count
		count=count+1
		new.append(count)
	else:
		print"5 se divisible nhi hai",list[i]
		counter=counter+1
	i=i+1
print new
	