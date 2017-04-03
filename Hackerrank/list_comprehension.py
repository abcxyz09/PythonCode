if __name__ == '__main__':
	'''x = int(raw_input())
	y = int(raw_input())
	z = int(raw_input())
	n = int(raw_input())'''
	x,y,z,n = [int(raw_input()) for t in range(4)]
	list = [[i,j,k] for i in range(x+1) for j in range(y+1) 
	       for k in range(z+1) if (i+j+k)!=n if i == 0 and j == 0]
	'''for i in range(x+1):
		for j in range(y+1):
			for k in range(z+1):
				if (i+j+k) != n:
					list.append([i,j,k])'''

	print list 