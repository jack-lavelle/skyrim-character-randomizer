# Run from command-line with: "python -c 'import prototype as p; p.main()'"
# TODO: weapons specialization?
# TODO: religion and alignment
# TODO: DiD-ify skills (meaning make them viable for each run)
# TODO: look over Reddit post for ideas / refinements
# TODO: reference openAI chat for good backstory ... include query.
# TODO: revamp character generation when manually selecting skills
# TODO: mid-game character changes
# TODO: non-random builds

import attributes
from property_generator import generate_property


class Character:
    previously_checked_properties = []

    def __init__(self, properties: dict):
        # Initialize all values to `None`.
        self.properties = dict(
            (property_key, None) for property_key in attributes.property_keys
        )

        # If some properties were passed, fill them in.
        if properties:
            for prop, prop_val in properties.items():
                self.properties[prop] = prop_val

        # Fill the remainder.
        for prop, prop_val in self.properties.items():
            if prop_val == None:
                if prop in attributes.property_dependency_map:
                    required_prop = attributes.property_dependency_map[prop]
                    if self.properties[required_prop] == None:
                        self.properties[required_prop] = generate_property(
                            required_prop, self.properties
                        )

                self.properties[prop] = generate_property(prop, self.properties)

        # TODO: I don't like how I am using side-effects like this ... it can be hard to track down
        # where self.previously_checked_properties changes ... this should be overhauled to be more
        # clear and concise, function oriented.

    def get_character_string_dictionary_list(self):
        strings_keyvalues = []
        for x, y in self.properties.items():
            checked_bool = False
            if x in self.previously_checked_properties:
                checked_bool = True
            strings_keyvalues.append((x.capitalize() + " : " + y, {x: y}, checked_bool))

        return strings_keyvalues
