import time
from random import randint

import sys
from io import StringIO

def runProblemA():
	import problemA
	try:
		del sys.modules['problemA']
	except AttributeError:
		pass

def generateRandomInputs():
	n = 2000
	numberOfHitchhikers = 2000
	initialFuel = randint(0, 1e9)

	postHitchhikers = []
	for i in range(n + 1):
		postHitchhikers.append([])

	for i in range(numberOfHitchhikers):
		origin = randint(0, n - 1)
		destination = n
		if origin + 1 != n:
			destination = randint(origin + 1, n)
		food = randint(0, 1e9)
		fuel = randint(0, 1e9)
		postHitchhikers[origin].append([str(destination), str(food), str(fuel)])

	return (n, numberOfHitchhikers, initialFuel, postHitchhikers)

def testProblemA():
	inputs = generateRandomInputs()

	stringInput = " ".join(map(str, inputs[:3]))
	postHitchhikers = inputs[3]
	for postId in range(len(postHitchhikers)):
		for hitchhiker in postHitchhikers[postId]:
			stringInput += "\n" + str(postId) + " " + " ".join(hitchhiker)
	sys.stdin = StringIO(stringInput)

	start = time.time()
	runProblemA()
	end = time.time()
	totalTime = end - start
	return totalTime

print("Running tests...")
print("--------------------------------------------")
NUMBER_OF_TESTS = 50
numberOfFails = 0
for i in range(NUMBER_OF_TESTS):
	test = testProblemA()
	if test > 2:
		numberOfFails += 1
	print(f"Test {i + 1}: {test}")

print("--------------------------------------------")
print("Number of successes: " + str(NUMBER_OF_TESTS - numberOfFails))
print("Number of fails: " + str(numberOfFails))
if numberOfFails > 0:
	print("Motivational quote: Git gud")
else:
	print("Motivational quote: Not too bad")

