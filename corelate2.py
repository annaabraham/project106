import plotly.express as px
import csv

with open('cups of coffee vs hours of sleep.csv') as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,y="sleep in hours",x="Coffee in ml")
    fig.show()
