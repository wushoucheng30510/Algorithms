The assignment2 contains 4 files
-----------------------------------
1. mergesort3.py
2. data.txt
3. mergeTime3.py
4. README.txt
-------------------------------------
Language: [python]
-------------------------------------
Running command: python mergesort3.py
		 python mergeTime3.py
-------------------------------------








Notes:

The purpose: 

	mergesort.py are designed to sort numbers from a file called data.txt. You can just need to change the value of input in data.txt file and run it in python 3.8.3 or in OSU engineer sever.
	
	

--------------------------------------

How to run a code:
	
	Running in local is acceptable. I am using python 3.7. That works. It can be run by OSU sever as well.
	How to run in OSU sever?
	1. Download MobaXterm
	2. Use ssh to connect OSU sever. The address is flip.engr.oregonstate.edu
	3. login your OSU account
	4. upload all files in the zip file.
	5. check whether it is running in the same folder. If not, use cd command to move in the folder.
	6. type python "name of the file".py and it can be run directly. For example: python mergesort.py


--------------------------------------
Something to keep in mind:


	For mergesort.py:


	The sturture of data.txt is like:	
	5 3 2 8 1 2
	3 100 50 101

	(Each line is a list of array which we neeed to sort. The first number of each line is telling how many numbers should be sorted.)	
	
	There are three other things that we need to keep in mind. 
	First, at the end of each line, we cannot type anything. It includes a space.
	Second, the format like:
	5 3 2 8 1 2

	3 100 50 101
	
	is not allowed. Leaving a line before next line is not allowed.
	Third, if the first number of each line is not correct. The program would show a exception.


	--------------------------------------------------------------------------------------

	For mergeTime3.py:

	Just type python python mergeTime3.py then we can get the results. But, it would not equal to my results directly. Please make sure run the codes as possible as you 	could and average them. They would be similar