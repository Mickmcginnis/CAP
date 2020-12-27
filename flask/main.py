from flask import Flask, render_template
import page_generator 

# ProPublica API key
# XirFDDm7LM9fETZWMhDCVhgOdWoVT881LVI3szQg 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/house")
def house():
    return page_generator.gen_pages(rep=None)
    
@app.route("/house/<rep>")
def rep_page(rep):
    return page_generator.gen_page(rep=rep)


if __name__ == "__main__":
    app.run(debug=True)