#!/usr/bin/env python
# coding=utf-8
# filename : treepredict_test.py
# author : Chase
# update : 2016/09/10

import treepredict

(set1,set2)=treepredict.divideset(treepredict.my_data,2,'yes')
print "divideset:"
print "set1 ", set1
print "set2 ", set2


# gini impurity
print "giniimpurity:", treepredict.giniimpurity(treepredict.my_data)
print "set1 ", treepredict.giniimpurity(set1)
print "entropy:", treepredict.entropy(treepredict.my_data)
print "set1 ", treepredict.entropy(set1)
print "set2 ", treepredict.entropy(set2)