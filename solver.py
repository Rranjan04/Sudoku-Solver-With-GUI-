# Backtracking Algorithm
def print_board(bo):
	for i in range(len(bo)):
		if i%3==0 and i!=0:
			print('- - - - - - - - - - - - - ')
		for j in range(len(bo[0])):
			if j%3==0 and j!=0:
				print(' | ',end="")

			if(j==8):
				print(bo[i][j])
			else:
				print(str(bo[i][j]),end=" ")	
def solve(bo):
	help(bo)
	print_board(bo)

def help(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if(bo[i][j]==0):
				# empty cell
				for d in range(1,10):
					if(isValid(bo,i,j,d)):
						bo[i][j] = d;
						if(help(bo)):
							return True;
						else:
							bo[i][j] = 0;
				return False
	return True

def isValid(bo,r,c,digit):
	for i in range(9):
		if(bo[i][c]==digit):
			 return False;
		if(bo[r][i]==digit):
			return False;
		if(bo[3*(int(r/3))+(int)(i/3)][3*(int(c/3))+i%3]==digit):
			return False;
	return True;

