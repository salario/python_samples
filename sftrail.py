# San Francisco Trail
# By: Salar Salahshoor

from sys import exit
import signal
import time

# Global variables
prompt = "What would you like to do next? \n> "

location = 1
items = ['2 bananas', '20 dollars', '1 can of mace']
game = 0
escape = 7
on = 90
game = on
start_time = time.time()
home = 2
location = home
marina = 8
embarcadero = 9
castro = 10
presidio = 11
marina = 5
tenderloin = 6
action = 12
win = 91

# Define neighborhoods
def neighborhoods():
	print """\n
	Castro
	Embarcadero
	Home
	Marina
	Presdiio
	Tenderloin\n
	"""

# Print inventory
def inventory():
	print "\n", items, "\n"

def loop_error():
	print "\nType a valid command.\n"

# Define timer to exit game
def timout_handler(signal, frame):
	print "\nYou ran out of time. Poor Jack is still lost! Try again tomorrow.\n"
	exit(0)
signal.signal(signal.SIGALRM, timout_handler)

# Define game time
def game_timer():
	game_time = time.time() - start_time
	minutes_left = int(300 - game_time) / 60
	seconds_left = int(300 - game_time) % 60
	print "\n", minutes_left, " minutes and ", seconds_left, " seconds left.\n"

# Checks to make sure the value entered is a number
def interpret_string(s):
    if not isinstance(s, basestring):
        return None
    if s.isdigit():
        return int(s)
    try:
        return float(s)
    except ValueError:
        return None

# Prints command instructions
def commands():
    print """\n
	To navigate, simply enter the name of the neighborhood to get there. To 
	search for Jack in any neighborhood, type "look" to find clues. To see what neighborhoods
	you can travel to, type "map". To see what you have in your inventory, type "inventory".
	To see where you are, type "location". To see how much time you have left, type "time".
	To see all these commands again, type "commands".\n"""

# Fail and exit the game
def fail(why):
    print "\n", why, "\n"
    exit(0)

# Initialize the game
print """\n
    You are at home. You just found out that your beloved rabbit,
    Jack, is missing. Your only clue to find him is that Isabel last
    saw him leaving the house to go get carrots. She tells you,
    "the dumbass left this morning without telling anyone where he was
    going. I heard him say something about the farmer's market, but I
    was distracted by the Gems singing a song I taught them and lost
    track of his blabbering. I can't be expected to watch over all these
    imbeciles."

    You decide to set out on a journey to find Jack and return him home safe.
    Mack agrees to give you a ride around San Francisco to track him down.
    You decide to take along a map and some cash. You have 10 minutes to
    track him down before the sun goes down and it's too dark to search.

    To navigate, simply enter the name of the neighborhood to get there.
    To search for Jack in any neighborhood, type "look". To see what neighborhoods
    you can travel to, type "map". To see what you have in your inventory, type
    "inventory". To see where you are, type "location". To see how much
    time you have left, type "time". To see all these commands again, type
    "commands". Good luck!\n
    """

signal.alarm(300)

