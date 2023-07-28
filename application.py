from flask import Flask
from flask import render_template, request
from ast import literal_eval
import CharacterBuild

app = Flask(__name__)

# TODO : design page and send data using jinja ... think of skyrim background with smooth white curved rectangle in front and then cool font, size, color for the text.
# TODO : button for completely new character
# TODO : background changes even if skills are held constant


@app.route("/")
def main():
    character = CharacterBuild.Character("random", None)
    print(character.get_character_string_dictionary_list())

    return render_template(
        "test.html", data=character.get_character_string_dictionary_list()
    )


@app.route("/handle_data", methods=["POST"])
def handle_data():
    dict_string_list = request.form.getlist("saved_property")
    d = {}
    for dict_string in dict_string_list:
        d.update(literal_eval(dict_string))

    new_character = CharacterBuild.Character("semi-random", d)

    return render_template(
        "test.html", data=new_character.get_character_string_dictionary_list()
    )


# This must be commented out for pythonanywhere
if __name__ == "__main__":
    app.run()
