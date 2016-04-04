# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import os
import math
"""
student -> student each exam id -> student each exam each ass id -> ass score -> each exam score 
@ ass_dir[ass] = exe_id
@ class_dir[class] = (hw_id, exam_list, students)
@ exam_dir[exam] = (exam_name, ass_list)
@ hw_dir[homework] = ass_list
@ sa_score_dir[student][ass] = score_list
"""

def __stripline__(line_list):
	new_line_list = []
	for line in line_list:
		if line == '\n':
			continue
		new_line_list.append(line.strip())
	return new_line_list

"""
k = []

for i in range(50):
	k.append(lambda_fun(i) + 0.5)
"""
def lambda_fun(x):
	return 1.0 / (1 + pow(1.1, 1 * x))


"""
题目ID（对应exercises目录内容）
开始时间
hard due
soft due

@ ass_dir[ass] = exe_id
"""
def read_ass():
	ass_dir = {}
	ass_list = os.listdir('assignments/')
	for ass in ass_list:
		if ass == 'readme':
			continue
		f = open('assignments/' + ass)
		exe_id = __stripline__(f.readlines())[0]
		ass_dir[ass] = exe_id
	return ass_dir

"""
行为列表（多行），包括以下的行为代码：
date view ID: 浏览作业, ID对应assignment目录内容
date subm ID: 提交程序, ID对应submissions目录内容
date login: 登录
date logout: 退出

@
"""
def read_bh():
	pass

"""
课程名
homework ID（作业安排，对应homework目录内容）
exam IDs（考试安排，一行内多个，对应exams目录内容）
学生ID列表 (多行，对应students目录内容)

@ class_dir[class] = (hw_id, exam_list, students)
"""
def read_class():
	class_dir = {}	
	class_list = os.listdir('classes/')
	for cl in class_list:
		if cl == 'readme':
			continue
		f = open('classes/' + cl)
		lines = __stripline__(f.readlines())
		hw_id = lines[1]
		exam_list = lines[2].split()
		students = lines[3:]
		class_dir[cl] = (hw_id, exam_list, students)
	return class_dir

"""
提交的代码文件内容，多行

@
"""
def read_code():
	pass


"""
考试名称
作业列表（多行，对应assignments目录内容）

@ exam_dir[exam] = (exam_name, ass_list)
"""
def read_exam():
	exam_dir = {}
	exam_list = os.listdir('exams/')
	for exam in exam_list:
		if exam == 'readme':
			continue
		f = open('exams/' + exam)
		lines = __stripline__(f.readlines())
		exam_name = lines[0]
		ass_list = lines[1:]
		exam_dir[exam] = (exam_name, ass_list)
	return exam_dir

"""
@ st_exam_score[student] = score
@ class_dir[class] = (hw_id, exam_list, students)
"""
def exam_score():
	st_exam_score = {}
	exam_dir = read_exam()
	class_dir = read_class()
	for cl in class_dir:
		hw_id, exam_list, students = class_dir[cl]
		for st in students:
			score = 0
			for exam in exam_list:
				ass_list = exam_dir[exam]
				if len(ass_list) > 12:
					each = 2
				else:
					each = 10

		for exam in exam_list:




"""
标题
类型
题目描述（多行）

@
"""
def read_exercises():
	pass


"""
作业列表（多行，对应assignments目录内容）

@ hw_dir[homework] = ass_list
"""
def read_hw():
	hw_dir = {}
	hw_list = os.listdir('homework/')
	for hw in hw_list:
		if hw == 'readme':
			continue
		f = open('homework/' + hw)
		hw_dir[hw] = __stripline__(f.readlines())
	return hw_dir


"""
性别
报考时是否第一目标就是计算机专业？
高中是否接触过编程？
高考成绩（保送生填0）
毕业省市

male
否
没有基础
612
湖北省荆州市

@ st_info_dir[st] = value
"""
def read_student():
	st_info_dir = {}
	st_list = os.listdir('students/')
	for st in st_list:
		if st == 'readme':
			continue
		f = open('students/' + st)
		st_info_dir[st] = __stripline__(f.readlines())
	return st_info_dir