while game == on:
	
	while location == home and "Jack" in items:
			game = win
			location = escape

	while location == home:

		instruction = raw_input(prompt).lower()

		if instruction == "castro":
			print """\nYou are in the Castro.\n"""
			location = castro

		elif instruction == "embarcadero":
			print """\nYou are in the Embarcadero.\n"""
			location = embarcadero

		elif instruction == "marina":
			print """\nYou are in the Marina.\n"""
			location = marina			

		elif instruction == "presidio":
			print """\nYou are in the Presidio.\n"""
			location = presidio

		elif instruction == "tenderloin":
			print """\nYou are in the Tenderloin.\n"""
			location = tenderloin

		elif instruction == "look":
			print """\nYou are at home, surrounded by sad family members, waiting for you to bring Jack home.\n"""
		
		elif instruction == "location":
			print "\nHome\n"
		
		elif instruction == "map":
			neighborhoods()

		elif instruction == "inventory":
			inventory()

		elif instruction == "time":
			game_timer()

		elif instruction == "commands":
			commands()

   		else:
   			loop_error()


	while location == castro:

		instruction = raw_input(prompt).lower()

		if instruction == "home":
			print """\nYou are at home.\n"""
			location = home

		elif instruction == "embarcadero":
			print """\nYou are in the Embarcadero.\n"""
			location = embarcadero

		elif instruction == "marina":
			print """\nYou are in the Marina.\n"""
			location = marina			

		elif instruction == "presidio":
			print """\nYou are in the Presidio.\n"""
			location = presidio

		elif instruction == "tenderloin":
			print """\nYou are in the Tenderloin.\n"""
			location = tenderloin

		elif instruction == "look":

			print """
	You find yourself in the heart of the Castro. No sign of Jack anywhere, but you stumble into
	an ice cream shop and the man at the counter tells you he thought he saw a rabbit earlier, but
	he can't be sure it was Jack.\n"""

		elif instruction == "location":
			print "\nCastro\n"

		elif instruction == "map":
			neighborhoods()

		elif instruction == "inventory":
			inventory()

		elif instruction == "time":
			game_timer()

		elif instruction == "commands":
			commands()

   		else:
   			loop_error()


	while location == embarcadero:

		instruction = raw_input(prompt).lower()

		if instruction == "home":
			print """\nYou are at home.\n"""
			location = home

		elif instruction == "castro":
			print """\nYou are in the Castro.\n"""
			location = castro

		elif instruction == "marina":
			print """\nYou are in the Marina.\n"""
			location = marina			

		elif instruction == "presidio":
			print """\nYou are in the Presidio.\n"""
			location = presidio

		elif instruction == "tenderloin":
			print """\nYou are in the Tenderloin.\n"""
			location = tenderloin

		elif instruction == "look":
			if '10 dollars' in items:
				if '1 crack pipe' not in items:
					print """
	You are surrounded by a busy farmer's market. A homeless man offers
	to help you find Jack for $10."""
					instruction = raw_input("\nDo you want to give him $10 to give you a clue? Yes or No?\n> ").lower()
					if instruction == "yes":
						print """
	The man takes your money and tells you he saw Jack with a little Tiger, and they were asking
	where they could buy some drugs. He hands you a crack pipe and wishes you good luck.\n"""
						items.remove('10 dollars')
						items.append('1 crack pipe')
		
				else:
					print """\nYou are surrounded by a busy farmer's market.\n"""
		
			elif '20 dollars' in items:
				print """
	You are surrounded by a busy farmer's market. A homeless man offers
	to help you find Jack for $10."""
				instruction = raw_input("\nDo you want to give him $10 to give you a clue? Yes or No?\n> ").lower()
				if instruction == "yes":
					print """
	The man takes your money and tells you he saw Jack with a little Tiger, and they were asking
	where they could buy some drugs. He hands you a crack pipe and wishes you good luck.\n"""
					items.remove('10 dollars')
					items.append('1 crack pipe')
			
			else:
				print """\nYou are surrounded by a busy farmer's market.\n"""
		
		elif instruction == "location":
			print "\nEmbarcadero\n"

		elif instruction == "map":
			neighborhoods()

		elif instruction == "inventory":
			inventory()

		elif instruction == "time":
			game_timer()

		elif instruction == "commands":
			commands()

   		else:
   			loop_error()


	while location == marina:

		instruction = raw_input(prompt).lower()

		if instruction == "home":
			print """\nYou are at home.\n"""
			location = home

		elif instruction == "embarcadero":
			print """\nYou are in the Embarcadero.\n"""
			location = embarcadero

		elif instruction == "castro":
			print """\nYou are in the Castro.\n"""
			location = castro			

		elif instruction == "presidio":
			print """\nYou are in the Presidio.\n"""
			location = presidio

		elif instruction == "tenderloin":
			print """\nYou are in the Tenderloin.\n"""
			location = tenderloin

		elif instruction == "look":
			if '10 dollars' in items:
				if '1 receipt' not in items:
					print """
	You find yourself near the Apple store in Marina. Across the street, you see an
	organic grocery store so you decide to go inside to scope out the situation.
	You ask the clerk if she's seen a rabbit come through, and she tells you she saw
	a blue rabbit purchase some carrots and that he seemed like he was in a hurry.\n"""

					instruction = raw_input("\nDo you want to tip the clerk $10 for being helpful? Yes or no?\n> ").lower()
					if instruction == "yes":
						print """
	The clerk accepts your tip and tells you she recalls the rabbit telling a story about
	how he was just in the Presidio searching for carrots at Off The Grid. Jack left a receipt
	with the clerk for a food truck named Hella Vegan Eats, and the clerk gives this to you.\n"""
						items.remove('10 dollars')
						items.append('1 receipt')

					else:
						print """\nYou are on Chestnut Street. No sign of Jack anywhere. :(\n"""	
				
				else:
					print """\nYou are on Chestnut Street. No sign of Jack anywhere. :(\n"""
			
			elif '20 dollars' in items:
				print """
	You find yourself near the Apple store in Marina. Across the street, you see an
	organic grocery store so you decide to go inside to scope out the situation.
	You ask the clerk if she's seen a rabbit come through, and she tells you she saw
	a blue rabbit purchase some carrots and that he seemed like he was in a hurry.\n"""

				instruction = raw_input("\nDo you want to tip the clerk $10 for being helpful? Yes or no?\n> ").lower()
				if instruction == "yes":
					print """
	The clerk accepts your tip and tells you she recalls the rabbit telling a story about
	how he was just in the Presidio searching for carrots at Off The Grid. Jack left a receipt
	with the clerk for a food truck named Hella Vegan Eats, and the clerk gives this to you.\n"""
					items.remove('20 dollars')
					items.append('10 dollars')
					items.append('1 receipt')

				else:
					print """\nYou are on Chestnut Street. No sign of Jack anywhere. :(\n"""
			
			else:
				print """\nYou are on Chestnut Street. No sign of Jack anywhere. :(\n"""
		
		elif instruction == "location":
			print "\nMarina\n"

		elif instruction == "map":
			neighborhoods()

		elif instruction == "inventory":
			inventory()

		elif instruction == "time":
			game_timer()

		elif instruction == "commands":
			commands()

   		else:
   			loop_error()


	while location == presidio:

		instruction = raw_input(prompt).lower()

		if instruction == "home":
			print """\nYou are at home.\n"""
			location = home

		elif instruction == "embarcadero":
			print """\nYou are in the Embarcadero.\n"""
			location = embarcadero

		elif instruction == "marina":
			print """\nYou are in the Marina.\n"""
			location = marina			

		elif instruction == "castro":
			print """\nYou are in the Castro.\n"""
			location = castro

		elif instruction == "tenderloin":
			print """\nYou are in the Tenderloin.\n"""
			location = tenderloin

		elif instruction == "look":
			if '1 receipt' in items:
				print """
	You are at Off The Grid. You make it to Hella Vegan Eats and show the cashier Jack's receipt.
	The woman at the counter immediately yells out for the police to seize you. Apparently
	Jack was with a wild tiger that stole money from the cash register. You decide to run into
	the woods instead of sticking around.\n"""
				items.remove('1 receipt')
				instruction = raw_input("\nYou run into a hungry bear. Do you want to use mace on the bear? Yes or No?\n> ").lower()
				if instruction == "yes":
					print """
	Close call! You use your mace on the bear and get away.\n"""
					items.remove('1 can of mace')

				elif instruction == "no":
					print """
	Good call! You decide to give the bear your bananas and he becomes your friend. You go on your way.\n"""	
					items.remove('2 bananas')
				
				else:
					fail("You need to think faster. The bear eats you and Jack remains lost. :(")

			else:
				print """\nYou are at Off The Grid, but there is no sign of Jack anywhere.\n"""

		elif instruction == "location":
			print "\nPresidio\n"

		elif instruction == "map":
			neighborhoods()

		elif instruction == "inventory":
			inventory()

		elif instruction == "time":
			game_timer()

		elif instruction == "commands":
			commands()

   		else:
   			loop_error()


	while location == tenderloin:

		instruction = raw_input(prompt).lower()

		if instruction == "home":
			print """\nYou are at home.\n"""
			location = home

		elif instruction == "embarcadero":
			print """\nYou are in the Embarcadero.\n"""
			location = embarcadero

		elif instruction == "marina":
			print """\nYou are in the Marina.\n"""
			location = marina			

		elif instruction == "presidio":
			print """\nYou are in the Presidio.\n"""
			location = presidio

		elif instruction == "castro":
			print """\nYou are in the Castro.\n"""
			location = castro

		elif instruction == "look":
			if '1 crack pipe' in items:
				print """
	You spot a crack head and ask where you can get some drugs in the hopes that
	you'll find Jack and Frank. You give him your pipe and he points you to the
	local dealer down the streat.\n"""
				items.remove('1 crack pipe')
				instruction = raw_input("\nDo you want to approach the dealer? Yes or No?\n> ").lower()
				if instruction == "yes" and '1 can of mace' in items:
					print """
	You spot Jack and Frank tied up next to the dealer and decide to use your can of mace. You
	hit the dealer right in the face with your mace, grab Jack and Frank, and escape.\n"""
					items.remove('1 can of mace')
					items.append('Jack')
					items.append('Frank')

				elif instruction == "yes" and '1 can of mace' not in items:
					fail("You spot Jack and Frank tied up next to the dealer, but you have no way of getting past the angry dealer. Poor Jack and Frank!")

				else:
					fail("You had your chance and you blew it. You'll have to try again another day")

			else:
				print """\nYou find yourself in the Tenderloin, but it's a scary sight and you don't know what to do.\n"""

		elif instruction == "location":
			print "\nTenderloin\n"

		elif instruction == "map":
			neighborhoods()

		elif instruction == "inventory":
			inventory()

		elif instruction == "time":
			game_timer()

		elif instruction == "commands":
			commands()

   		else:
   			loop_error()


