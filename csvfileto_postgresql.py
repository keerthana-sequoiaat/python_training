import psycopg2
import csv

conn_params = {
    'dbname': 'sales_db',
    'user': 'postgres',
    'password': '',
    'host': 'localhost',
    'port': '5432'
}
try:
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS orders (
        ORDERNUMBER INTEGER,
        QUANTITYORDERED INTEGER,
        PRICEEACH FLOAT,
        ORDERLINENUMBER INTEGER,
        SALES FLOAT,
        ORDERDATE DATE,
        STATUS VARCHAR(50),
        QTR_ID INTEGER,
        MONTH_ID INTEGER,
        YEAR_ID INTEGER,
        PRODUCTLINE VARCHAR(50),
        MSRP INTEGER,
        PRODUCTCODE VARCHAR(50),
        CUSTOMERNAME VARCHAR(100),
        PHONE VARCHAR(20),
        ADDRESSLINE1 VARCHAR(100),
        ADDRESSLINE2 VARCHAR(100),
        CITY VARCHAR(50),
        STATE VARCHAR(50),
        POSTALCODE VARCHAR(50),
        COUNTRY VARCHAR(50),
        TERRITORY VARCHAR(50),
        CONTACTLASTNAME VARCHAR(50),
        CONTACTFIRSTNAME VARCHAR(50),
        DEALSIZE VARCHAR(50)
    )
    """
    try:
        cur.execute(create_table_query)
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()
    csv_file_path ='sales_data_sample.csv'

    try:
        with open(csv_file_path, mode='r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            next(reader)
            insert_query = """
            INSERT INTO orders(
                ORDERNUMBER, QUANTITYORDERED, PRICEEACH, ORDERLINENUMBER, SALES, ORDERDATE,
                STATUS, QTR_ID, MONTH_ID, YEAR_ID, PRODUCTLINE, MSRP, PRODUCTCODE, CUSTOMERNAME,
                PHONE, ADDRESSLINE1, ADDRESSLINE2, CITY, STATE, POSTALCODE, COUNTRY, TERRITORY,
                CONTACTLASTNAME, CONTACTFIRSTNAME, DEALSIZE
            ) VALUES (%s, %s, %s, %s, %s, TO_DATE(%s, 'MM/DD/YYYY'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for row in reader:
                try:
                    cur.execute(insert_query, row)
                except Exception as e:
                    print(f"Error inserting row {row}: {e}")
                    conn.rollback()
    except Exception as e:
        print(f"Error reading or processing the CSV file: {e}")
    conn.commit()

except Exception as e:
    print(f"Database connection error: {e}")

finally:
    if 'cur' in locals() and cur:
        cur.close()
    if 'conn' in locals() and conn:
        conn.close()