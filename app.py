from flask import Flask, render_template, request, session, redirect, url_for, Response
from utils import billionaires, global_development, state_fragility
import json, urllib2, urllib
import dbUtils

app = Flask(__name__)
app.secret_key = 'the_crew'



#
#
#DO NOT LOOK AT THIS
#


# =============================
# MAIN
# =============================


@app.route('/', methods = ['GET', 'POST'])
def root():
    if "country" in request.form:
        line_graph_country = request.form["country"]
    else:
        line_graph_country = "default"

    return render_template("dots.html", gd_list=dev, sf_list=frag, b_list=bill, countries=countries_list, line_graph_country = line_graph_country)

# =============================
# LINE GRAPH ROUTES
# =============================

# line graph can only read data from this route if it includes a
# .json extension at the end of the country name
@app.route('/line/development/<country>.json/')
def development(country):
    data = []
    llist = global_development.get_reports()
    for value in llist:
        if country == value['Country']:
            telephone_lines = round(value['Data']['Infrastructure']['Telephone Lines per 100 People'], 3)
            cell_subscriptions = round(value['Data']['Infrastructure']['Mobile Cellular Subscriptions per 100 People'], 3)
            life_expectancy = round(value['Data']['Health']['Life Expectancy at Birth, Total'], 3)

            measure_growth = round((cell_subscriptions + telephone_lines) * life_expectancy)
            year = value['Year']
            data.append({'index': measure_growth , 'date': year})

    return Response(response = json.dumps(data), status = 200, mimetype='application/json')

@app.route('/line/fragility/<country>.json/')
def fragility(country):
    data = []
    llist = state_fragility.get_scores()
    for value in llist:
        if country == value['Country']:
            sf_index = value['Metrics']['State Fragility Index']
            year = value['Year']
            data.append({'index': sf_index, 'date': year})

    return Response(response = json.dumps(data), status = 200, mimetype='application/json')



if __name__ == '__main__':
    app.debug=True
app.run(threaded=True)
