#Iterative way

'''1.Start pointer pointing the first and end pointer pointing last element.
   2.swap the values of pointers.
   3.Start increments and end decrements. 

   (In-place reversal)'''

def reverse(arr):
	(start,end)=(0,len(arr)-1)
	while end>=start:
		(arr[start],arr[end])=(arr[end],arr[start])
		start+=1
		end-=1

	return arr


#Recursive way

'''Same thing in recursive fashion.'''

def reverse_rec(arr,start,end):
	if start>=end:
		return

	(arr[start],arr[end])=(arr[end],arr[start])
	reverse_rec(arr,start+1,end-1)
	return arr

if __name__=='__main__':

	l=['A','R','I']
	l=reverse_rec(l,0,len(l)-1)
	print(l)