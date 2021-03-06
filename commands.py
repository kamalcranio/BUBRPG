from creator import *

# Global variables, defines party selection (int sel), party size (list party)
# and selector (int bagslct)

sel = 0
party = [None]*5
bagslct = 0

def zeroAttr(kind):
# This funcion is used whenever an item leaves the selected player's hand
# Whatever attributes have been changed by an item are reversed.
	party[sel].hp -= party[sel].wearing[kind].hpdiff
	party[sel].mp -= party[sel].wearing[kind].mpdiff
	party[sel].sta -= party[sel].wearing[kind].stadiff
	party[sel].spd -= party[sel].wearing[kind].spddiff
	party[sel].curatk -= party[sel].wearing[kind].itatk
	party[sel].curdef -= party[sel].wearing[kind].itdef
	party[sel].atkpwr /= party[sel].wearing[kind].atkpwrdiff
	party[sel].defpwr /= party[sel].wearing[kind].defpwrdiff
	party[sel].healpwr /= party[sel].wearing[kind].healpwrdiff
	
def refreshAttr(kind):
# This function updates the player's attributes based on the new items'
	party[sel].hp += party[sel].wearing[kind].hpdiff
	party[sel].mp += party[sel].wearing[kind].mpdiff
	party[sel].sta += party[sel].wearing[kind].stadiff
	party[sel].spd += party[sel].wearing[kind].spddiff
	party[sel].curatk += party[sel].wearing[kind].itatk
	party[sel].curdef += party[sel].wearing[kind].itdef
	party[sel].atkpwr *= party[sel].wearing[kind].atkpwrdiff
	party[sel].defpwr *= party[sel].wearing[kind].defpwrdiff
	party[sel].healpwr *= party[sel].wearing[kind].healpwrdiff


def addToBag(toitem):
# This is blemished code that took me too long to get working.
# I'd much rather not talk about it, but this function just
# adds whatever item called by the "toitem" var.
	for n in range(len(party[sel].bag)):
		if party[sel].bag[n] is None:
			party[sel].bag[n] = toitem
			print("Added {0} to bag. Position {1}".format(party[sel].bag[n].name, n))
			return 0
	
	print("No more space in the bag!")



def remFromBag(bagslct):
# Removes items from bag
	party[sel].bag[bagslct] = None
	bagSort()
				

def bagSort():
# It just sorts empty spaces in the bag, pushing them to
# the end of the list
    tempBag = []
    for i in range(len(party[sel].bag)):
        if party[sel].bag[i] is not None:
            tempBag.append(party[sel].bag[i])

    remainingAmount = party[sel].bagsize - len(tempBag)
    tempBag += [None] * remainingAmount
    party[sel].bag = tempBag



def wearItem(item):
# It checks whether or not the selected player's hands
# has an item already on it. Changes items if needed.
	if item is None:
		print("There's no item in that bag's position!")	
	elif party[sel].wearing[item.kind] is None:
		party[sel].wearing[item.kind] = item
		print("Using {0}".format(party[sel].wearing[item.kind].name))
		refreshAttr(item.kind)
		remFromBag(bagslct)
	else:
		zeroAttr(item.kind)
		addToBag(party[sel].wearing[item.kind])
		party[sel].wearing[item.kind] = item
		remFromBag(bagslct)
		refreshAttr(item.kind)
		print("Using {0}".format(party[sel].wearing[item.kind].name))
		


def addParty(p):
# Adds a character to the party, considering there is a free slot
# TODO: Add character swap logic
	global party
	for n in range(len(party)):
		if party[n] is None:
			party[n] = p
			print("Character {0} added to party in position {1}".format(party[n].name, n))
			return 0
		else:
			print("Slot {0} contains: {1}".format(n, party[n].name))
		


def newGame():
# This is mostly a test function, I don't expect this to stay here in the future.
# TODO: Implement an actual "new game" function. Though this is probably need to be
# done once I get a primitive interface going.
	global sel
	global bagslct
	p1 = Person(name = "Hero")
	addParty(p1)
	wdswd = Wearable(name = "Wooden Sword", itatk = 5)
	lthcap = Wearable(name = "Leather Cap", itdef = 1, kind = 1)
	cotsht = Wearable(name = "Cotton Shirt", itdef = 5, kind = 2)
	cotleg = Wearable(name = "Cotton Pants", itdef = 5, kind = 3)
	lthbot = Wearable(name = "Leather Boots", itdef = 3, kind = 4)
	addToBag(wdswd)
	addToBag(lthcap)
	addToBag(cotsht)
	addToBag(cotleg)
	addToBag(lthbot)
	wearItem(party[sel].bag[bagslct])
	wearItem(party[sel].bag[bagslct])
	wearItem(party[sel].bag[bagslct])
	wearItem(party[sel].bag[bagslct])
	wearItem(party[sel].bag[bagslct])

