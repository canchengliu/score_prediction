# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import os

def __stripline__(line_list):
	for line in line_list:
		line = line.strip()
	return line_list


def read_submissions():
	subm_list = os.listdir('submissions/')
	print len(subm_list)
	if os.path.isdir('whole_submissions_simple') is False:
		os.mkdir('whole_submissions_simple')
	fw = open('whole_submissions_simple/total_sub.txt', 'w')
	context = ''
	for subm in subm_list:
		if subm == 'readme':
			continue
		f = open('submissions/' + subm)
		lines = f.readlines()
		student = lines[0]
		ass = lines[1]
		#time = lines[2]
		score = lines[3]
		context += student + ass + score
		#code = lines[4]
		#comment = lines[5:]		
	fw.write(context)

def readlines_():
	f = open('exams/16')
	lines = f.readlines()
	print len(lines[2])

read_submissions()
