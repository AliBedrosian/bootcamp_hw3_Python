# bootcamp_hw3_Python
Alison McCondichie - Homework 3 - Python

The purpose of this homework was to show how to utilize Python code to analyze large volumes of data in a quick, repeatable way.

Importing the csv was tricky at first but I found that when I opened the parent folder of the project in Visual Studio Code it worked perfectly.****(note this did NOT work later)

The VBA homeowrk in week two was very helpful to find a starting point and general flow needed for looping through rows with an incrimenting total, and keeping track of a max and min. 

PyPoll had slightly more work to do only because it involved the use of dictionaries to keep track of the candidate and the votes. Once I understood the flow of calling on certain values in a dictionary with the .get method, this part was easier. 

I created a parent Submission folder with my written code and analysis, and a submission folder for each individual Python project for organization. 

***After my first submission attempt I found that unfortunately my code would not run if I tried to re-open it without having the entire parent folder open as well. I kept receiving a 'file not found' error. The the help of TA's I found a solution that has been working since. I added an extra line of code after importing the os and before attempting to read in the code. This line of code changed the directory to the directory of the Python script. This way the csv and txt files have a direct path to the script.
