import csv
import os

# List of input files
input_files = [
    './data/daily_sales_data_0.csv',
    './data/daily_sales_data_1.csv',
    './data/daily_sales_data_2.csv'
]

output_file = './data/formatted_sales_data.csv'

with open(output_file, mode='w', newline='') as out_csv:
    writer = csv.writer(out_csv)
   
    writer.writerow(['sales', 'date', 'region'])

    for file in input_files:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'].strip().lower() == 'pink morsel':
                    try:
                        quantity = int(row['quantity'])
                        price = float(row['price'].replace('$', ''))
                        sales = quantity * price
                        writer.writerow([f"{sales:.2f}", row['date'], row['region']])
                    except (ValueError, KeyError) as e:
                        print(f"Skipping row due to error: {e}")
