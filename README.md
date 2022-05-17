## Microservice to plot the money invested in a portfolio
__CS 361: Simple microservice created for Cameron Hollis by Luis Gonzalez__

### What the microservice does:
- Reads a .txt file. This file can be provided through the user interface or as an argument when running this microservice
- This microservice plot the data from the text file into a bar chart.
- It displays the barchart and saves it as a jpg. The default image title is image.jpg or it can be passed as an argument when running the microservice
- If the image.jpg already exist it will overwrite it.

** Please ensure pip is already installed on your machine.

### To use:
- Download the files from Github to your project directory.
- In the command line, install the matplotlib module for python. Run the following command to install the module:

python -m pip install -U matplotlib

- if your computer already has python 2.7 installed you will have to specify to call python 3.0 by doing the following:

python3 -m pip install -U matplotlib
