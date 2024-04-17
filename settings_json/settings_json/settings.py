import json
import os


class Settings:
    """
    A class used to manage settings by reading from and writing to a JSON settings file.

    Attributes
    ----------
    file_path : str
        The file path for the JSON settings file.

    Methods
    -------
    value_for_key(key)
        Retrieves the value associated with the given key from the JSON settings file.

    set_value_for_key(key, value)
        Sets the value for the specified key in the settings and writes the updated settings to the JSON file.

    read_json()
        Reads the JSON settings file and returns its contents as a dictionary.

    write_json()
        Writes the current settings (stored in self.data) to the JSON settings file, ensuring data persistence.
    """
    file_path = "data/settings.json"

    def value_for_key(self, key):
        """
        Retrieves the value associated with the given key from the JSON settings file.

        Parameters
        ----------
        key : str
            The key whose value is to be retrieved.

        Returns
        -------
        any
            The value associated with the key in the settings JSON file.
        """
        data = self.read_json()
        value = data[key]
        return value

    def set_value_for_key(self, key, value):
        """
        Sets the value for the specified key in the settings and writes the updated settings to the JSON file.

        Parameters
        ----------
        key : str
            The key for which the value is to be set.
        value : any
            The new value to set for the specified key.

        Raises
        ------
        KeyError
            If the key is not found in the data dictionary.
        """
        self.data[key] = value
        self.write_json()

    def read_json(self):
        """
        Reads the JSON settings file and returns its contents as a dictionary.
        If the file does not exist or has invalid content, appropriate error messages are printed.

        Returns
        -------
        dict
            A dictionary representing the JSON data in the settings file.
        """
        if not os.path.exists(self.file_path):
            print(f"File not found at {self.file_path}")
        else:
            try:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    return data
            except FileNotFoundError:
                print("No util.json file found: " + self.file_path)
            except json.decoder.JSONDecodeError:
                print("Invalid util.json file")

    def write_json(self):
        """
        Writes the current settings (stored in self.data) to the JSON settings file, ensuring data
        persistence.
        If the file does not exist or an error occurs during writing, appropriate error messages
        are printed.
        """
        if not os.path.exists(self.file_path):
            print(f"File not found at {self.file_path}")
        else:
            try:
                with open(self.file_path, "w") as file:
                    json.dump(self.data, file, indent=4)
                print("Settings saved to {}".format(self.file_path))
            except FileNotFoundError:
                print("No util.json file found")
            except json.decoder.JSONDecodeError:
                print("Invalid util.json file")
