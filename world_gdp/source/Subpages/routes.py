from flask import render_template, url_for, flash, redirect, request, Blueprint, Response
from source import app, conn, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from source.models import Customers, select_Customers, select_Employees
import pandas as pd 
import psycopg2
from psycopg2 import sql
from source.Subpages import query 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt



Subpages = Blueprint('Subpages', __name__)


def countries():
    sql_string = f"""
    SELECT distinct name FROM gdp
    ;
    """
    df = pd.read_sql_query(sql.SQL(sql_string),conn)
    df = df.sort_values('name')
    countrylist = df.name.tolist()

    return countrylist

posts = {
  "countries": countries(),
  "hasgraph": False 
}

@Subpages.route("/")
@Subpages.route("/home")
def home():
    return render_template('home.html')


@Subpages.route("/gdp")
def gdp():
    return render_template('gdp.html', title='GDP', posts=posts)

@Subpages.route("/data",methods=('GET','POST'))
def get_graph():
    if request.method == 'POST':
        country_1 = request.form["country_1"]
        country_2 = request.form["country_2"]
        measure = request.form['Measure']
        query.user_sql(measure, country_1=country_1, country_2=country_2)
        posts['hasgraph'] = True   

    return render_template('gdp.html', title=measure, posts=posts)