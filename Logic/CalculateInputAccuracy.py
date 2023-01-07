def FindWhiteSpacesInString(string):
    whiteSpaceIndicies = []
    for charIndex in range(0, len(string)):
        if string[charIndex] == " ":
            whiteSpaceIndicies.append(charIndex)
    return whiteSpaceIndicies


def CalculateInputAccuracy(userInput: str, targetInput: str):
    # Check that target input 'contains' user input
    noOfCorrectWords = 0
    indexOfIncorrectChars = []

    # Check input isn't blank or whitespace
    if(len(userInput) == 0 or userInput.isspace() == True):
        return 0

    if(userInput in targetInput):
        return 100
    else: # Whats incorrect?
        userInputArray = userInput.split()
        targetInputArray = targetInput.split()
        for i in range(0, len(userInputArray)):
            if(userInputArray[i] == targetInputArray[i]):
                noOfCorrectWords += 1

        return (noOfCorrectWords / len(userInputArray)) * 100 if noOfCorrectWords != 0 else 0

    # The above code works as long as the spaces are in the correct place


