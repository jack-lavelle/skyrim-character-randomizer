from flask import Flask
from prototype import CharacterBuild
app = Flask(__name__)

@app.route("/")
def home():
	myCharacterBuild = CharacterBuild(0)

	printString = ""

	for x in myCharacterBuild.__dict__:
		printString += str(x) + ": " + str(myCharacterBuild.__dict__[x]) + "\n"


	return printString

if __name__ == "__main__":
	app.run()