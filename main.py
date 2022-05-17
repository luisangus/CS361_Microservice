if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import os
    import sys
    
    ## we can take the input file path and output image path as argument when the microservice is called
    if len(sys.argv) == 2:
        pathOfTxtFile = sys.argv[1]
        pathOfImage = "image.jpg"  # saves to folder where microservice is located
    elif len(sys.argv) == 3:
        pathOfTxtFile = sys.argv[1]
        pathOfImage = sys.argv[2]
    else: ## if no arguments are passed then proceed with user interface
        ##Description of the microservice
        print("")
        print("\033[1;34;40m")    ## blue text
        print("*****************************************************************************")
        print("The purpose of this microservice is to receive a text file that contains")
        print("information to be plotted in a bar chart. This microservive will process")
        print("the information, plot the data and save the bar chart as a jpg.")
        print("*****************************************************************************")
        print("\033[0m")
        print("")
        print("\033[1;32;40m")    ##Green text
        pathOfTxtFile = input("Enter the file path of the text file you want to read\n")
        pathOfImage = "image.jpg"    # saves to folder where microservice is located
    #open and read file
    f = open(pathOfTxtFile, "r")
    lines = f.read().splitlines()
    # the first line is the categories and the 2nd line is the values of those categories
    categories = lines[0].split(",")
    values = lines[1].split(",")
    values = list(map(int, values))
    #assigning colors to the bars in the chart
    Colors = ['green', 'blue', 'purple']
    plt.bar(categories, values, color=Colors)
    plt.title(os.path.basename(pathOfTxtFile), fontsize=14)
    plt.grid(True)
    plt.savefig(pathOfImage)
    plt.show()
    print("\033[0m")

