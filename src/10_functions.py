# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):

    '''
    Returns true if the inserted value is an even number.
    '''

    ## Old code

    # if type(x) == int:
        
    #     if x % 2 == 0:

    #         return True
    
    # else:

    #     return False

    ## New code

    if type(x) == int and x % 2 == 0:
        
        return True
    
    return False


# Read a number from the keyboard
num = input("Enter a number: ")

try:
    num = int(num)

    # Print out "Even!" if the number is even. Otherwise print "Odd"

    # YOUR CODE HERE

    if is_even(num):

        print('Even!')

    else:

        print('Odd.')

except:

    print('Insert a integer.')


