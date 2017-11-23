
# The Requests Python package should be built into Python3 but can be installed using pip: pip install requests
import json
import requests


val = ""

while val != 4:

	print("\nPress 1: To Get All 200 Todo's")
	print("Press 2: To Make A Todo")
	print("Press 3: To Delete A Todo")
	print("Press 4: To Quit The Program")

	option=input("Option :")

	try:
		val = int(option)
	except ValueError:
		print("That's not an option!")

	# Retrieve all 200 Todo items
	if val == 1:
		r = requests.get('https://jsonplaceholder.typicode.com/todos')
		todos = r.json()
		for todo in todos:
			print("Todo ID: %s, user ID: %s, Title: %s, Completed: %s" % (todo['id'], todo['userId'], todo['title'], todo['completed']))


	# Create a Todo item
	if val == 2:
		data = {}
		title = input("Please enter a title for your todo item :")
		completed = input("Is this todo item completed (y/n)? :")
		
		if completed.lower() == 'y':
			completed = True
		else:
			completed = False

		data['title'] = title
		data['completed'] = completed

		r = requests.post('https://jsonplaceholder.typicode.com/todos', data=data)
		todo = r.json()
		print("Todo item created!")
		print("Todo ID: %s, Title: %s, Completed: %s" % (todo['id'], todo['title'], todo['completed']))


	# Delete a Todo item
	if val == 3:

		# Using a while loop like this is not best practice but it's fine for this use case
		status = False
		while status != True :
			pk = input("Please enter the ID of the todo item you wish to delete :")
			
			try:
				pk = int(pk)
				todo = requests.get('https://jsonplaceholder.typicode.com/todos/%s' % (pk))
				
				# Make sure the id exists
				if todo.status_code == 200:

					# Delete it if it does
					r = requests.delete('https://jsonplaceholder.typicode.com/todos/%s' % (pk))
					status = True
					todo = todo.json()
					print("Todo Item #: %s, With Title: %s, was deleted!" % (todo['id'], todo['title']))
				
				# Loop program to ask for a valid id
				else:
					status = False
					print("That Item does not exist please enter another one")
			
			except ValueError:
				print("Enter an Integer")

			





















