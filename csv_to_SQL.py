import pandas as pd
import sqlite3


exit = False

while exit != True:
    try:
        sql_file = input("Enter SQl filename:")
        csv_file = input("Enter csv filename:")

        conn = sqlite3.connect(f'{sql_file}.db')

        csv_df = pd.read_csv(f'{csv_file}.csv')

        csv_df.to_sql(csv_file,conn,if_exists='replace',index=False)

    except Exception as error:
        print("Error has occured", error)
    else:
        exit = True
print("done!")