"""
@ st_value_dir[st] = value [1, 1.7]
"""
def student_value():
	st_info_dir = read_student()
	st_value = {}
	for st in st_info_dir:
		value = 0.0
		sex, first, fund, grade, location = st_info_dir[st]
		if sex == 'male':
			value += 0.05
		if first == '是':
			value += 0.05
		if fund[0] != '没':
			value += 0.5
		st_value[st] = 1 + value
	return st_value



"""
提交学生ID（对应students目录内容）
作业ID（对应assignments目录内容）
提交时间
分数
编程题：提交文件的IDs（一行内可以有多个ID，对应code目录内容）；解释题和选择题：提交的答案
评分反馈（多行）

@ sa_score_dir[student].append((ass, time, score))
"""
def _read_submissions():
	sa_score_dir = {}
	subm_list = os.listdir('submissions/')
	for subm in subm_list:
		if subm == 'readme':
			continue
		f = open('submissions/' + subm)
		lines = __stripline__(f.readlines())
		student = lines[0]
		ass = lines[1]
		#time = lines[2]
		score = lines[3]
		#code = lines[4]
		#comment = lines[5:]
		if student not in sa_score_dir:
			sa_score_dir[student] = {}
		if ass not in sa_score_dir[student]:
			sa_score_dir[student][ass] = []
		if score[0] < '0' or score[0] > '9':
			score = '0'
		sa_score_dir[student][ass].append(int(score))
	for s in sa_score_dir:
		for a in sa_score_dir[s]:
			sa_score_dir[s][a].sort(reverse=True)
	return sa_score_dir

"""
subm_ID
提交学生ID（对应students目录内容）
作业ID（对应assignments目录内容）
提交时间
分数
编程题：提交文件的IDs（一行内可以有多个ID，对应code目录内容）；解释题和选择题：提交的答案
评分反馈（多行）

@ sa_score_dir[student].append((ass, time, score))
"""
def read_submissions():
	sa_score_dir = {}
	f = open('whole_submissions_simple/total_sub.txt')
	lines = __stripline__(f.readlines())
	subm_list = zip(*[iter(lines)]*3)
	for subm_arr in subm_list:
		student, ass, score = subm_arr
		if student not in sa_score_dir:
			sa_score_dir[student] = {}
		if ass not in sa_score_dir[student]:
			sa_score_dir[student][ass] = []
		if score[0] < '0' or score[0] > '9':
			score = '0'
		sa_score_dir[student][ass].append(int(score))
	for s in sa_score_dir:
		for a in sa_score_dir[s]:
			sa_score_dir[s][a].sort(reverse=True)
	return sa_score_dir



"""
@ cl_ass_score[class][assignment] = list of students' score list
"""

def get_ass_score(hw_dir, sa_score_dir, class_dir):
	cl_ass_score = {}
	for cl in class_dir:
		hw_id, exam_list, students = class_dir[cl]
		hw_list = hw_dir[hw_id]
		amount = len(students)
		cl_ass_score[cl] = {}
		for s in students:
			if s not in sa_score_dir: # student s never submit any homework, s contribution nothing to the difficulty of assignment, just ignore it
				continue 
			for ass in hw_list:
				if ass not in cl_ass_score[cl]:
					cl_ass_score[cl][ass] = []
				else:
					if ass not in sa_score_dir[s]: # student s never submit assignment ass
						cl_ass_score[cl][ass].append([0])
					else:
						cl_ass_score[cl][ass].append(sa_score_dir[s][ass])
	return cl_ass_score

def _fix_sub_cnt(cnt):
	return math.log(cnt + 9, 10)

