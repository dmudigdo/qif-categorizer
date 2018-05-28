
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

#open i/o files
# Open input file
ifile = open('input.qif')

# Open output file
ofile = open('output.qif', 'w')

for line in file:
#    if description-line:
    if line.startswith('P'):
        # It is a description field, so:
        # 1. Write out that descriptionline
        ofile.write(line)

        # 2a. Scan the line for 'COLES' or 'WOOLWORTHS'.
        #    If found, category is Groceries, write this category line to output file
        # DELETE THIS BLOCK ONCE YOU ARE DONE:
#        if 'COLES' in line or 'WOOLWORTHS' in line or 'CARLISLE IGA' in line:
#            print('Found COLES or WOOLWORTHS or CARLISLE IGA')
#            category = "Living Expenses:Groceries and Household Consumables"
#            ofile.write('L'+category+'\n')
        # endif

        # THIS BLOCK REPLACES THE ABOVE:
        # for each key in categ:
        for key in categ:
            if key in line:
                print('found ' + key)
                ofile.write('L'+ categ[key]) +'\n')
            # endif
         #endfor

    else:
    # else, it is not a description field, so write it straight out into the output file
        ofile.write(line)
    # endif
#endfor

# Close the files
ifile.close()
ofile.close()
