"""
/***
Author: Dinesh Kalidindi
Problem Name: Sherlock and Date ( To Find Previous Date)
Submission Url : http://www.hackerearth.com/submission/424182/
**/"""

months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
t=int(raw_input())
for i in range(t):
	date=raw_input().split()
	dd=int(date[0])
	mm=date[1]
	yy=int(date[2])
	if dd!=1:
		p_dd=dd-1
		print str(p_dd)+" "+mm+" "+str(yy)
	elif dd==1 and mm=="May" or mm=="July" or mm=="October" or mm=="December":
		p_dd=30
		mm_i=months.keys()[months.values().index(mm)]
		p_mm_i=mm_i-1
		p_mm=months[p_mm_i]
		p_yy=yy
		print str(p_dd)+" "+p_mm+" "+str(p_yy)
	elif dd==1 and mm=="February" or mm=="April" or mm=="June" or mm=="August" or mm=="September" or mm=="November" or mm=="January":
		p_dd=31
		if mm=="January":
			p_mm="Decemeber"
			p_yy=yy-1
		else:
			mm_i=months.keys()[months.values().index(mm)]
			p_mm_i=mm_i-1
			p_mm=months[p_mm_i]
			p_yy=yy
		print str(p_dd)+" "+p_mm+" "+str(p_yy)
	elif mm=="March":
		p_mm="February"
		p_yy=yy
		if ((yy%4==0 and yy%100!=0) or (yy%400==0)):
			p_dd=29
		else:
			p_dd=28
		print str(p_dd)+" "+p_mm+" "+str(p_yy)
