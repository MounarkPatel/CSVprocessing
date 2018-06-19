#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:10:46 2018

@author: mounarkpatel
"""

"""
Code to convert CSV file into a list of dictionaries or dictionary of dictionaries.
Code to write a list of dictionaries into a CSV file.
A dictionary represents a row in CSV file
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    #function assumes first row of CSV file contains the field names
    csvtable = []
    with open(filename, "rt", newline = '') as csvfile:
        #open reader with delimeter and quotechar options to set seperator and quote
        csvreader = csv.reader(csvfile,
                               delimiter = separator, 
                               quotechar = quote)
        #easiest way to access a row
        for row in csvreader:
            csvtable.append(row) 
            #beak becuase you only need first row
            break
    #instead returning csvtable = [[]] lst is returned = []
    lst = csvtable[0]
    return lst


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    csvtable = []
    with open(filename, "rt", newline = '') as csvfile:
        #each row is a dictionary with DictReader
        csvreader = csv.DictReader(csvfile,
                               delimiter = separator, 
                               quotechar = quote)
        for row in csvreader:
            csvtable.append(row)
    return csvtable
        


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline = '') as csvfile:
        csvreader = csv.DictReader(csvfile,
                               delimiter = separator, 
                               quotechar = quote)
        for row in csvreader:
            """done becuase each row is accessed with a keyfield and to do key
            value mapping that information needs to be in table and equal row"""
            table[row[keyfield]] = row
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    
    with open(filename, "wt") as csvfile:
        #uses DictReader becuase rows are dictionaries
        #csv.QUOTE_NONNUMERIC because only non-numeric fields should be quoted
        writer = csv.DictWriter(csvfile,
                               delimiter = separator,
                               quotechar = quote,
                               quoting = csv.QUOTE_NONNUMERIC,
                               fieldnames = fieldnames)
        #all feildnames need to be written
        writer.writeheader()
        #write each row
        for row in table:
            writer.writerow(row)