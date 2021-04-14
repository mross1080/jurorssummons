import csv
import redis
import json
import sys

REDIS_HOST = 'redis-14390.c256.us-east-1-2.ec2.cloud.redislabs.com'
zipcode_data = {}

def read_csv_data(csv_file):
    with open("ny_zc.csv") as csvf:
        print("loaded data")
        csv_reader = csv.reader(csvf, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # print(row)
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # zipcode = rowp[0]
                # white_pct = row[1]
                # unemp_rate = row[7]
                # median_income = row[13]
                data_for_zipcode = {
                    "zipcode" : row[0],
                    "white_pct" : row[1],
                    "unemp_rate" : row[7],
                    "median_income" : row[13]
                }
                zipcode_data[row[0]] = data_for_zipcode
                print(
                    data_for_zipcode)
                line_count += 1
        print(f'Processed {line_count} lines.')
    with open('zipcode_data.txt', 'w') as outfile:
        json.dump(zipcode_data, outfile)
    # return [(r[ik], r[iv]) for r in csv_data]

# def store_data(conn, data):
#     for i in data:
#         conn.setnx(i[0], i[1])
#     return data


def main():

    # columns = (0, 1) if len(sys.argv) < 4 else (int(x) for x in sys.argv[2:4])
    data = read_csv_data("ny_zc.csv")
    conn = redis.Redis(host=REDIS_HOST, port='14390',
                       password='EEDPLADvHhC12ziP5B2m2skqO7ZRv24i')
    # print (json.dumps(store_data(conn, data)))


if '__main__' == __name__:
    main()
