# get string input
player = raw_input("Enter the player's name: ")

# get integer input: int() convert string to integer
# float() convert string to floating number
year_joined = int(raw_input("When did the player join NBA: "))

years_in_nba = 2017 - year_joined

# use string formatting to output result
print "%s has played in NBA for %d years!" % (player, years_in_nba)
