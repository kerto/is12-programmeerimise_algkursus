def faktoriaal(n):
	f = 1	
	i = 1
	while i <= n:	
		f = f * i
		i = i + 1
	return f

print "5!=" + str(faktoriaal(5))
print "7!=" + str(faktoriaal(7))


