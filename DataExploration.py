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

    print(" ")
    print("### 1. Column names and count. ")
    print("Training data columns : " + ", ".join(str(x) for x in training_column_name) + ".")
    print("Number of columns in the training data: {}.".format(len(training_column_name)))

    print("Test data columns : " + ", ".join(str(x) for x in test_column_name) + ".")
    print("Number of columns in the test data: {}.".format(len(test_column_name)))
    print(" ")
    print(" ")

    # 2. Identify the label and concatanate it with test data
    for i in training_column_name:
        if i not in test_column_name:
            possible_label = i

    print(" ")
    print("### 2. Label identification. ")
    user_answer = input(" '{}' is not in the test data. It might be a label, is it correct (y/n)? >>> ".format(possible_label))
    if user_answer == 'y':
        label = possible_label
    elif user_answer == 'n':
        not_done = True
        while not_done:
            user_answer = input("Please enter label name manually >>> ") # User manually specifying the label name
            if user_answer in training_column_name:
                not_done = False
                label = user_answer
            else:
                print(" '{}' is not in the training column name".format(user_answer))
    else:
        print("Let's start over.")
        sys.exit()       
    print(" Label '{}' will be dropped and the training data and test data will be combined for feature engineering process. ".format(label))
    
    temp_train = train.copy()
    temp_train = temp_train.drop([label], axis=1)
    Data = pd.concat([temp_train, test])

    print("Combined data is stored under variable named 'Data' (training + test) . ")
    print(" ")
    print(" ")

    # 3. NULL count analysis
    print(" ")
    print("### 3. NULL count. ")
    for i in list(Data):
        this_null_count = Data[i].isnull().sum()
        print("Column name: {} ----> Proportion of NULLs: {} / {}".format(i, this_null_count, Data.shape[0]))




    

        
if __name__ == "__main__":
    main(sys.argv)