from utils.train import run as RunTrain

print('Choose an action.')
print('0: Train a model                     1: Use trained model')
print('2: Real time object detection        3: Display available cameras')
selection = input('>_ ')

if(selection == '0'):
    RunTrain()