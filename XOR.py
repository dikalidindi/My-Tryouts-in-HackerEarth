"""
Coding Attempt : Dinesh Kalidindi
submission Url : http://www.hackerearth.com/submission/426156

Problem Statement:

You are given an array A1,A2...AN. You have to tell how many pairs (i, j) exist such that 1 . i < j . N and Ai XOR Aj is odd.

Input and Output
First line T, the number of testcases. Each testcase: first line N, followed by N integers in next line. For each testcase, print the required answer in one line.

Constraints
1 . T . 10
1 . N . 105
0 . Ai . 109 

Explanation

For XOR of two numbers to be odd it is necessary that one number should be even and other should be odd.
So for getting the numbers of pairs you can make two counters

    c_even : for counting even numbers
    c_odd : for counting odd numbers

Hence number of pairs will be = c_even*c_odd
"""
t=int(raw_input())
for i in range(t):
	arr_len=int(raw_input())
	del arr_len
	numbers=map(int,raw_input().split())
	c_even=0
	c_odd=0
	for number in numbers:
		if number%2==1:
			c_odd+=1
		else:
			c_even+=1
	print c_even*c_odd
	
