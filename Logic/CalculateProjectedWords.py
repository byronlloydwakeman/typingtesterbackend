from Logic.FindNumberOfWordsInString import FindNumberOfWordsInString as FindNoOfWorInStr

def CalculateProjectedWordsPerMinute(userInput, timeElapsed):
    if(timeElapsed != 0):
        multiplier = 60 / timeElapsed
    else:
        multiplier = 60

    return FindNoOfWorInStr(userInput) * multiplier
