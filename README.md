# Optimus-Learning:
A repository for our day-to-day projects at OptimusLogic.

# Problem Definition:
Read words/characters from a file and count the number of words,also count the repeated words in the file.

# Solution:
Programming Language used-Python 3.

-Import required libraries.

-Open a file in read mode to read the contents of the file and display the contents.

-A function to count the number of words.

-A function to count the repeated words.

-Display the total count of words.

-Display the repeated words along with their counts.

# Algorithm:
Step 1:Open the text file in read mode.

Step 2:Read & store data in a variable.

Step 3:Print contents of text file stored in the variable.

Step 4:Declare a variable to count the number of words and initialize it to zero.

Step 5:Declare a dictionary for holding count values of each word.

Step 6:Replace all punctuations by an empty space and split the file data into words.

Step 7:Calculate total number of words in file.

Step 8:Print total number of words.

Step 9:for loop to iterate through the words.

  for word in words:
            if word in counts:                  
                      counts[word] += 1               
            else:                              
                      counts[word] = 1
Step 10:Print the repeated words along with their occurances.

# User Manual:
1.Enter the text file name along with.txt format when prompted for the filename.

2.The output will be displayed as follows:

-The contents of the given filename.

-Number of words in the file.

-A table form containing the words along with their occurances.
