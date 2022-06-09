import pandas as pd 
from psycopg2 import sql
from bank import conn





def user_sql(value, country_1, country_2):
    sql_string = f"""
    SELECT * FROM '{value}'
    where name in ('{country_1}','{country_2}');
    """

    print(sql_string)
    df = pd.read_sql_query(sql.SQL(sql_string),conn)
    df.plot(style='.-')







