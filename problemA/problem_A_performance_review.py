import time
from random import randint

import sys
import ast
import types

with open("problemA.py") as f:
   p = ast.parse(f.read())

for node in p.body[:]:
    if not isinstance(node, ast.FunctionDef):
        p.body.remove(node)

module = types.ModuleType("mod")
code = compile(p, "mod.py", 'exec')
sys.modules["testedMod"] = module
exec(code,  module.__dict__)

import testedMod


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
		postHitchhikers[origin].append([destination, food, fuel])

	return (n, numberOfHitchhikers, initialFuel, postHitchhikers)

def testProblemA():
	inputs = generateRandomInputs()
	start = time.time()
	testedMod.test(inputs[0], inputs[1], inputs[2], inputs[3])
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

