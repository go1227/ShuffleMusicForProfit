__author__ = "Guilherme Ortiz"
__version__ = "1.1"
__date_last_modification__ = "12/22/2018"


# This program is intended to read a given list of music (CSV file) and shuffle it.
# However, each time a song is played, the streaming service has to pay royalties/fees to the artists.
# Depending on how cheap/expensive the song is per play, the shuffle algorithm should provide the cheap songs first and then the more expensive ones, so the streaming service can avoid paying for the expensive songs as much as possible, by simply suppressing the expensive songs to the end of this shuffled list of songs
# Example:
# List of songs: (musics UUU and XXX are more expensive, so we will only present these songs at the end of this "custom shuffle" list produced.
# 1. Music AAA - full play price: $0.001
# 2. Music TTT  - $0.002
# 3. Music YYY  - $0.001
# 4. Music UUU  - $0.08 - expensive to play (must go to the bottom of the shuffle list)
# 5. Music XXX  - $0.09 - expensive to play (must go to the bottom of the shuffle list)
# 6. Music EEE  - $0.002
# 7. Music PPP  - $0.001
#
# Sample result of custom shuffling:
# Music YYY, Music PPP, Music AAA, Music EEE, Music TTT, Music XXX, Music UUU


import random
import csv

try:
    # Read all songs and prices from a CSV file - songlist.csv
    with open('songlist.csv','r',encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        fullmusiclist = list(reader)
    file.close()
except:
    print("The file 'songlist.csv' couldn't be found or loaded.\nExecution of program aborted.")
    exit()


# Split the list of prices into 2 even parts, so we can balance them using recursive function
def balancelist(listA, listB):
    while (sum(listA) < sum(listB) and len(listB) > 1):
        #print(str(listA) + '........' + str(listB))
        listA.append(listB[0])
        listB.pop(0)  # there is no need to use popleft() because we are assuming that this is a very short and simple list of numbers, so no big performance gains would be noticedx
        balancelist(listA, listB)
    return listA, listB


# Get all DISTINCT prices from fullmusiclist into the set "prices"
prices = set()
for price in fullmusiclist:
    prices.add(float(price[3]))

prices = list(prices)
prices.sort()

# Split the list of prices into 2, so we can balance them using a recursive function
prices_a = prices[:int(len(prices)/2)]
prices_b = prices[int(len(prices)/2):]

prices_a, prices_b = balancelist(prices_a, prices_b)

shufflegroup_a = []
shufflegroup_b = []

# Allocate all song codes that have the price in Price_A list ("cheaper songs") and Price_B list ("more expensive songs")
for i in fullmusiclist:
    if float(i[3]) in prices_a:
        #print('Adding [' + str(i[0]) + ']')
        shufflegroup_a.append(i[0])
    else:
        #print('Adding [' + str(i[0]) + ']')
        shufflegroup_b.append(i[0])

random.shuffle(shufflegroup_a)
random.shuffle(shufflegroup_b)

# Print full list of songs that were shuffled based on price per song (more expensive always at the bottom of the list)
shufflemusiccodes = shufflegroup_a + shufflegroup_b

for i in shufflemusiccodes:
    for j in fullmusiclist:
        if int(i) == int(j[0]):
            print(j[1] + ' - ' + j[2])
            break