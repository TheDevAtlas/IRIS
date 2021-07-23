#---Copyright 2021, Jacob McGowan, All Rights Reserved. Software Not For Public Or Financial Use---#
#----------------------------------------IRIS Version 0.2.0----------------------------------------#
#------------------------------------------July 23rd 2021------------------------------------------#

# IRIS Version 0.2.0 Has Three Scripts. Main, Trainer, and Predictor.
# Main - Controls The Interface And Starts The Other Scripts
# Trainer - Trains The Neural Network Or Creates One If It Does Not Exist Then Saves It
# Predictor - For Some Input Data What Will x Days Stock Price Be In Context With Input Data

#-# Import Trainer And Predictor #-#
import trainer as t
import predictor as p
#-# ---------------------------- #-#

while True:
    userInput = int(input('What Would You Like To Do? '))
    if userInput == 0:
        t.LoadNet()
    elif userInput == 1:
        t.SaveNet()
    elif userInput == 2:
        t.CreateNet()
    elif userInput == 3:
        t.TrainNet()
    elif userInput == 4:
        break