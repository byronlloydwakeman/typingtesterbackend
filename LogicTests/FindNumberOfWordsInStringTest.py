from Logic.FindNumberOfWordsInString import FindNumberOfWordsInString as TestFunction

inputData = "1"
expected = 1
actual = TestFunction(inputData)
print("True" if expected == actual else f'expected: {expected} but actually got {actual}')