import cmath
a=float(input("Enetr the a value"))
b=float(input("Enetr the b value"))
c=float(input("Enetr tyhe c value"))
d=((b*b)-(4*a*c))
if d==0:
	root=-b/(2*a)
	print("Roots are equal")
	print("root="+root)
if d>0.0:
	root1=(-b+(cmath.sqrt(d)))/(2*a*c)
	root2=(-b-(cmath.sqrt(d)))/(2*a*c)
	print("Roots are real and distinct")
	print("Root1=",root1)
	print("root2=",root2)
else:
	print("roots are imaginary")

