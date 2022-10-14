tweet = input('Enter tweet: ')

# Check if 160 characters or less
if len(tweet) > 160:
    print(f'This is {len(tweet) - 160} characters too long for a tweet')
else:
    if 'LOL' in tweet:
        print('LOL = laughing out loud')
    if 'BFN' in tweet:
        print('BFN = bye for now')
    if 'FTW' in tweet:
        print('FTW = for the win')
    if 'IRL' in tweet:
        print('IRL = in real life')
    if 'ROTFL' in tweet:
        print('ROTFL = rolling on the floor laughing')
