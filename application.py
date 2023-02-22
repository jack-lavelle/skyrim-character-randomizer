from flask import Flask
from CharacterBuild import CharacterBuild
app = Flask(__name__)

@app.route("/")
def home():
	myCharacterBuild = CharacterBuild(0)

	return myCharacterBuild.__dict__

if __name__ == "__main__":
	app.run()