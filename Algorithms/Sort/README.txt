The assignment1 contains 6 files
-----------------------------------
1. insertsort.py
2. mergesort.py
3. data.txt
4. insertTime.py
5. mergeTime.py
6. README.txt
-----------------------------------

The purpose: 

	insertsort.py and mergesort.py are designed to sort numbers from a file called data.txt. You can just need to change the value of input in data.txt file and run it in python 3.8.3 or in OSU engineer sever.
	
	

--------------------------------------

How to run a code:
	
	Running in local is acceptable. I am using python 3.7. That works. It can be run by OSU sever as well.
	How to run in OSU sever?
	1. Download MobaXterm
	2. Use ssh to connect OSU sever. The address is flip.engr.oregonstate.edu
	3. login your OSU account
	4. upload all files in the zip file.
	5. check whether it is running in the same folder. If not, use cd command to move in the folder.
	6. type python "name of the file".py and it can be run directly. For example: python insertsort.py


--------------------------------------
Something to keep in mind:


	For mergesort.py and insertsort.py:


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

	For insertTime.py and mergeTime.py:

	Just type python insertTime.py and python mergeTime.py then we can get the results. But, it would not equal to my results directly. Please make sure run the codes as possible as you could and average them. They would be similar