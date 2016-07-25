#! usr/bin/env python

# Python script to convert a page that was created with a form with multiple instance templates into a CSV file to be
# used with the mediawiki extension, Extension:Data Transfer.

import re, csv

# Open the text file containing wiki text of page to pull info into csv.
text_file = open('wiki_text.txt', 'r')

# First find all template calls and place into list
# Finds {{This Template<content>\n}}
template_calls = re.findall(r'(\{\{Template To Extract Info From.*?\n\}\})', text_file.read(), re.DOTALL)
text_file.close()

# Open the csv file that will be created.
csv_out = open('output_csv.csv', 'w', newline='')

data = csv.writer(csv_out)

# Write the first row of csv file
data.writerow(['Title',
              'Template A[Parameter W]',
              'Template B[Parameter X]',
              'Template C[Parameter Y]',
              'Template D[Parameter Z]'])

for call in template_calls:
    # Separate regexes because not all templates contain every argument.
    parameter_w_regex = re.compile(r'\|Parameter W=(.*)?\n(\||\}\})', re.DOTALL)
    parameter_x_regex = re.compile(r'\|Parameter X=(.*)?\n(\||\}\})', re.DOTALL)
    paramter_y_regex = re.compile(r'\|Parameter Y=(.*)?\n(\||\}\})', re.DOTALL)
    parameter_z_regex = re.compile(r'\|Parameter Z=(.*)?\n(\||\}\})', re.DOTALL)

    # Extract values of template parameters
    # If no value exists, then enter ''.
    try:
        parameter_w = parameter_w_regex.search(call).group(1)
    except AttributeError:
        parameter_w =''
    try:
        parameter_x = parameter_x_regex.search(call).group(1)
    except AttributeError:
        parameter_x = ''
    try:
        parameter_y = parameter_y_regex.search(call).group(1)
    except AttributeError:
        parameter_y = ''
    try:
        parameter_z = parameter_z_regex.search(call).group(1)
    except AttributeError:
        parameter_z = ''


    data.writerow([parameter_w, parameter_x, parameter_y, parameter_z])

del data
csv_out.close()