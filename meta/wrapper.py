data = open('dat.txt').read().strip().split("\n")
for line in data:
	c = line.split("	")

	print "### " + c[0]
	print
	print c[1]
	print