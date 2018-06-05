# QIF CATEGORIZER VERSION 2
#
# Opens a QIF file of bank transactions and adds categories according to keywords.
# E.g. if the transaction description string contains "COLES", category is "Groceries" 
#
# View README.md for more details.


# read categories file into dictionary
# keyphrase, category
# e.g. "Guzman"\t"Eating Out"
#
# TODO: Die when categories.txt is not properly formatted as <keyword>\t<category>

# open categories file
catfile = open('categories.txt')

# populate a dictionary with the (keyword -> category) hash values
categ=dict()
for line in catfile:
    content = line.split("\t")
# Need a die clause here, when categories file not formatted properly!
    categ[content[0]]=content[1].rstrip()

# done 
catfile.close

# report categories
print ''
print "Categories found:"
for key in categ:
    print key + ' - ' + categ[key]

print ''
print 'Starting categorization...'
print ''

# open input file
ifile = open('input.qif')

# open output file
ofile = open('output.qif', 'w')

for line in ifile:
#   if it is a description-line:
    if line.startswith('P'):
        # It is a description field, so:
        # 1. Write out that descriptionline
        ofile.write(line)

        # 2. for each key in the categ dictionary:
        for key in categ:
            # find if the key is in the description line
            if key in line:
                # and if found, do the magic
                print('found ' + key + ', assigned to ' + categ[key])
                ofile.write('L'+ categ[key] +'\n')
            # endif
         #endfor

    else:
    # else, it is not a description field, so duplicate it into the output file
        ofile.write(line)
    # endif
#endfor

# Close the files
ifile.close()
ofile.close()

