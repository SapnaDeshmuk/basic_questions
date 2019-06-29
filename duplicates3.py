n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
new_list=[]
count=0
while i<len(n):
	j=1
	while j<len(n):
		if n[i]==n[j]:
			if count>=1:
				if n[i] not in new_list:	
					new_list.append(n[i])
			
	i=i+1
print new_list