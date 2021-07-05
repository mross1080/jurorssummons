import csv

def generate_html_elements(country_count, country_name):
    html_element = "<option class='selectOption' value='{}'>{}</option>".format(country_count, country_name)
    print(html_element)
    with open('countryhtmlelements.txt', 'a') as the_file:
        the_file.write(f"{html_element}\n")

with open('values.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        generate_html_elements(line_count,row[0])
        line_count += 1
    print(f'Processed {line_count} lines.')