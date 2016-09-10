#!/usr/bin/env python
# coding=utf-8
# filename : recommendations.py
# author : Chase
# update : 2016/09/10

from math import sqrt

critics={'Cathy':{'a':2.5,'b':3.5,'c':3,'d':3.5,'e':2.5,'f':3},
	'Sophie':{'a':3,'b':3.5,'c':1.5,'d':5,'e':1.5,'f':3},
	'Susie':{'a':2.5,'b':3,'d':3.5,'f':4},
	'Antonio':{'b':3.5,'c':3,'d':4,'e':2.5,'f':4.5},
	'Marco':{'a':3,'b':4,'c':2,'d':3,'e':2,'f':3},
	'Jack':{'a':3,'b':4,'d':5,'e':3.5,'f':3},
	'Leo':{'b':4.5,'d':4,'e':1.0}
}

'''
返回一个有关person1与person2的基于距离的相似度评价
'''
def sim_distance(prefs, person1, person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	if len(si)==0: return 0

	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item], 2)
						for item in prefs[person1] if item in prefs[person2]])
	return 1/(1+sqrt(sum_of_squares))

'''
返回一个person1与person2的皮尔逊相关系数
'''
def sim_pearson(prefs, person1, person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	# get the count of list
	n=len(si)

	# if nothing in common return 1
	if n==0: return 1

	sum1=sum([prefs[person1][it] for it in si])
	sum2=sum([prefs[person2][it] for it in si])

	sum1Sq=sum([pow(prefs[person1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[person2][it],2) for it in si])

	pSum=sum([prefs[person1][it]*prefs[person2][it] for it in si])

	# calculate pearson relation
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0

	r=num/den
	return r


'''
Return the toppest match
'''
def topMatches(prefs, person, n=5, similarity=sim_pearson):
	scores = [(similarity(prefs,person,other),other)
				for other in prefs if other!=person]
	# sort the scores
	scores.sort()
	scores.reverse()
	return scores[0:n]


'''
'''
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		if other==person: continue
		sim=similarity(prefs,person,other)

		if sim<=0: continue
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item]==0:
				totals.setdefault(item, 0)
				totals[item]+=prefs[other][item]*sim
				simSums.setdefault(item,0)
				simSums[item]+=sim
	rankings=[(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings
