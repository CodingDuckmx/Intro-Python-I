"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('src/foo.txt') as f:
    
    for line in f:
        print (line, end = ' ')
    
    f.close()

print(''' 

''')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open('src/bar.txt', 'w')

text = ''' Lambda School is 100 percent live and online, and uses interactive technology to teach people the tech skills they need to launch a new career in just 9 months.
Lambda is designed for student success.
We’re in this together, from your first day of classes to your first day on the job — and beyond.
        '''

f.write(text)
f.close()

with open('src/bar.txt') as f:
    for line in f:
        print(line, end=' ')

    f.close()