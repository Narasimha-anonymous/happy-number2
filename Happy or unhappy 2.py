while True:	
	def check(n):
		while n!=1 and n!=4:
			a=0
			while n:
				r=n%10
				a+=r*r
				n//=10
			n=a
		if n==1:
			print("Happy number")
		else:
			print("Unhappy number")
	def range(p,q,d):
		if p>q:
			p,q=q,p
		for n in range(p,q+1):
				t=n
				while n!=1 and n!=4:
					a=0
					while n:
						r=n%10
						a+=r*r
						n//=10
					n=a
				if n==1 and d==1 :
					print(t)
				elif n==4 and d==0:
					print(t)
	print("Check or Range \nType 'C' or 'Check' to check the number Happy or Not happy\nType 'R' or 'Range' for happy or not happy numbers for given range")
	k=input()
	if k in "checkCheck":
		n=int(input("Enter the number:"))
		check(n)
	elif k in "Rangerange":
		p,q=map(int,input("Enter range:").split())
		print('Do you want happy numbers or not happy numbers?\nFor happy type "Happy numbers" or "Happy number" or "Happy" or "happy number" or "happy" or "H" or "h"\nFor not happy numbers type "Unhappy numbers" or "Unhappy number" or "Unhappy" or "unhappy number" or "unhappy" or "Un" or "un" ')
		s=input()
		if s in "Happy numbershappy numbers" :
			d=1
		elif s  in "Unhappy numbersunhappy numbers":
			d=0
		range(p,q,d)
	elif k=="break":
		break