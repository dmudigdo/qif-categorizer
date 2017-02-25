# qif-categorizer

Categorizes transactions in a QIF (Quicken Interchange Format) file according to keywords in the  description field.

## Motivation
When importing a bank-generated QIF file of transactions into ClearCheckBook.com, categorization must be done manually after import. This program will insert a category field into each transaction record, according to keywords in the description field. For example, if the description field contains "Coles" or "Woolworths", the category field "Groceries" will be added.

## QIF Format
According to [Wikipedia](https://en.wikipedia.org/wiki/Quicken_Interchange_Format#Detail_items), for each transaction, categories have an 'L' prefix, while descriptions have the 'M' (for Memo) prefix.

The task then becomes a matter of looping through each transaction in a QIF file, extracting the line with an 'M' prefix, checking the existence of a given keyword in that line (e.g. does the line starting with 'M' have 'Coles' in it?), then appending an 'L' prefixed line containing the category (e.g. "LGroceries").

## Pseudocode
Here is the pseudocode:

    for each transaction in a QIF file:
        check the description field
        if it contains ... then
            insert category X
        endif
        if it contains ... then
            insert category Y
        endif
        <etc. etc.>
    endfor

## To do

* ~Test whether or not ClearCheckBook accepts a category field in QIF imports, and how it matches it against it's internal category classification.~
* Write the program!