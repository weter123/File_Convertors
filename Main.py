import Excel_to_SQL as ets
import CSV_to_SQL as cts
import SQL_to_Excel as ste

def main():
    print("Welcome to converters.")
    print("1. Excel to SQL\n2. SQL to Excel \n3. CSV to SQL\nq. Quit")
    choice = input("please select convertor to use (1-3, q to quit): ")
    if choice == "1":
        ets.excel_to_sql()
    elif choice == "2":
        ste.sql_to_excel()
    elif choice == "3":
        ste.sql_to_excel()
    elif choice == "q":
        print("quitting")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()