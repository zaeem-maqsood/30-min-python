

poem = "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles And by opposing end them. To die—to sleep, No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to: 'tis a consummation Devoutly to be wish'd. To die, to sleep; To sleep, perchance to dream—ay, there's the rub: For in that sleep of death what dreams may come, When we have shuffled off this mortal coil, Must give us pause—there's the respect That makes calamity of so long life. For who would bear the whips and scorns of time, Th'oppressor's wrong, the proud man's contumely, The pangs of dispriz'd love, the law's delay, The insolence of office, and the spurns That patient merit of th'unworthy takes, When he himself might his quietus make With a bare bodkin? Who would fardels bear, To grunt and sweat under a weary life, But that the dread of something after death, The undiscovere'd country, from whose bourn No traveller returns, puzzles the will, And makes us rather bear those ills we have Than fly to others that we know not of? Thus conscience does make cowards of us all, And thus the native hue of resolution Is sicklied o'er with the pale cast of thought, And enterprises of great pitch and moment With this regard their currents turn awry And lose the name of action."
# convert every single character to an element of a list
poem_list = list(poem)
# you can print this if you wanna see what happens



# Take out the punctiation----------------------------------------------------------------------------------------------------------------------
new_poem_list = []
# I just made a list of punctuation you can add more if you want
punctuation_list = ['.', ',', '"', '-', "'", ':', '!', '_', '/', '#', '?']
# Loop through the poem list of characters and remove all punctuation
for character in poem_list:
	if character not in punctuation_list:
		new_poem_list.append(character)




# Join the words back now that the puncuation is gone--------------------------------------------------------------------------------------------

# This will be the new list that has all the words in it
rejoined_list = []

# This is a temporary string that keeps changing in value depending on the word we are working on
word = ""

for character in new_poem_list:
	
	# If there is a space then we want to stop adding characters to our temporary string (word) and add the completed word to our list (rejoined_list)
	if character == ' ':
		rejoined_list.append(word)
		word = ""

	# If there isn't a space yet then just keep adding the characters to our temporary string (word). Oh and make sure everything is set to lower case
	else:
		word += character.lower()



# Count the words and add it to a dictionary ---------------------------------------------------------------------------------------------------

# Create a dictionary that is going to hold the word and how many times the word was used
"""
this is an example of how the dictionary looks 

word_and_its_count_dict = {'the': 10,  'to': 7}

Remember a dictionay has a key and a value for that key. So the key in our case is goin to be the word,
and the value is going to be the amount of times that word is in the poem
"""
word_and_its_count_dict = {}


for word in rejoined_list:

	# So if the word is not already in the list set the value of the word to how many times it appears in the list(rejoined_list)
	# Also remember to assign a value to a dictionary we use this syntax dictionary[key] = value
	# So thats what we did, our dictionary is 'word_and_its_count_dict' and the key is the 'word' and the value is 'rejoined_list.count(word)'
	if word not in word_and_its_count_dict:
		word_and_its_count_dict[word] = rejoined_list.count(word)



# Now just simply print the keys(words) and the values(word counts) --------------------------------------------------------------------------------
for word, word_count in word_and_its_count_dict.items():
	print("The word: '%s' is in the poem %s times" % (word, word_count))













