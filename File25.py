# copies the contents of one text file to another

file_orig = open('Assig_5.txt','r')
file_copy = open('Assign_2','w')
copy = file_orig.read()
file_copy.write(copy)