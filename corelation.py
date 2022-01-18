import plotly.express as px
import csv
import numpy as np

def getDataSource(datapath):
    percentage=[]
    present=[]
    with open(datapath) as csv_file:
        csvreader=csv.DictReader(csv_file)
        for row in csvreader:
            percentage.append(float(row["Marks In Percentage"]))
            present.append(float(row["Days Present"]))
    return{"x":present,"y":percentage}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Student Marks vs Days Present:  \n",corelation[0,1])

def setup():
    datapath="Student Marks vs Days Present.csv"
    dataSource=getDataSource(datapath)
    findCorelation(dataSource)
setup()