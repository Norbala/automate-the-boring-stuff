import random

num_of_experiments = 10000
number_of_streaks = 0
sequence_length = 6
num_of_tosses = 100
streaks = 0

for experiment_number in range(num_of_experiments):
    randomList = list()
    for i in range(num_of_tosses):
        randomList.append("H" if random.randint(0,1) == 0 else "T")
        # ["H" if random.randint(0,1) == 0 else "T"]
    for i in range(num_of_tosses-sequence_length):
        if randomList[i:i+sequence_length] == (['H', 'H', 'H', 'H', 'H', 'H'] or ['T', 'T', 'T', 'T', 'T', 'T']):
            number_of_streaks+=1
    outcomes_string = ''.join(randomList)
    tail_streak = outcomes_string.count('T'*6)
    head_streak = outcomes_string.count('H'*6)
    streaks = tail_streak + head_streak




print(f"Chance of a streak: {100*(number_of_streaks / num_of_tosses)}%")
print((number_of_streaks))
print(streaks)