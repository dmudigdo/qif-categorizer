# qif-categorizer
This Python script categorizes QIF (Quicken Interchange Format) bank transactions according to keywords in the description field.

## Motivation
When importing a bank-generated QIF file of transactions into [ClearCheckBook.com](http://clearcheckbook.com), categorization normally must be done manually after import. Automating this should be straightforward, e.g. if the description field contains "Coles" or "Woolworths", the category field "Groceries" should be added.

## QIF Format
According to [the Wikipedia entry for QIF](https://en.wikipedia.org/wiki/Quicken_Interchange_Format#Detail_items), for each transaction, categories have an 'L' prefix, while descriptions have a 'P' prefix. For example, here is the QIF entry for $6.15 spent on 25th February 2017, on McDonalds, with the category assigned to *Leisure:Eating Out*:

    D25/02/2017
    PMCDONALDS SOUTH PERTH - Visa Purchase - Receipt 180624
    LLeisure:Eating Out
    T-6.15
    ^

## What This Script Does
For uncategorized transactions, the task of categorization then becomes a simple matter of looping through each line in a QIF file, extracting the line with a 'P' prefix, checking the existence of a given keyword in that line (e.g. does the line starting with 'P' have 'COLES' in it?), then appending an 'L' prefixed line containing the category (e.g. "LGroceries").

## My Common Transactions

Category *Living Expenses:Groceries and Household Consumables* usually has a description that contains:

* COLES
* WOOLWORTHS

Category *Leisure:Eating Out* usually has a description that contains:

* SUBWAY
* GLORIA

Category *Transportation:EZ-Link Recharge* usually has a description that contains:

* SMARTRIDER
* PUBLIC TRANSPORT

## Improvements/To Do

Suggestions and comments are most welcome!

### Hardwired Filename
Currently, the filenames are hardwired into the code. This can be made more elegant, prompting the user for an input/output filename. 

### Hardwired Categories and Keywords
Currently, the categories and keywords are hardwired into the code. I am envisaging a method whereby the categories and matching keywords are kept in a separate (.txt?) file, and then read into a data structure of some sort (a dict?). Then, we can refactor the code so that it checks each description ('P' prefixed) line against this data structure containing all the keywords and categories.
