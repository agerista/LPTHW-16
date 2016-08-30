from sys import argv # create you new file here

script, filename = argv

print "We're going to erase %r." % filename # make sure you want to empty
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # new contents of file
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) # you will see these in file
target.write("\n")
target.write(line2)
target.write("n")
target.write(line3)
target.write("\n")

print "And finally, we close it." # saving and closing file
target.close()