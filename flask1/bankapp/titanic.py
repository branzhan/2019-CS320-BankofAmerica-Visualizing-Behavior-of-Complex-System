import functools

from flask import Blueprint, flash, g, redirect,render_template,request,session,url_for,jsonify
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

import csv
import pandas as pd
import numpy as np

#from bankapp import get_db

titanic_df = pd.DataFrame()
survived = pd.DataFrame()

bp = Blueprint("titanic", __name__, url_prefix="/titanic")

def init_db(app):
    titanic_df = pd.read_csv(app.root_path+"/static/data/train.csv")
    survived = titanic_df[(titanic_df['Survived']==1) & (titanic_df["Age"].notnull())]
    return

def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""
    percent = np.divide(val, total)
    return percent

@bp.route('/get_piechart_data')
def get_piechart_data():
    class_labels = ['Class I', 'Class II', 'Class III']

    titanic_df = pd.read_csv(bp.root_path+"/static/data/train.csv")
    survived = titanic_df[(titanic_df['Survived']==1) & (titanic_df["Age"].notnull())]

    pclass_percent = calculate_percentage(survived.groupby('Pclass').size().values, survived['PassengerId'].count())*100

    pieChartData = []
    for index, item in enumerate(pclass_percent):
        eachData = {}
        eachData['category'] = class_labels[index]
        eachData['measure'] =  round(item,1)
        pieChartData.append(eachData)

    return jsonify(pieChartData)

@bp.route('/get_barchart_data')
def get_barchart_data():

    titanic_df = pd.read_csv(bp.root_path+"/static/data/train.csv")
    survived = titanic_df[(titanic_df['Survived']==1) & (titanic_df["Age"].notnull())]

    age_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
    survived["age_group"] = pd.cut(survived.Age, range(0, 81, 10), right=False, labels=age_labels)
    survived[['age_group', 'Pclass']]

    survivorFirstClass = survived[survived['Pclass']==1]
    survivorSecondClass = survived[survived['Pclass']==2]
    survivorThirdClass = survived[survived['Pclass']==3]

    survivorAllclassPercent = calculate_percentage(survived.groupby('age_group').size().values,survived['PassengerId'].count())*100
    survivorFirstclassPercent = calculate_percentage(survivorFirstClass.groupby('age_group').size().values,survivorFirstClass['PassengerId'].count())*100
    survivorSecondclassPercent = calculate_percentage(survivorSecondClass.groupby('age_group').size().values,survivorSecondClass['PassengerId'].count())*100
    survivorThirdclassPercent = calculate_percentage(survivorThirdClass.groupby('age_group').size().values,survivorThirdClass['PassengerId'].count())*100

    barChartData = []
    for index, item in enumerate(survivorAllclassPercent):
        eachBarChart = {}
        eachBarChart['group'] = "All"
        eachBarChart['category'] = age_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)


    for index, item in enumerate(survivorFirstclassPercent):
        eachBarChart = {}
        eachBarChart['group'] = "Class I"
        eachBarChart['category'] = age_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(survivorSecondclassPercent):
        eachBarChart = {}
        eachBarChart['group'] = "Class II"
        eachBarChart['category'] = age_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(survivorThirdclassPercent):
        eachBarChart = {}
        eachBarChart['group'] = "Class III"
        eachBarChart['category'] = age_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    return jsonify(barChartData)

@bp.route('/')
def index():
    return render_template('titanic_home.html')
