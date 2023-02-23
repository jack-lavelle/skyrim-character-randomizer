from flask import Flask
from flask import render_template_string
import CharacterBuild
import pandas as pd
app = Flask(__name__)

#TODO : design page and send data using jinja ... think of skyrim background with smooth white curved rectangle in front and then cool font, size, color for the text.
@app.route("/")
def home():
	myCharacterDict = CharacterBuild.characterDictGen()
	df = pd.DataFrame(data=myCharacterDict.items())
	
	return render_template_string(df.to_html())

if __name__ == "__main__":
	app.run()