import sys
import importlib
from io import StringIO
from time import time
class Tester:
	def __init__(self, testModuleName, testFolder, numberOfTests, maxDuration):
		self.testModuleName = testModuleName
		self.testFolder = testFolder
		self.numberOfTests = numberOfTests
		self.maxDuration = maxDuration

	def runAllTests(self):
		fails = 0
		meanDuration = 0
		lineJumpChar = "\n"
		print(f"Running tests of {self.testModuleName}...")
		print("---------------------------------------------------------------------")
		startTime = time()
		for i in range(1, self.numberOfTests + 1):
			testResult, testDuration, expectedResult, realResult = self.runTest(i)
			meanDuration += testDuration
			if not testResult:
				print(f"Test {i}: Failed Duration: {testDuration}")
				print(f"	Expected: {expectedResult.removesuffix(lineJumpChar)} Real: {realResult.removesuffix(lineJumpChar)}")
				fails += 1
			elif testDuration > self.maxDuration:
				print(f"Test {i}: Failed Duration: {testDuration}")
				fails += 1
			else:
				print(f"Test {i}: Success Duration: {testDuration}")
		endTime = time()
		print("---------------------------------------------------------------------")
		meanDuration = meanDuration / self.numberOfTests
		print(f"Successes: {self.numberOfTests - fails} Fails: {fails} Average duration per test: {meanDuration}")
		print(f"Total duration: {endTime - startTime}")
		if meanDuration > self.maxDuration:
			print("Hurry up andouille")
		if fails > 0:
			print("Motivational quote: git gud")


	def runTest(self, testId):
		testInputFileName = self.testFolder + (str(testId) if testId >= 10 else "0" + str(testId))
		testExpectedResultFileName = testInputFileName + ".a"

		with open(testInputFileName) as file:
			strInput = file.read()

		original_stdout = sys.stdout
		with StringIO(strInput) as inputs, StringIO() as output:
			sys.stdin = inputs
			sys.stdout = output
			startTime = time()
			importlib.import_module(self.testModuleName)
			endTime = time()
			del sys.modules[self.testModuleName]
			realResult = output.getvalue()
		sys.stdout = original_stdout

		with open(testExpectedResultFileName, "r") as output:
			expectedResult = output.read()

		return realResult == expectedResult, endTime - startTime, expectedResult, realResult

	def displayResults(self, testId):
		testInputFileName = self.testFolder + (str(testId) if testId >= 10 else "0" + str(testId))

		with open(testInputFileName) as file:
			strInput = file.read()

		with StringIO(strInput) as inputs:
			sys.stdin = inputs
			importlib.import_module(self.testModuleName)
			del sys.modules[self.testModuleName]

tester = Tester("problem_a", "./tests/a/", 10, 2)
# tester.runAllTests()
tester.displayResults(1)

# tester = Tester("problem_b", "./tests/b/", 11, 2.5)
# tester.runAllTests()
