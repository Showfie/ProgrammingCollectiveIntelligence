#!/usr/bin/env python
# coding=utf-8
# filename : recommendations_test.py
# author : Chase
# update : 2016/09/10

import recommendations

print("distance between Leo and Cathy is:", 
	recommendations.sim_distance(recommendations.critics, 'Leo', 'Cathy'))
print("distance between Susie and Cathy is:", 
	recommendations.sim_distance(recommendations.critics, 'Susie', 'Cathy'))

print("Antonio TopMatches:",
	recommendations.topMatches(recommendations.critics,'Antonio', n=3))

print("Leo's recommendations:",
	recommendations.getRecommendations(recommendations.critics,'Leo'))