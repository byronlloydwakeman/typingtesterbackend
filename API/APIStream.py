from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

from Logic.CalculateProjectedWords import CalculateProjectedWordsPerMinute as CalcProjWordPerMin
from Logic.CalculateInputAccuracy import CalculateInputAccuracy as CalcInpAcc

app = FastAPI()

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class TypeDataModel(BaseModel):
    timeElapsed: int
    userInput: str
    targetInput: str

# Note that the program only works if spaces aren't in incorrect places
# So the UI must make sure that the user only enters spaces when there
# are actually spaces

@app.post("/CalcAverageWordsPerMinute/Post")
async def post(typeDataModel: TypeDataModel):
    # Call logic classes to process data
    try:
        wordspermin = CalcProjWordPerMin(typeDataModel.userInput, typeDataModel.timeElapsed)
        accuracy = CalcInpAcc(typeDataModel.userInput, typeDataModel.targetInput)
        return {
                "WordsPerMinute" : wordspermin,
                "Accuracy" : accuracy,
                "AdjustedWordsPerMinute" : wordspermin * (accuracy / 100)
            }
    except Exception as e:
        print(f'Error: {e.__str__()}')
        return {"Error": e.__str__()}