while game == win:
	print "Congratulations! You saved the day. Jack is safe at home."
	print """
    ,::.                           ::
   ::;;:.                        .::;:
   ::;;;:.                      ,;::;:,
   ;;;;;;,                     .;::;;;:
   ;::;;;:,                   `;::;;;;:
   `:;;;;;:`                  ;;:;;;;;.
    ;:;;;;;:                 ;;::;;;;:
    `:;;;';:`               ,;::;;;;;
     :;:;;;;:               ;::;';;;`
      ;;:;;;:`             ;;;;;;;:
      `;::;;;:             ;:;;;;:
        ;:;;;;`           ;:;;;;,
         ;:::::,,,,,,,::::;:;;;;
          ::;;::::::::::::::;:;
          `;;::::::::::::::::;`
           ::::::::::::::,:,,,
          .::::::::::::::,,,,,`
          ;;;::::::::::::,,,,,.
         .;;;;;::::::::::,,,,,,
         ;;;;;;::::::::::,,,,,,`
        `;;;;;:;::::::::::,,,,..
        :;;;;:;;:::::::::,,,,,,.
   ,:`  ;;;;##:;:::::::::,##,,,,;  ':,
      ::;.`;;;+##';;;:,,:::::##+;:; 
    ;:;;;;;++#;;;::,..::::#++;;,;:;:
     :;;;;;;;;;;':::,..:::'':,,,:;;:`
      `:;;;;;;;;':::,,.,:::,,,,,:;,
      ':;;;;;;;;';::,,.:::,:,,,,,
    :;';;;;;;;;;;';:,,:,,::,:,,,::,
    ::;`:;;;;;;;;;;;:::,:::,,,,,;;::
    ;;, .:;;;;;;;;;:::::::::,,,. ,;;
         :::;;;;;` ` ::::::,,,,`
          ::;;;;:` ``::::::,,,.
           ,::;:;;:::::::::::.
           `,:::::::::::::::`
             `;;::::::::,:`
             ;;;::::::::;
             ;;;;;;;;;;::`
            .;;;;;;;;;;::,
            ;;;;;;;;;;:::,
           .';;;;;;;;;:::,`
          ;;';;;::;;';:::,:,
         ;''+;;;::'';;:::,:,,
     `` `''++;;;::''';::,:::,`,:.
    ;;:;;;'++;;:::++';::,:;::::::,
   `;;:::''++;;:::++';:::;;::;::::
   ,;;::::'++;;:::++;;:::;;;;:::::`
   :;;::::;++;;:::'+;::::'';;:::,:`
   ,;;;:::'+#;;:::'+:::::'';;;::::
   `;;;:::'# ;;::,. ;;:::;+';;:::,
    ;;;:;'   ;;:::  `;:::   ,';:.               
   """                                               

	exit(0)