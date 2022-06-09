from psycopg2 import sql
import psycopg2
import pandas as pd
from bank import conn




user_sql = sql.SQL("""
    SELECT * FROM gdp
    """)

df = pd.read_sql_query(user_sql,conn)
df_dk = df.loc[df['name'] == "Denmark"]
df_dk.plot.line()



