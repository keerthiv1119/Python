for row in range(6):
	for col in range(7):
		if(row==0 and col%3!=0):
			print("I",end="")
		if(row==1 and col%3==0):
			print("L",end="")
		if(row-col==2) or (row+col==8):
			print("U",end=" ")
		else:
			print(end=" ")
	print()
