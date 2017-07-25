def demo(name, age, gender, oppGender):
	print "Your name is %s." % name
	print "You are %s years old." % age
	print "You are %s." % gender
	print "You are not %s." % oppGender


prompt = "> "

print "What is your name?"
yourName = raw_input(prompt)

print "What is your age?"
yourAge = raw_input(prompt)

print "What is your gender, male or female?"
yourGender = raw_input(prompt)

if yourGender == "male":
	yourOppGender = "female"
else:
	yourOppGender = "male"

demo(yourName, yourAge, yourGender, yourOppGender)