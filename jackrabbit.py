print 'You enter a dark room with two doors. Do you go through door #1 or door #2?'

prompt = "> "

door = raw_input(prompt)

if door == '1':
	print 'There\'s a giant rabbit named Jack here eating carrots. What do you do?'
	print '1. Take the carrots'
	print '2. Scream at Jack.'

	rabbit = raw_input(prompt)

	if rabbit == '1':
		print "The rabbit eats your face off. Good job!"
	elif rabbit == '2':
		print "The rabbit eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better than those other options. Jack runs away." % rabbit

elif door == '2':
	print 'You run into a scared dog named Harvey. What shoud you do?'
	print '1. Teach him English.'
	print '2. Give him vision to see.'
	print '3. Give him fish to eat.'

	insanity = raw_input(prompt)

	if insanity == '1' or insanity == '2':
		print "That's nice of you to help a poor dog."
	else:
		print "You're not a very good vegan."

else:
	print "You don't want to play my game?"
