import attributes
from property_generator import generate_property


class Character:
    def __init__(self, properties: dict = None):
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
            if prop_val == None and prop in attributes.property_dependency_map:
                required_prop = attributes.property_dependency_map[prop]
                if self.properties[required_prop] == None:
                    self.properties[required_prop] = generate_property(
                        required_prop, self.properties
                    )

            self.properties[prop] = generate_property(prop, self.properties)
