# Time conversion function.
# NB Please make sure there is a space between the time substring and the am/pm substrings. Also ensure that the am/pm substrings are in lowercase fore the code to work appropriately.
def time_conversion(time):
    """
    This function converts a given time from 12-hour format to 24-hour format.
    """
    t = time.replace(":", "") # Remove the colon from the time string

    if "am" in t and int(t[:2]) == 12:
        """
        If the time is in the morning and the hour is 12, 
        then the 24-hour format time is 00 with the minutes.
        """
        return "00" + t[2:4]
    elif "am" in t:
        """
        If the time is in the morning and the hour is not 12, 
        then the 24-hour format time is the hour with the minutes.
        """
        if len(t) == 6:
            return "0" + t[0:4]
        else:
            return t[:4]
    elif "pm" in t:
        """
        If the time is in the afternoon, 
        then the 24-hour format time is the hour plus 12 with the minutes.
        """
        if t[:2] == "12":
            return t[:4]
        elif len(t) == 6:
            return str(12 + int(t[:1])) + t[1:3]
        else:
            return str(12 + int(t[:2])) + t[2:4]




def positive(a, b, c):
    # Initialize positive count
    positive_count = 0

    # Check if a is positive and increment positive count
    if a > 0:
        positive_count += 1

    # Check if b is positive and increment positive count
    if b > 0:
        positive_count += 1

    # Check if c is positive and increment positive count
    if c > 0:
        positive_count += 1

    # Return true if positive count is 2, else false
    return positive_count == 2


def consonants(s):
    # define vowels for comparison
    vowels = 'aeiou'
    # initialize max value and current value
    max_value = 0
    current_value = 0

    # iterate through each letter in string
    for letter in s:
        # if letter is not a vowel
        if letter not in vowels:
            # increment current value
            current_value += ord(letter) - ord('a') + 1
        else:
            # update max value and reset current value
            max_value = max(max_value, current_value)
            current_value = 0

    # compare max value and current value after iteration
    max_value = max(max_value, current_value)

    return max_value





