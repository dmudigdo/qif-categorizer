# qif-categorizer
This Python script categorizes QIF (Quicken Interchange Format) bank transactions according to keywords in the description field. Tested working on Python 3.5.

## Usage
Create a file named "categories.txt" which contains tab-separated keyword->category data, one per line (see below for an example). Then:

    python3 qif-categorizer.py

## Motivation
When importing a bank-generated QIF file of transactions into [ClearCheckBook.com](http://clearcheckbook.com), categorization must be done manually after import. Automating this should be straightforward, e.g. if the description field contains "Coles" or "Woolworths", the category field "Groceries" should be added.

## QIF Format
According to [the Wikipedia entry for QIF](https://en.wikipedia.org/wiki/Quicken_Interchange_Format#Detail_items), for each transaction, categories have an 'L' prefix, while descriptions have a 'P' prefix. For example, here is the QIF entry for $6.15 spent on 25th February 2017, on McDonalds, with the category assigned to *Leisure:Eating Out*:

    D25/02/2017
    PMCDONALDS SOUTH PERTH - Visa Purchase - Receipt 180624
    LLeisure:Eating Out
    T-6.15
    ^

When importing a data file from the bank however, the category line (with an 'L' prefix) will be missing. Our job is to add that line.


## What This Script Does
This script first reads the categories.txt file into a dictionary of keywords -> category. Then it scans the .qif file (containing uncategorized transactions) for description lines (begins with 'P') and checks if it contains one of the keywords. If it does, it appends the matching category line (begins with 'L'). 

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

So the tab-separated categories.txt file looks like:

    COLES<tab>Living Expenses:Groceries and Household Consumables
    WOOLWORTHS<tab>Living Expenses:Groceries and Household Consumables
    SUBWAY<tab>Leisure:Eating Out
    GLORIA<tab>Leisure:Eating Out
    SMARTRIDER<tab>Transportation:EZ-Link Recharge
    PUBLIC TRANSPORT<tab>Transportation:EZ-Link Recharge

## Improvements/To Do

Suggestions and comments are most welcome!

### Hardwired Filename
Currently, the filenames are hardwired into the code. This can be made more elegant, prompting the user for an input/output filename. 

