import pandas as pd 
import psycopg2
from psycopg2 import sql
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import os



db = "dbname='DIS_project' user='postgres' host='localhost' password='12345678'" #potentially wrong password
conn = psycopg2.connect(db)


def user_sql(value, country_1, country_2):
    sql_string = f"""
    SELECT * FROM {value}
    where name in ('{country_1}','{country_2}');
    """
    print(sql_string)
    df = pd.read_sql_query(sql.SQL(sql_string),conn)
    df = df.rename(columns={'name':'Country'})
    df = df.set_index('Country')
    df = df.round(5)
    df = df.drop('code',1)
    df = df.fillna(0.0)
    df = df.transpose()

  

    df.plot(kind = 'line', ylabel = value, title = value + ' ' + 'for selected countries', xlabel = 'Year')
    #plt.savefig('..\Static\Comparison' + value + '.png')

    my_cwd = os.getcwd()
    my_cwd = r'{}'.format(my_cwd)
    filename = 'Comparison.png'
    static_part = 'static'
    source_part = 'source'
    path_file = os.sep.join([my_cwd, source_part, static_part, filename])

    plt.savefig(path_file)
    return 0


