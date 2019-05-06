import pandas as pd
import warnings
import os
import sys, getopt

def main(argv):

    # Let's check everything is ok
    if len(argv) < 2:
        print("Directory name needs to be specified.")
        sys.exit()
    elif argv[1] != "-d":
        print("Directory name flag should be '-d'.")
        sys.exit()
    elif len(argv) == 2:
        print("Data directory needs to be specified.")
        sys.exit()
    
    directory_name = argv[2]         
    
    cwd = os.getcwd() # current directory
    try:
        train = pd.read_csv(cwd + '/' + directory_name + '/train.csv')
        test = pd.read_csv(cwd + '/' + directory_name + '/test.csv')
    except:
        print("Either training file or test file doesn't exist. Please try to save file in the format of 'train.csv' and 'test.csv' format. ")
        sys.exit()
    
    # 1. Analysis one: Extract columns of training and test data. Conventionally, training data has exactly one more column than test data.
    training_column_name = list(train)
    test_column_name = list(test)

    if len(training_column_name) != len(test_column_name)+1:
        # Number of column for training data is not 1 + number of column for test data
        print("Training data must have exactly one more column (label) than test data.")
        sys.exit()

    print("Training data columns : " + ", ".join(str(x) for x in training_column_name) + ".")
    print("Number of columns in the training data: {}.".format(len(training_column_name)))

    print("Test data columns : " + ", ".join(str(x) for x in test_column_name) + ".")
    print("Number of columns in the test data: {}.".format(len(test_column_name)))

    print("hos about now")
    

        
if __name__ == "__main__":
    main(sys.argv)