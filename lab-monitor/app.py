from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import csv
from time import time
from random import random
from flask import Flask, render_template, make_response


my_csv_file = "dummy.csv" #change this to your data file

"""
The data file should have the form:
    str(time), str(var1), str(var2), ...
    int, int, int, ...
    ..., ..., ..., ...
"""


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')



@app.route('/about.html', methods=["GET", "POST"])
def about():
    return render_template('about.html')



@app.route('/data', methods=["GET", "POST"])
def data():
    #data = [time() * 1000, random() * 100]
    
    #### Read in CSV instead
    with open(my_csv_file, 'r') as f:
        reader = csv.reader(f)
        final_line = list(reader)[-1]
        #header_line = list(reader)[-1]
        #print(list(reader)[2])
        try:
            data = [float(ele) for ele in final_line]
        except:
            print("WOAH! Does the file exist and is it's last line all numbers?")

    #### End open CSV
    
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True)
