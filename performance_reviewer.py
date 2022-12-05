import sys
import importlib
from io import StringIO
from time import time
from random import randint
class PerformanceReviwer:
	def __init__(self, testModuleName, maxDuration, inputGenerator, numberOfIterations):
		self.testModuleName = testModuleName
		self.maxDuration = maxDuration
		self.inputGenerator = inputGenerator
		self.numberOfIterations = numberOfIterations

	def generateInput(self):
		return self.inputGenerator()

	def runPerformanceReview(self):
		meanDuration = 0
		fails = 0
		print(f"Reviewing {self.testModuleName}...")
		print("---------------------------------------------------------------------")
		startTime = time()
		for i in range(1, self.numberOfIterations + 1):
			testDuration = self.perform()
			meanDuration += testDuration
			if testDuration > self.maxDuration:
				print(f"Test {i}: Failed Duration: {testDuration}")
				fails += 1
			else:
				print(f"Test {i}: Success Duration: {testDuration}")
		endTime = time()
		print("---------------------------------------------------------------------")
		meanDuration = meanDuration / self.numberOfIterations
		print(f"Successes: {self.numberOfIterations - fails} Fails: {fails} Average duration per test: {meanDuration}")
		print(f"Total duration: {endTime - startTime}")
		if fails > 0:
			print("Motivational quote: git gud")

	def perform(self):
		original_stdout = sys.stdout
		with StringIO(self.generateInput()) as inputs, StringIO() as output:
			sys.stdin = inputs
			sys.stdout = output
			startTime = time()
			importlib.import_module(self.testModuleName)
			endTime = time()
			del sys.modules[self.testModuleName]
		sys.stdout = original_stdout

		return endTime - startTime


def problemAInputGenerator():
	n = randint(2, 2000)
	m = randint(0, 2000)
	f = randint(1, 1e9)
	t = randint(1, n)
	stringInput = f"{n} {m} {f} {t}"
	for i in range(m):
		origin = randint(1, n)
		destination = randint(origin, n) if origin != n else n
		cans = randint(1, 1e9)
		gasoline = randint(1, 1e9)
		stringInput += f"\n{origin} {destination} {cans} {gasoline}"
	return stringInput


def problemBInputGenerator():
	n = randint(1, 30000)
	m = randint(1, 30000)
	s = randint(1, n)
	t = randint(1, n)
	stringInput = f"{n} {m} {s} {t}"
	for i in range(m):
		origin = randint(1, n)
		destination = randint(1, n)
		length = randint(1, 1e9)
		snow = randint(1, 1e9)
		stringInput += f"\n{origin} {destination} {length} {snow}"
	return stringInput

tester = PerformanceReviwer("problem_a", 2, problemAInputGenerator, 50)
tester.runPerformanceReview()

tester = PerformanceReviwer("problem_b", 2.5, problemBInputGenerator, 50)
tester.runPerformanceReview()