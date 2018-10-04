import numpy as np
import sys
#sys is a module which gives us access to the command module. useful when we have a module that
# has prior behavior and we want to change it optionally when the program runs

#define a function that returns a value
def expo(x):
	return np.exp(x)	#return the np e^x function
	
#define a subroutine that does not return a value but does do some other stuff
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo function
		
#define a main function
def main():
	n=10 #provides a default value for n
	
	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if an argument was provided, use it for n
		
	show_expo(n) 		#call the show_expo subroutine
	
#run the main function
if __name__ == "__main__":
	main()
	
#Once this program is executed, in the terminal we can type any integer after the
#program in order to change how many values of n we look at
#Into the terminal:

#cd Desktop
#python3 functions.py n
						#where n is some integer that we want this program to loop that
						#many time