#    for each transaction in a QIF file:
#        check the description field
#        if it contains ... then
#            insert category X
#        endif
#        if it contains ... then
#            insert category Y
#        endif
#        <etc. etc.>
#    endfor


# Open input file
ifile = open('input.qif')

# Open output file
ofile = open('output.qif', 'w')

# For each transaction line in the input file
for line in ifile:

    # If line is prefixed by 'M'...
    if line.startswith('P'):
        # It is a Memo, so do stuff:

        # 1. Write out the Memo
        ofile.write(line)

        # 2. Scan the line for 'COLES' or 'WOOLWORTHS'.
        #    If found, category is Groceries, write this to output file
        if 'COLES' in line or 'WOOLWORTHS' in line:
            print('Found COLES or WOOLWORTHS')
            category = "Living Expenses:Groceries and Household Consumables"
            ofile.write('L'+category+'\n')
        # endif

        if 'SUBWAY' in line or 'GLORIA' in line or 'MCDONALDS' in line:
            print('Found SUBWAY or GLORIA or MCDONALDS')
            category = "Leisure:Eating Out"
            ofile.write('L'+category+'\n')
        # endif

        # (write some more if statements here)        
    else:
    # It is not a Memo, so write it straight out into the output file
        ofile.write(line)
    # endif
#endfor

# Close the files
ifile.close()
ofile.close()


