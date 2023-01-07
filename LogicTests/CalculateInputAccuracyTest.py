from Logic.CalculateInputAccuracy import CalculateInputAccuracy as CalcInpAcc

def TestFunction(userInput, targetInput, expected):
    actual = CalcInpAcc(userInput, targetInput)
    print("True" if expected == actual else f'expected: {expected} but actually got {actual}')

userInput = "A lion waz sleeping"
targetInput = "A lion was sleeping"

expected = 75

TestFunction(userInput, targetInput, expected)
TestFunction("A lion was sleeping", "A lion was sleeping", 100)
TestFunction("B ", "A lion was sleeping", 0)