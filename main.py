from utils.train import run as RunTrain

print('Select the action to perform.')

def send_help():
    print('0: Train a model                     1: Use trained model')
    print('2: Real time object detection        3: Display available cameras')
    print('4:                                   5:')
    print('6:                                   7:')
    print('8:                                   9:')
    print('H: Get help.                         Q: Quit program.')

send_help()

while(True):
    selection = input('>_ ')
    
    if(selection == '0'):
        try:
            RunTrain()
        except Exception as e:
            print("¡Unspected error!", e)
        else:
            print('Action finished correctly!')
        finally:
            print('Model train finished!')


    elif(selection == '1'):
        pass
    elif(selection == '2'):
        pass
    elif(selection == '3'):
        pass
    elif(selection == '4'):
            pass
    elif(selection == '5'):
            pass
    elif(selection == '6'):
            pass
    elif(selection == '7'):
            pass
    elif(selection == '8'):
            pass
    elif(selection == '9'):
            pass
    elif(selection.lower() == 'q'):
            break
    elif(selection.lower() == 'h'):
            send_help()
    else:
        print("Invalid option, try another option ID.")