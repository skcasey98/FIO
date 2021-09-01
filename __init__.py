#Kellen Casey
#8/30/2021
#FIO Awesome Inc.
#weather.py

#This is the flask file that is used to render the html pages and run the 
#web app.

#Sources (not all were used for the final product but some
# earlier sources did help with later parts)

#https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX
#https://www.geeksforgeeks.org/connecting-custom-domain-to-website-hosted-on-firebase/
#https://stackoverflow.com/questions/63434488/how-can-my-cgi-access-firestore-database
#https://www.youtube.com/watch?v=ecT42O6I_WI
#https://flask.palletsprojects.com/en/2.0.x/#user-s-guide
#https://stackoverflow.com/questions/50439426/request-vs-requests-module-in-python
#https://www.youtube.com/watch?v=aj4L7U7alNU
#https://www.weatherbit.io/api/weather-forecast-16-day
#https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing
#https://towardsdatascience.com/how-do-i-extract-nested-data-in-python-4e7bed37566a

from flask import Flask, redirect, url_for, render_template, request
import requests
import json

app = Flask(__name__)

#render the index page. If the form is filled out, then location.html will
#be rendered. location.html is where the user is taken to see teh forcast for
#the city they entered.
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        cty = request.form["city"]
        st = request.form["state"]
        baseURL = "http://api.weatherbit.io/v2.0/forecast/daily"
        api_key = "8072824f3aeb48caa6e51f60fbb5d05b"
        api_result = requests.get(baseURL + "?city=" + cty + "," + st + "&key=" + api_key)
        api_response = api_result.json()
            
        return render_template("location.html", city=cty, state=st, apiResponse=api_response['data'])
    else:
        return render_template("index.html")

#If about is selcted on the nav bar, then about.html is rendered
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)