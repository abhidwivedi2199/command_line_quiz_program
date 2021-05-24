import quiz

i=1
while i==1:
	print("Press 1. You are a Teacher.")
	print("Press 2. You are a Student.")
	print("Press 0 To exit")
	choice=int(input())
	if choice==1:
		print("Please Login : ")
		a=quiz.super_user_login()
		while a==1:
			print("If you want to add question Press 1.")
			print("If you want to logout Press 2.")
			b=int(input())
			if b==1:
				quiz.add_questions()
			elif b==2:
				quiz.logout()
				a=-1
			else:
				print("Wrong input")
		if a==0:
			pass


	elif choice==2:
		print("Press 1 to start the quiz.")
		i=int(input())
		if i==1:
			quiz.take_quiz()
		else:
			print("Wrong input")
	elif choice==0:
		i=0
	else:
		print("Wrong Input ,Please try again")


