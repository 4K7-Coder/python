a = list(map(int, input("Enter some numbers : ").split()))
print("Input: ",a)
print("Output: ",end="")
for i in a:
	if i>0:
		print (i,end=", ")