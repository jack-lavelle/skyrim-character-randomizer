from flask import Flask
from flask import render_template, request
from ast import literal_eval
from character import Character
import attributes
import database

app = Flask(__name__)
# TODO : button for completely new character
# TODO : do I really need another page for handle_data ... condense it into one page.


@app.route("/")
def main():
    character = Character({})

    return render_template(
        "front-page.html", data=character.get_character_string_dictionary_list()
    )


@app.route("/handle_data", methods=["POST"])
def handle_data():
    checked_properties = request.form.getlist("checked_property")
    d = {}
    for dict_string in checked_properties:
        d.update(literal_eval(dict_string))

    # If `skills` is selected, then so too should `background` be.
    if "skills" in d:
        background_val = list(attributes.backgrounds.keys())[
            list(attributes.backgrounds.values()).index(d["skills"])
        ]
        d["background"] = background_val
    elif "background" in d:
        skills_val = list(attributes.backgrounds.values())[
            list(attributes.backgrounds.keys()).index(d["background"])
        ]
        d["skills"] = skills_val

    new_character = Character(d)
    new_character.previously_checked_properties = list(d.keys())

    return render_template(
        "front-page.html", data=new_character.get_character_string_dictionary_list()
    )


@app.route("/suggestion")
def show_suggestion_page():
    return render_template("suggestion.html")


@app.route("/submit_suggestion", methods=["POST"])
def submit_suggestion():
    suggestion = request.form["suggestion"]
    database.write_suggestion(suggestion)
    character = Character({})

    return render_template(
        "front-page.html", data=character.get_character_string_dictionary_list()
    )


# This must be commented out for pythonanywhere
if __name__ == "__main__":
    app.run()
