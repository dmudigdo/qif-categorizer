# QIF CATEGORIZER
#
# Opens a QIF file of bank transactions and adds categories according to keywords.
# E.g. if the transaction description string contains "COLES", category is "Groceries" 
#
# View README.md for more details.

# Open input file
ifile = open('input.qif')

# Open output file
ofile = open('output.qif', 'w')

# For each line in the input file
for line in ifile:

    # If line is prefixed by 'P'...
    if line.startswith('P'):
        # It is a description field, so:

        # 1. Write out the line
        ofile.write(line)

        # 2a. Scan the line for 'COLES' or 'WOOLWORTHS'.
        #    If found, category is Groceries, write this to output file
        if 'COLES' in line or 'WOOLWORTHS' in line or 'CARLISLE IGA' in line:
            print('Found COLES or WOOLWORTHS or CARLISLE IGA')
            category = "Living Expenses:Groceries and Household Consumables"
            ofile.write('L'+category+'\n')
        # endif

        # 2b. Scan the line for 'SUBWAY' or 'GLORIA' or 'MCDONALDS' or 'DOME '.
        #    If found, category is Eating Out, write this to output file
        elif 'SUBWAY' in line or 'GLORIA' in line or 'MCDONALDS' in line or 'DOME ' in line:
            print('Found SUBWAY or GLORIA or MCDONALDS or DOME')
            category = "Leisure:Eating Out"
            ofile.write('L'+category+'\n')
        # endif

        # 2c. Scan the line for 'SMARTRIDER' or 'PUBLIC TRANSPORT'.
        #    If found, category is Transportation:EZ-Link Recharge, write this to output file
        elif 'SMARTRIDER' in line or 'PUBLIC TRANSPORT' in line:
            print('Found SMARTRIDER or PUBLIC TRANSPORT')
            category = "Transportation:EZ-Link Recharge"
            ofile.write('L'+category+'\n')
        # endif
        
        # 2d. Scan the line for 'ALDIMOBILE'.
        #    If found, category is < 100% Peachy Expense, write this to output file
        elif 'ALDIMOBILE' in line:
            print('Found ALDIMOBILE')
            category = "< 100% Peachy Expense"
            ofile.write('L'+category+'\n')
        # endif

        # 2e. Scan the line for 'KMART'.
        #    If found, category is < 100% Peachy Expense, write this to output file
        elif 'KMART' in line:
            print('Found KMART')
            category = "Living Expenses:Household Hardware"
            ofile.write('L'+category+'\n')
        # endif

        # 2f. Scan the line for 'AUST UNITY'.
        #    If found, category is < 100% Peachy Expense, write this to output file
        elif 'AUST UNITY' in line:
            print('Found AUST UNITY')
            category = "Health and Medical"
            ofile.write('L'+category+'\n')
        # endif

        # 2g. Scan the line for 'AUST UNITY'.
        #    If found, category is < 100% Peachy Expense, write this to output file
        elif 'BETHEL CHURCH' in line:
            print('Found BETHEL CHURCH')
            category = "Spiritual"
            ofile.write('L'+category+'\n')
        # endif

        # (can write some more if statements here for other categories/keywords)
        # (suggestions welcome on how to make this more elegant)
    else:
    # Else, it is not a description field, so write it straight out into the output file
        ofile.write(line)
    # endif
#Endfor

# Close the files
ifile.close()
ofile.close()


