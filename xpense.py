parties = input("How many people: ")

#Create a list of money spent
spent = []
for i in range(parties):
	spent.append(float(input("Total spent by that guy: ")))

#Create a payback list
result = []
for k in range(parties):
	result.append(spent[k] - ( sum(spent) / parties ))

# Show the results
for l in range(parties):
	if result[l] > 0:
		print "Whoever spend %d gets %d from the leeches" % (spent[l], result[l])
	elif result[l] == 0:	
		print "Whoever spend %d can go home now" % spent[l]
	else:
		print "Whoever spend %d pays %d to the capitalist pigs" % (spent[l], result[l] * -1)