def fix_difficulty(cl_ass_score):
	cl_ass_dif = {}
	for cl in cl_ass_score:
		cl_ass_dif[cl] = {}
		for ass in cl_ass_score[cl]:
			ll_score = cl_ass_score[cl][ass]
			max_list = [s[0] / _fix_sub_cnt(len(s)) for s in ll_score]
			#max_list = [s[0] for s in ll_score]
			avg_score = sum(max_list) / len(max_list)
			if avg_score < 10: # 避免负数和难度系数相差太大
				avg_score = 10
			#cl_ass_dif[cl][ass] = 1.0 / avg_score # 1 / math.sqrt(avg_score)
			cl_ass_dif[cl][ass] = avg_score # 1 / math.sqrt(avg_score)
	return cl_ass_dif


"""
@ cl_st_score[class][student] = total_hw_score

@ 平均最高分: avg_highest_score[ass] = avg_highest_score
@ 平均提交次数: avg_submit_time[ass] = avg_submit_time
@ 提交率: submit_rate[ass] = submit_rate
@ 作业难度: ass_diff[ass] = difficult
"""


def hw_score():
	# result
	avg_highest_score = {}
	cl_st_score = {}
	# read data about homework and assignment etc
	hw_dir = read_hw()
	sa_score_dir = read_submissions()	
	class_dir = read_class()
	# calculate the total homework score of each student in each class
	cl_ass_score = get_ass_score(hw_dir, sa_score_dir, class_dir)
	cl_ass_dif = fix_difficulty(cl_ass_score)

	for cl in class_dir:
		hw_id, exam_list, students = class_dir[cl]
		hw_list = hw_dir[hw_id]
		amount = len(students)
		cl_st_score[cl] = {}
		for s in students:
			cl_st_score[cl][s] = 0
			if s not in sa_score_dir: # student s never submit any homework
				continue 
			for ass in hw_list:
				if ass not in sa_score_dir[s]: # student s never submit assignment ass
					continue
				#-- fix difficulty--
				score = sa_score_dir[s][ass][0]
				#score *= (1 + (score - cl_ass_dif[cl][ass]) / 20.0)
				score = pow(score - cl_ass_dif[cl][ass], 3)
				cl_st_score[cl][s] += score
				#-- fix difficulty--
				#cl_st_score[cl][s] += sa_score_dir[s][ass][0]
				#cl_st_score[cl][s] += sa_score_dir[s][ass][0] * lambda_fun(len(sa_score_dir[s][ass]))
	return cl_st_score

"""
学生提交各个作业的分数列表
要计算个题目难度
方差
提交次数
平均分

difficult = ((final_score = 100) ? final_score : final_score / 2) * log2(submit_time ＋ 2)

从我多年数据挖掘的经验来看，有很多可以参考的feature，但是没有好的训练模型的话，引入的feature越多，带来的噪声远大于得到的有效信息
特征选择的一种典型思路是可以用随机组合然后通过结果加以选择的方式，例如经典的爬山算法或则模拟退货算法，
但是这需要跑很多次来验证，而这次作业是在线提交测试，故不采用这种方法
"""


"""
@ sort_class[cl] = sorted_student_list
"""
def sort_student():
	cl_st_score = hw_score()
	st_value = student_value()
	for cl in cl_st_score:
		for st in cl_st_score[cl]:
			if st in st_value:
				#pass
				cl_st_score[cl][st] *= st_value[st]
			else:
				print '*',
	student_list = []
	sort_class = {}
	for cl in cl_st_score:
		st_score_dic = cl_st_score[cl]
		sorted_dic = sorted(st_score_dic.iteritems(), key=lambda kv:kv[1], reverse=True)
		student_list = [kv[0] for kv in sorted_dic]
		sort_class[cl] = student_list
	return sort_class

"""
write the final result of sorted student list
"""
def write_result():
	sort_class = sort_student()
	if os.path.isdir('prediction') is False:
		os.mkdir('prediction')
	for cl in sort_class:
		f = open('prediction/' + cl, 'w')
		s = '\n'.join(sort_class[cl])
		f.write(s + '\n')
		f.close()

if __name__ == '__main__':
	write_result()

