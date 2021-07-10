import csv

def generate_html_elements(country_count, country_name):
    html_element = "<option class='selectOption' value='{}'>{}</option>".format(country_count, country_name)
    print(html_element)
    with open('countryhtmlelements.txt', 'a') as the_file:
        the_file.write(f"{html_element}\n")

country_json_data = {}

def create_json_for_country_data(line_count, country,score):
    country_json_data[line_count] = {"country_name": country, "score": score}


with open('values.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        # generate_html_elements(line_count,row[0])
        create_json_for_country_data(line_count, row[0],row[1])
        line_count += 1
    print(f'Processed {line_count} lines.')
    print("Writing json file ")
    import json
    with open('country_json_data.json', 'w') as fp:
        json.dump(country_json_data, fp)
    print("DONE :-)")