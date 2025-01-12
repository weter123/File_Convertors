import pandas as pd
import sqlite3

sql_file = input("Enter SQl filename:")
excel_file = input("Enter Excel Filename:")
conn = sqlite3.connect(f'{sql_file}.db')

query_statment = ("""SELECT name FROM sqlite_master 
    WHERE type='table';""")
table_list_df = pd.read_sql(query_statment,conn)
table_list = table_list_df['name'].tolist()


with pd.ExcelWriter(f'{excel_file}.xlsx') as writer:
    for table in table_list:
        query_statment = (f"SELECT * FROM {table};")
        table_df = pd.read_sql(query_statment,conn)
        table_df.to_excel(writer,sheet_name=table)