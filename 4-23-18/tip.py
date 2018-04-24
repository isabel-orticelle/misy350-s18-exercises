# get string input
Total_bill =int(raw_input("Enter the total amont: "))

# get integer input: int() convert string to integer
# float() convert string to floating number
tip_rate = float(raw_input("Enter tip rate (such as .15): "))

tip=(Total_bill*tip_rate)
total=int(Total_bill+tip)


# use string formatting to output result
print "You should pay: $%d" % (total)
