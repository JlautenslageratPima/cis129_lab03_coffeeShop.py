import time

print('Welcome to my Coffee and Muffin shop \n \nThe price of a cup of coffee is $5 and the price of a muffin is $4, We have also added Pretzels at $6 and holistic volcanic spring water from the top of Mt.Everest at $28')
time.sleep(1)

#This checks to confirm if user input is an integer and gives them a single chance to correct themselves. We could give them multiple chances by throwing them in a loop but it seems uneccesary for this project. 
try:
    coffeeOrdered = int(input('How many cups of coffee do you want today?'))
except ValueError:
    print("Invalid input. Please enter an integer.")
    coffeeOrdered = int(input('How many cups of coffee do you want today?'))
try:
    muffinOrdered = int(input('How many muffins do you want today?'))
except ValueError:
    print("Invalid input. Please enter an integer.")
    muffinOrdered = int(input('How many muffins do you want today?'))
try:
    pretzelOrdered = int(input('How many pretzels do you want today?'))
except ValueError:
    print("Invalid input. Please enter an integer.")
    pretzelOrdered = int(input('How many pretzels do you want today?'))
try:
    waterOrdered = int(input('How many bottles of water do you want today?'))
except ValueError:
    print("Invalid input. Please enter an integer.")
    waterOrdered = int(input('How many bottles of water do you want today?'))
print('Got it! \n \nPrepparing your order...')


#Calculates Order total and applies tax
coffeeTotalCost =  coffeeOrdered * 5
muffinTotalCost = muffinOrdered * 4
pretzelTotalCost =  pretzelOrdered * 6
waterTotalCost =  waterOrdered * 28
taxOnOrder = (coffeeTotalCost + muffinTotalCost + pretzelTotalCost + waterTotalCost) * .06
total = coffeeTotalCost + muffinTotalCost + pretzelTotalCost + waterTotalCost + taxOnOrder
time.sleep(3)

#Prints Receipt
print('***************************************')
print('My Coffee and Muffin Shop')
print(f'Number of coffees bought? \n {coffeeOrdered}')
print(f'Number of muffins bought? \n {muffinOrdered}')
print(f'Number of pretzels bought? \n {pretzelOrdered}')
print(f'Number of water bottles bought? \n {waterOrdered}')
print('*************************************** \n \n************************************** ')
print('My Coffee and Muffin Shop Receipt')
print(f'{coffeeOrdered} at $5 each: {coffeeTotalCost}')
print(f'{muffinOrdered} at $5 each: {muffinTotalCost}')
print(f'{pretzelOrdered} at $6 each: {pretzelTotalCost}')
print(f'{waterOrdered} at $5 each: {waterTotalCost}')
print(f'6% tax: {taxOnOrder}')
print('---------')
print(f'Total: ${total}')
print('***************************************')
print('\n \n Thank you for visiting I hope you come again!')


# unclear whether program should have stayed open in a while loop so i just set it to stay open long enough to view the results
time.sleep(20)
