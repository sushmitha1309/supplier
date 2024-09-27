import click
from supplier_app.cli.supplierLib.Database import Database
import os
import pandas as pd
import datetime
#import xlsxwriter

@click.group("supplier_cli")
@click.pass_context
def supplier_cli(ctx):
         """
         Component supplier_cli
         this has a basic method to execute a simple call but can be used as an example for new modules
         """

@supplier_cli.command("get_database_connection")
@click.option(
        "--hostname",
         prompt="Parameter description for user to read. It's possible to add as much parameters as needed and also optional parameters",
         help="More details about parameter or possible values",
     )
@click.pass_context
def get_database_connection(ctx, hostname):
    print(hostname)
    click.echo("Get Database Connection")
    db_obj = Database()
    cursor, conn = db_obj.connect_database("info")
    #cursor.execute("SELECT * from students;")
    #cursor.execute("INSERT INTO students(id,name,age,dob,gender)Values('5','tom','36','1990-09-8','F')")
    #cursor.execute("UPDATE students SET name='sushmitha' WHERE id='1'")
@supplier_cli.command("show_students_list")
@click.pass_context
def show_students_list(ctx):
    db_obj = Database()
    cursor = db_obj.connect_database("info")
    cursor.execute("SELECT * from supplier_T;")
    record = cursor.fetchall()
    for row in record:
        click.echo(row)

@supplier_cli.command("say_hi")
@click.option(
    "--param_option",
    prompt="Parameter description for user to read. It's possible to add as much parameters as needed and also optional parameters",
    help="More details about parameter or possible values",
)

@click.pass_context
def say_hi(ctx):
    click.echo("Get Database Connection")
    db_obj = Database()



@supplier_cli.command("parse_supplier")
@click.option(
    "--supplier_location",
    prompt="Please provide supplier directory location",
    help="Please provide supplier directory location",
)
@click.pass_context
def parse_supplier(ctx, supplier_location, part_number=None):
    click.echo("Retrieve supplier names")
    # get year from given path
    year = os.path.basename(os.path.normpath(supplier_location))

    for dirpath, dirnames, filenames in os.walk(supplier_location):
        # print(f"Current Directory: {dirpath}")

        #List all the subdirectories in the current directory
        # if dirnames:
        #     print(f"Subdirectories: {dirnames}")

        # List all files in the current directory
        for file in filenames:

            # check the file extension is csv or xlsx.

            full_filepath = dirpath + "\\" + file
            column_data = {}
            print(f"File: {dirpath}\\{file}")

            supplier_parts = file.split('_')

            column_data['supplier_name'] = supplier_parts[0].replace(".xlsx","")
            #supplier_code = ""

            # Read the excel file
            data = pd.read_excel(full_filepath, engine='openpyxl')
            data = data.astype(str)
            df = pd.DataFrame(data)



            for row in df.iterrows():
                # print(row)
                # check the row is header or not
                if 'part_number' in row[1]:
                    column_data['part_number'] = row[1]['part_number']
                else:
                    column_data['part_number'] = ""

                if 'part_description' in row[1]:
                    column_data['part_description'] = row[1]['part_description']
                else:
                    column_data['part_description'] = ""

                if 'gross_price' in row[1]:
                    column_data['gross_price'] = row[1]['gross_price']
                else:
                    column_data['gross_price'] = ""

                if 'net_price' in row[1]:
                    column_data['net_price'] = row[1]['net_price']
                else:
                    column_data['net_price'] = ""

                if 'discount_price' in row[1]:
                    column_data['discount_price'] = row[1]['discount_price']
                else:
                    column_data['discount_price'] = ""

                if 'MOQ' in row[1]:
                    column_data['MOQ'] = row[1]['MOQ']
                else:
                    column_data['MOQ'] = ""

                if 'currency' in row[1]:
                    column_data['currency'] = row[1]['currency']
                else:
                    column_data['currency'] = ""

                if 'origin_country' in row[1]:
                    column_data['origin_country'] = row[1]['origin_country']
                else:
                    column_data['origin_country'] = ""

                if 'core_surcharge' in row[1]:
                    column_data['core_surcharge'] = row[1]['core_surcharge']
                else:
                    column_data['core_surcharge'] = ""

                if 'first_date' in row[1]:
                    column_data['first_date'] = row[1]['first_date']
                else:
                    column_data['first_date'] = ""

                if 'last_date' in row[1]:
                    column_data['last_date'] = row[1]['last_date']
                else:
                    column_data['last_date'] = ""

                # first_date = datetime.date(int(year), 1, 1).strftime("%d-%m-%Y")
                # last_date = datetime.date(int(year), 12, 31).strftime("%d-%m-%Y")

                #Connect database
                db_obj = Database()
                cursor, conn = db_obj.connect_database("info")
                # Insert this values into database
                insert_query = "INSERT INTO supplier_new_format (first_date, last_date, part_number, part_description, gross_price, origin_country, supplier_name, net_price, discount_price, MOQ, currency, core_surcharge) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(insert_query, column_data['first_date'], column_data['last_date'], column_data['part_number'], column_data['part_description'], column_data['gross_price'], column_data['origin_country'], column_data['supplier_name'], column_data['net_price'], column_data['discount_price'], column_data['MOQ'], column_data['currency'], column_data['core_surcharge'])

                conn.commit()
        click.echo("Sheet imported into DB")
    click.echo("All are imported")
    #conn.close()

@supplier_cli.command("export_supplier")
@click.option(
    "--filename",
    prompt="Please provide supplier directory location",
    help="Please provide supplier directory location",
)
@click.pass_context
def export_supplier(ctx, filename):
    click.echo("Export One template database table into xlsx")

    db_obj = Database()
    cursor, conn = db_obj.connect_database("info")

    sql_query = "SELECT * FROM supplier_new_format"
    df = pd.read_sql_query(sql_query, conn)

    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, sheet_name="all_suppliers", index=False)
    writer._save()

    conn.close()
