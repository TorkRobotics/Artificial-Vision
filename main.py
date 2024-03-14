from utils.train import run as RunTrain

print('Select an option to run:')
print('0: Train a model     1: Use trained model    2: Real time object detection')
selection = input('>_ ')

if(selection == '0'):
    RunTrain()