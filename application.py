from flask import Flask
from flask import render_template
import CharacterBuild
app = Flask(__name__)

# TODO : design page and send data using jinja ... think of skyrim background with smooth white curved rectangle in front and then cool font, size, color for the text.


@app.route("/")
def main():
    character = CharacterBuild.Character("random", None)

    return render_template("test.html", data=character.get_character_string_list())

# This must be commented out for pythonanywhere
# if __name__ == "__main__":
# app.run()
