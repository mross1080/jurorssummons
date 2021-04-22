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
                    "zipcode": row[0],
                    "white_pct": row[1],
                    "black_pct": row[2],
                    "asian_pct": row[3],
                    "latino_pct": row[6],
                    "unemp_rate": row[7],
                    "commute_time": row[8],
                    "service_pct": row[9],
                    "construction_pct": row[10],
                    "finance_pct": row[11],
                    "maunfacturing_pct": row[12],
                    "median_income": row[13],
                    "health_insurance_pct": row[14],
                    "poverty_pct": row[15]
                }

                data_points = [
                    "{}% White Population".format(
                        data_for_zipcode["white_pct"]),
                    "{}% Black Population".format(
                        data_for_zipcode["black_pct"]),
                    "{}% Asian Population".format(
                        data_for_zipcode["asian_pct"]),
                    "{}% Latino Population".format(
                        data_for_zipcode["latino_pct"]),
                    "{} Unemployment Rate".format(
                        data_for_zipcode["unemp_rate"]),
                    "{} Minutes Average Commute Time".format(
                        data_for_zipcode["commute_time"]),
                    "{}% Work in the Service Industry".format(
                        data_for_zipcode["service_pct"]),
                    "{}% Work in the Construction Industry".format(
                        data_for_zipcode["construction_pct"]),
                    "{}% Work in the Finance Industry".format(
                        data_for_zipcode["finance_pct"]),
                    "{}% Work in the Manufacturing Industry".format(
                        data_for_zipcode["maunfacturing_pct"]),
                    "${} Median Income".format(
                        data_for_zipcode["median_income"]),
                    "{}% Have Health Insurance".format(
                        data_for_zipcode["health_insurance_pct"]),
                    "{}% Families live below the Poverty Line".format(
                        data_for_zipcode["poverty_pct"]),
                ]

                data_points_es = [
                    "{}% población blanca".format(
                        data_for_zipcode["white_pct"]),
                    "{}% población negra".format(
                        data_for_zipcode["black_pct"]),
                    "{}% población asiática".format(
                        data_for_zipcode["asian_pct"]),
                    "{}% población latina".format(
                        data_for_zipcode["latino_pct"]),
                    "{}% tasa de desempleo".format(
                        data_for_zipcode["unemp_rate"]),
                    "{} minutos, tiempo promedio de viaje al trabajo".format(
                        data_for_zipcode["commute_time"]),
                    "{}% Trabaja en la industria de servicio".format(
                        data_for_zipcode["service_pct"]),
                    "{}% Trabaja en la industria de construcción".format(
                        data_for_zipcode["construction_pct"]),
                    "{}% Trabaja en la industria de construcción".format(
                        data_for_zipcode["finance_pct"]),
                    "{}% Trabaja en la industria de manufactura".format(
                        data_for_zipcode["maunfacturing_pct"]),
                    "${} Ingreso medio".format(
                        data_for_zipcode["median_income"]),
                    "{}% Tiene seguro médico".format(
                        data_for_zipcode["health_insurance_pct"]),
                    "{}% Familias que viven debajo del nivel de pobreza".format(
                        data_for_zipcode["poverty_pct"]),
                ]

                zipcode_data[row[0]] = {"en": data_points, "es":data_points_es}
                # print(
                #     data_for_zipcode)
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
