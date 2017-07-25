from sys import argv

script, filename = argv

targetR = open(filename, 'r')
prompt = "> "

# Prints the contents of the original file for the user to see.
print "Here are the contents of your file."
print targetR.read()
targetR.close()

# Gives the user an opportunity to back out of truncating the file.
print "Are you sure you want to continue? Hit enter to proceed."
raw_input(prompt)

targetW = open(filename, 'w')
print "Your file is being deleted..."
targetW.truncate()

# Let's the user input new values for the same file that was truncated.
print 'We\'re going to ask you to write five new lines of content.'
line1 = raw_input(prompt)
line2 = raw_input(prompt)
line3 = raw_input(prompt)
line4 = raw_input(prompt)
line5 = raw_input(prompt)

print 'We\'re writing these updates to the file now.'

targetW.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5)
targetW.close()

targetX = open(filename, 'r')
# Reads the new content for the file for the user to verify it worked.
print "Here are the contents of your new file: \n"
print targetX.read()

targetX.close()