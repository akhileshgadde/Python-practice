inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

#add a new list with ‘pocket’ as key
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#sort the list with ‘backpack’ as key
inventory['backpack'].sort()

#remove('dagger') from the list of items stored under the 'backpack' key
inventory['backpack'].remove('dagger')

# add 50 to the number stored in ‘gold’ key
inventory['gold'] += 50

print inventory

"""Credits: CodeAcademy"""
