import csv
with open('fixed.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # We have one "row" now.  Pick out the element named 'INFO' which might
        # contain multiple fields separated by commas.
        element = row['INFO']
        # Make a list named "fields" with elements split at the commas.
        fields = element.split(',')
        # Set up an empty list for output
        output_list = []

        for field in fields:
            # "field" is one of the possibly many elements in "fields"
            # We want to keep field if it doesn't match
            if "EFF=INTRON(MODIFIER;;;;;" not in field:
                # Appending it to the output_list is how we keep it
                output_list.append(field)

        # Now output_list has all the fields we want to print
        for item in output_list:
            # item is one of the fields, and we're in the row identified by "KeyID"
            keystr = str(row['KeyID'])
            # Only the first item starts with "EFF="
            if "EFF=" in item:
                print keystr, item
            # For each non-first item, indent the item by a pleasing number of spaces.
            else:
                print " "*(len(keystr)+len("EFF=")), item
