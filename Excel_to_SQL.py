import pandas as pd
import sqlite3



def excel_to_sql():
    exit = False
    while exit != True:
        try:
            sql_file = input("Enter SQl filename:")
            excel_file = input("Enter Excel Filename:")

            conn = sqlite3.connect(f'{sql_file}.db')

            excel_df = pd.ExcelFile(f'{excel_file}')
            sheets_num = len(excel_df.sheet_names)
            print(sheets_num)
            sheet =0

            while sheet < sheets_num:
                sheet_name = excel_df.sheet_names[sheet]
                df = excel_df.parse(sheet_name)
                df.to_sql(sheet_name,conn,if_exists='replace',index=False)
                df.to_csv(f'{sheet_name}.csv', index=False)
                sheet = sheet + 1
            
        except Exception as error:
            print("Error has occured", error)
        else:
            exit = True
    print("done!")







