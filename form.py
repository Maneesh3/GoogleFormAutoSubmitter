import requests
import random
import time

all_names = [

]   # fill this list with names 

_FORM_LINK = ' '  # google form url without '/viewform' at end
url = _FORM_LINK + '/formResponse'

user_agent = {'Referer':_FORM_LINK + '/viewform',
			  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        

AGE =    [16, 17, 18, 19, 20, 21, 22, 23]
WT_AGE = [0.05,0.1,0.25,0.25,0.1,0.1,0.1,0.05]

Q1_r = {
	1:'Basically every day',
	2:'A few times a month',
	3:'Not at all'
}
Q1 = [1,2,3]
WT_Q1 = [0.7,0.25,0.05]


Q2_r = {
	1:'Yes',
	2:'No'
}
Q2 = [1,2]


Q3_r = {
	1:'Good',
	2:'Fair',
	3:'Poor'
}
Q3 = [1,2,3]


Q4_r = {
	1:'Completely',
	2:'Partially',
	3:'Not at all'
}
Q4 = [1,2,3]
WT_Q4 = [0.7,0.23,0.07]


Q5_r = {
	1:'Yes',
	2:'No'
}
Q5 = [1,2]
WT_Q5 = [0.7,0.3]

def get_age():
	return random.choices(population=AGE,weights=WT_AGE,k=1)[0]

def get_Q1():
	return random.choices(population=Q1,weights=WT_Q1,k=1)[0]
	
def get_Q2(age):
	if(age<18):
		return 2
	elif(age>=19):
		return random.choices(population=Q2,weights=[0.75,0.25],k=1)[0]
	else:
		return random.choices(population=Q2,weights=[0.5,0.5],k=1)[0]
	
def get_Q3(age):
	if(age<18):
		return 1
	elif(age>=19):
		return random.choices(population=Q3,weights=[0.1,0.8,0.1],k=1)[0]
	else:
		return random.choices(population=Q3,weights=[0.6,0.35,0.5],k=1)[0]

def get_Q4():
	return random.choices(population=Q4,weights=WT_Q4,k=1)[0]

def get_Q5():
	return random.choices(population=Q5,weights=WT_Q5,k=1)[0]


for n in all_names:
	print("\n=====\n")
	age_r = get_age()
	print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
		n,
		str(age_r),
		str(Q1_r[get_Q1()]),
		str(Q2_r[get_Q2(age_r)]),
		str(Q3_r[get_Q3(age_r)]),
		str(Q4_r[get_Q4()]),
		str(Q5_r[get_Q5()])
	))
	form_data = {			
		'entry.850561468':n,
		'entry.1120506989':str(age_r),
		'entry.1680412405':str(Q1_r[get_Q1()]),
		'entry.372544484':str(Q2_r[get_Q2(age_r)]),
		'entry.1841766524':str(Q3_r[get_Q3(age_r)]),
		'entry.1026186278':str(Q4_r[get_Q4()]),
		'entry.848226990':str(Q5_r[get_Q5()]),
		'draftResponse':[],
		'pageHistory':0
	}
			# these entry.<id> are be different for each form, send a sample response to find out from Network tab in browser
	r = requests.post(url, data=form_data, headers=user_agent)
	print(r)	# if response status code is 200, then success
	#print(r.content)
	time.sleep(0.5)

