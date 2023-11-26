# toy-_problems

# Time Conversion Function
The time_conversion function in this code converts a given time from 12-hour format to 24-hour format. It expects the input time string to have a space between the time substring and the am/pm substrings. Additionally, the am/pm substrings should be in lowercase for the code to work appropriately.

Details
Function Explanation
The function follows these steps:

1.Remove the colon from the time string.
2.Check if the time is in the morning and the hour is 12. If so, the 24-hour format time is "00" with the minutes.
3.If the time is in the morning and the hour is not 12, the 24-hour format time is the hour with the minutes.
4.If the time is in the afternoon, the 24-hour format time is the hour plus 12 with the minutes.

Important Note
Ensure that there is a space between the time substring and the am/pm substrings, and the am/pm substrings are in lowercase for the code to work appropriately.

# Positive Numbers Function
The positive function checks if exactly two out of three integers are positive numbers. The function takes three integers (a, b, c) as arguments and returns True if exactly two of them are positive, and False otherwise.

# Consonant Values Function
The consonants function calculates the highest value of consonant substrings in a given lowercase string. Consonants are any letters of the alphabet except "aeiou".

Details
The function iterates through the string, identifies consonant substrings, calculates their values based on the mapping (a=1, b=2, ..., z=26), and returns the highest value. Ensure that there are no spaces in the input string, and all characters are alphabetic.