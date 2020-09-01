from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/academy')
def academy():
    return render_template('academy.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/google-ranking')
def googleRanking():
    return render_template('google-ranking.html')

@app.route('/local-seo')
def localSeo():
    return render_template('local-seo.html')

@app.route('/pay-per-click')
def payPerClick():
    return render_template('pay-per-click.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/seo')
def seo():
    return render_template('seo.html')

@app.route('/website-audit')
def websiteAudit():
    return render_template('website-audit.html')

if __name__ == "__main__":
    app.run(debug=True)
