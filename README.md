# Python-JSON-Settings
 Python script that reads and writes settings from a JSON file source.
 
Attributes
----------
`file_path : str`  The file path for the JSON settings file.

Methods
-------
`value_for_key(key)`
    Retrieves the value associated with the given key from the JSON settings file.

`set_value_for_key(key, value)`
    Sets the value for the specified key in the settings and writes the updated settings to the JSON file.

`read_json()`
    Reads the JSON settings file and returns its contents as a dictionary.

`write_json()`
    Writes the current settings (stored in self.data) to the JSON settings file, ensuring data persistence.

