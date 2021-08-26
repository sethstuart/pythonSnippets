import datetime
import logging
import os


def interview_function(intArg1, intArg2):
    print(f’{intArg1} has completed 1/3 of the test’)
    d = 1
    while d < 38:
        newArg = intArg2 * d
        if d == 37:
            print(f’My favorite number is {newArg}!’)
            print(f’{intArg1} has completed 2/3 of the test’)
        d += 1
    os.chdir(f’/home/{intArg1}/Desktop/’)
    try:
        newFile = open(‘intLog.txt’, mode = ’r’, encoding=’utf-8’)
        newFile.close()
        print(‘file exists, continuing’)
        
    except:
        print(f’no file exists, making file in directory: {os.getcwd()}’)
        newFile = open(‘intLog.txt’ mode = ‘x’, encoding=’utf-8’)
        newFile.close()

    logging.basicConfig(level=logging.DEBUG, filename=’intLog.txt’, filemode=’a’)
    logging.debug(f‘{intArg1} has completed the test at {datetime.datetime.now()}’)
