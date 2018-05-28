
# read categories file into duct
# keyphrase, category
# e.g. "Guzman"\t"Eating Out"

# Open categories file
catfile = open('categories.txt')

# Populate a dictionary with the keyword -> category hash values
categ=dict()
for line in catfile:
    content = line.split("\t")
    categ[content[0]]=content[1].rstrip()

# Done
catfile.close
print categ

# read qif file
#open i/o files
#for line in file:
#    if description-line:
#        for key in categ:
#            if key in line:
#                add categ[key]
#close files
