import csv
import math

with open(r"WA_Sales_Products_2012-14.csv") as f:
    dane = csv.DictReader(f)
    avg_gross_margin = 0
    gross_margin = []
    count = 0
    for row in dane:
        try:
            avg_gross_margin += (float(row['Gross margin']))
            count += 1
            gross_margin.append((float(row['Gross margin'])))
        except Exception:
            pass
    average = avg_gross_margin / count
    print(average)

    minimum = min(gross_margin)
    print(minimum)

    maximum = max(gross_margin)
    print(maximum)

    slownik = dict()
    for line in dane:
        slownik.update({line['Year'], +(float(row['Gross margin']))})

    print(slownik)

    #     avg_gross_margin += float(row[-1])
    #     gross_margin.append(row[-1])
    # avg = avg_gross_margin/len(gross_margin)
    # print(avg)
