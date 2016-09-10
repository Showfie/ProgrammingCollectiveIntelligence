#!/usr/bin/env python
# coding=utf-8
# filename : treepredict.py
# author : Chase
# update : 2016/09/10

#来源网站	| 	位置	| 	是否阅读FAQ	 |	浏览网页数 	| 	选择服务类型	|

my_data=[['slashdot','USA','yes',18,'None'],
['google','France','yes',23,'Premium'],
['digg','USA','yes',24,'Basic'],
['kiwitobes','UK','no',21,'Premium'],
['google','UK','no',21,'Premium'],
['(direct)','New Zealand','no',12,'None'],
['(direct)','UK','no',21,'Basic'],
['google','USA','no',24,'Premium'],
['slashdot','France','yes',19,'None'],
['digg','USA','no',18,'None'],
['google','UK','no',19,'None'],
['kiwitobes','UK','no',19,'Basic'],
['digg','New Zealand','yes',12,'Basic'],
['google','UK','yes',18,'Basic'],
['kiwitobes','France','yes',19,'Basic']]

class decisionnode:
	def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
		self.col=col
		self.value=value
		self.results=results
		self.tb=tb
		self.fb=fb


# 对树进行训练
# CART(Classification and Regression Trees)
def divideset(rows,column,value):
	split_function=None
	if isinstance(value,int) or isinstance(value,float):
		split_function=lambda row:row[column]>=value
	else:
		split_function=lambda row:row[column]==value

	set1=[row for row in rows if split_function(row)]
	set2=[row for row in rows if not split_function(row)]
	return (set1,set2)

def uniquecounts(rows):
	results={}
	for row in rows:
		r=row[len(row)-1]
		if r not in results: results[r]=0
		results[r]+=1
	return results


'''
基尼不纯度
'''
def giniimpurity(rows):
	total=len(rows)
	counts=uniquecounts(rows)
	imp=0
	for k1 in counts:
		p1=float(counts[k1])/total
		for k2 in counts:
			if k1==k2: continue
			p2=float(counts[k2])/total
			imp+=p1*p2
	return imp

'''
熵Entropy=p(x)log(p(x))
'''
def entropy(rows):
	from math import log
	log2=lambda x:log(x)/log(2)
	results=uniquecounts(rows)

	ent=0.0
	for r in results.keys():
		p=float(results[r])/len(rows)
		ent=ent-p*log2(p)
	return ent


def buildtree(rows,scoref=entropy):
	if len(rows)==0: return decisionnode()
	current_score=scoref(rows)

	best_gain=0.0
	best_criteria=None
	best_sets=None

	column_count=len(rows[0])-1
	for col in range(0, column_count):
		column_value={}
		for row in rows:
			column_value[row[col]]=1

		for value in column_value.keys():
			(set1,set2)=divideset(rows,col,value)

			p=float(len(set1))/len(rows)
			gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
			if gain>best_gain and len(set1)>0 and len(set2)>0:
				best_gain=gain
				best_criteria=(col,value)
				best_sets=(set1,set2)
			