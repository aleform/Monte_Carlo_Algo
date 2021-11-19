import random
import numpy_financial as npf
initial=[4000,4500,4899,5000,5500]
final=[1500,2000,2449,3000,3500]
taxrate=0.31
waccblomb=0.03
NPVlist=[]
numero=1000000

def CountFrequency(my_list):
	freq = {}
	for item in my_list:
		if (round(item)) in freq:
			freq[round(item)] += 1
		else:
			freq[round(item)] = 1
	for key, value in freq.items():
		print ("% d : % d"%(key, value))
	expect=sum(k*v for k,v in freq.items())/numero
	print(round(expect))

for i in range(numero):

	intercashflow=[-467,761,1659,2282,3174,4372,340+2714]
	estri=random.random()
	estrf=random.random()
	result=[]

	if (estri<0.10):
		iniz=initial[0]
	elif (estri<0.30):
		iniz=initial[1]
	elif (estri<0.70):
		iniz=initial[2]
	elif (estri<0.90):
		iniz=initial[3]
	else:
		iniz=initial[4]

	intercashflow[0]=intercashflow[0]-iniz

	finalbv=0.5*iniz

	if (estri<0.10):
		fin=final[0]
	elif (estri<0.300):
		fin=final[1]
	elif (estri<0.70):
		fin=final[2]
	elif (estri<0.90):
		fin=final[3]
	else:
		fin=final[4]

	intercashflow[-1]=intercashflow[-1]+fin

	taxeffect=(finalbv-fin)*taxrate
	intercashflow[-1]=intercashflow[-1]+taxeffect

	NPV=npf.npv(waccblomb,intercashflow)
	due=(iniz,fin)

	result.append(due)
	#print(NPV)
	NPVlist.append(NPV)

CountFrequency(NPVlist)


	
