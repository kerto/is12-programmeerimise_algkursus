arv1 = int(raw_input("Sisestage esimene arv:"))
arv2 = int(raw_input("Sisestage teine arv:"))
muutuv = 3
def arvud(arv1, arv2, muutuv):
	if arv1 > arv2:	
		arv1,arv2 = arv2,arv1	
		arv1 = arv1 + (muutuv - (arv1 % muutuv))
		return [i for i in range(arv1, arv2, muutuv)]

tulemus = [i for i in range((arv1 + (muut - (arv1 % muutuv))),arv2, muut)]
print "Sisestatud arvude vahel on" + str(len(tulemus)) + " arvu, mis jaguvad 3-ga"

## Teine

tekst = raw_input("Sisesta tekst:")

if tekst == str(tekst.lower()) and any(c.isdigit() for c in tekst):
	print "Tekstis on v2iksed t2hed ja numbrid."
elif tekst == str(tekst.lower()):
	print "Tekstis on v2iksed t2hed ja numbrid puuduvad."
elif tekst == str(tekst.upper()) and any(c.isdigit() for c in tekst):
	print "Tekstis on suured t2hed ja numbrid." 
elif tekst == str(tekst.upper()):
	print "Tekstis on suured t2hed ja numbrid puuduvad."
elif any(c.isdigit() for c in tekst):
	print "Tekstis on suured ja v2iksed t2hed ning numbrid."
else:
	print "Tektstis on suured ja v2iksed t2hed ja numbrid puuduvad."

print

