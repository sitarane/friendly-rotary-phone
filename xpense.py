parties = int(input("How many people: "))

everyone = []

for party in range(parties):
	everyone.append({"Name": input("Name #%d: " % (party + 1))})

# Total spent

for someone in range(len(everyone)):
	everyone[someone]["Spent"] = float(input("Amount spent by %s: " % everyone[someone]["Name"]))

print("Spendlist:", everyone)

total = 0
for someone in range(len(everyone)):
	total += everyone[someone]["Spent"]

print("You guys spent a total of", total)

# Fill in the money owed

for someone in range(len(everyone)):
	everyone[someone]["Gets"] = everyone[someone]["Spent"] - ( total / parties )

# Sort by debt

everyone.sort(key=lambda item: item.get("Gets"))

# Biggest with biggest. Substact. Repeat.

while everyone[0]["Gets"] != 0:
	max_debit = everyone[0]["Gets"] # Negative number
	max_credit = everyone[len(everyone) - 1]["Gets"]
	diff = max_debit + max_credit
	print(everyone[0]["Name"], "pays", max(abs(max_credit), abs(max_debit)), "to", everyone[len(everyone) - 1]["Name"])
	if diff >= 0: # Reduce max_debit/credit of what's been paid
		everyone[0]["Gets"] = 0
		everyone[len(everyone) - 1]["Gets"] = diff
	else:
		everyone[0]["Gets"] = diff
		everyone[len(everyone) - 1]["Gets"] = 0
	everyone.sort(key=lambda item: item.get("Gets")) # resort so we get new max candidates next iteration
