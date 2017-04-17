from flask import Flask, render_template, request, session, redirect, url_for, Response
import json, urllib2, urllib

app = Flask(__name__)
app.secret_key = 'the_crew'


################################################################################
################################################################################
################################################################################


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/whyPhoneGap')
def why():
    return render_template("why.html")

@app.route('/howItWorks')
def how():
    return render_template("how.html")

@app.route('/compatibility')
def comp():
    return render_template("comp.html")

@app.route('/downsides')
def down():
    return render_template("down.html")

@app.route('/walkthrough')
def walk():
    return render_template("walk.html")






if __name__ == '__main__':
    app.debug=True
app.run(threaded=True)
