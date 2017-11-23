

def all_perms(elements):
	# Temp list
	new_list = []

	# If the elements in the list only have one character return it
	if len(elements) <=1:
		new_list.append(elements)

	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				new_list.append(perm[:i] + elements[0:1] + perm[i:]) 

	return(new_list)




with open('test.txt') as f:
	contents = f.readlines()
contents = [x.strip() for x in contents]


# Loop over each line in the file pass it to the function
for content in contents:
	perms = all_perms(content)

	# The sorted built-in function within python3 sorts the lists
	print(sorted(perms))

