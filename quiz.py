import json
import random

global s_user
s_user=[]

def take_quiz():
	print("************* QUIZ STARTED *************")
	score=0
	name=input("Please enter your name : ")
	with open("questions.json", 'r+') as a:
		j=json.load(a)
		for i in range(10):
			number_of_questions=len(j)
			rand=random.randint(0,number_of_questions-1)
			print(" ")
			print(j[rand]["question"])
			for option in j[rand]["options"]:
				print(option)
			user_answer = input("Enter your answer: ")
			if j[rand]["answer"][0] == user_answer[0].upper():
				score+=1
				print("Your answer is correct!!")
			else:
				print("Incorrect! , correct answer is : ",j[rand]["answer"][0])
			del j[rand]
		print("************* QUIZ IS OVER *************")
		print(" ")
		print(name,"Your Final Score is ",score)
		print(" ")

def add_questions():
	if len(s_user)==0:
		print("You need to login first in order to add questions.")
	elif len(s_user)>0 and s_user[0]==1:
		print("**********ADD QUESTIONS**********")
		question=input("Enter the question you want to add : ")
		option=[]
		for i in range(4):
			option.append(input())
		answer=input("Enter the correct answer : ")
		with open("questions.json", 'r+') as a:
			questions = json.load(a)
			ques_dict={"question": question, "options": option, "answer": answer}
			questions.append(ques_dict)
			a.seek(0)
			json.dump(questions,a,indent=4)
			a.truncate()
			print("Question added successfully.")	
	else:
		pass




def super_user_login():
	print("**********LOGIN SUPER USER**********")
	username = input("username: ")
	password = input("password: ")
	with open('user_accounts.json', 'r') as super_user:
		users = json.load(super_user)
	if username not in users.keys():
		print("Account with such username does not exist.")
		return 0
	elif username in users.keys():
		if users[username][0] != password:
			print("Your password is incorrect. Please try again")
			return 0
		elif users[username][0] == password:
			print("You have successfully logged in.")
			global s_user
			s_user.append(1)
			return 1
			

def logout():
	global s_user
	if len(s_user) == 0:
		print("You are already logged out.")
	else:
		s_user = []
		print("You have been logged out successfully.")


