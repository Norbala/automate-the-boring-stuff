import random

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

logging.disable(logging.DEBUG)

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug('The toss value is: %s' % toss)
if toss == 1:
    toss = 'heads'
else:    toss = 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in ('heads', 'tails'):
        print("Enter only 'heads' or 'tails':")
        guess = input()
    logging.debug('The second guess value is: %s' % guess)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

