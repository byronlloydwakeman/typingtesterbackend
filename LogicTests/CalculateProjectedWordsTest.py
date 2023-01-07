from Logic.CalculateProjectedWords import CalculateProjectedWordsPerMinute as TestFunction

inputDataString = "A lion was sleeping"
inputDataTimeElapsed = 60
expected = 2
actual = TestFunction(inputDataString, inputDataTimeElapsed)
print("True" if expected == actual else f'expected: {expected} but actually got {actual}')