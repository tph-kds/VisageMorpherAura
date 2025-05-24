import os
import yaml # Import the YAML library

class ProjectGenerator:
    """
    A class to generate a project folder and file structure based on a dictionary.
    Now with added support for loading structure from YAML files.
    """

    def __init__(self, base_path: str, structure_dict: dict):
        """
        Initializes the ProjectGenerator.

        Args:
            base_path (str): The root directory where the project structure will be created.
                             If it doesn't exist, it will be created.
            structure_dict (dict): A dictionary defining the project structure.
                                   Keys are folder names or file names.
                                   Values can be:
                                   - Another dictionary for nested folders.
                                   - A string for file content.
                                   - None for an empty file.
        """
        self.base_path = os.path.abspath(base_path)
        self.structure_dict = structure_dict

    def _create_item(self, current_path: str, item_name: str, item_content):
        """
        Recursively creates folders and files based on the structure dictionary.

        Args:
            current_path (str): The current path to create items in.
            item_name (str): The name of the current item (folder or file).
            item_content: The content of the item (dict for folder, str/None for file).
        """
        full_path = os.path.join(current_path, item_name)

        if isinstance(item_content, dict):
            # It's a directory
            if not os.path.exists(full_path):
                os.makedirs(full_path)
                print(f"Created directory: {full_path}")
            else:
                print(f"Directory already exists: {full_path}")
            # Recursively create contents of the directory
            for sub_item_name, sub_item_content in item_content.items():
                self._create_item(full_path, sub_item_name, sub_item_content)
        else:
            # It's a file
            try:
                with open(full_path, 'w') as f:
                    if item_content is not None:
                        # Ensure content is written as a string
                        f.write(str(item_content))
                print(f"Created file: {full_path}")
            except IOError as e:
                print(f"Error creating file {full_path}: {e}")

    def generate_structure(self):
        """
        Generates the project structure based on the initialized dictionary.
        """
        print(f"Starting project structure generation at: {self.base_path}")
        if self.base_path != "":
            # Ensure the base path exists
            if not os.path.exists(self.base_path):
                os.makedirs(self.base_path)
                print(f"Created base directory: {self.base_path}")
            else:
                print(f"Base directory already exists: {self.base_path}")

        # Start recursive creation from the base path
        for item_name, item_content in self.structure_dict.items():  # Skip the first item (base path)

            ## don't create the base path again, just create the items inside it
            if self.base_path == "":
                # If base path is empty, create items in the current directory
                self._create_item(os.getcwd(), item_name, item_content)
            else:
                # Create items in the specified base path
                self._create_item(self.base_path, item_name, item_content)

        print("Project structure generation complete.")

    @staticmethod
    def from_yaml(yaml_file_path: str, base_path: str):
        """
        Creates a ProjectGenerator instance by loading the structure from a YAML file.

        Args:
            yaml_file_path (str): The path to the YAML file defining the project structure.
            base_path (str): The root directory where the project structure will be created.

        Returns:
            ProjectGenerator: An instance of ProjectGenerator with the structure loaded.

        Raises:
            FileNotFoundError: If the YAML file does not exist.
            yaml.YAMLError: If there's an error parsing the YAML file.
        """
        if not os.path.exists(yaml_file_path):
            raise FileNotFoundError(f"YAML file not found: {yaml_file_path}")

        try:
            with open(yaml_file_path, 'r') as f:

                structure_dict = yaml.safe_load(f)

            if not isinstance(structure_dict, dict):
                raise ValueError("YAML file must contain a dictionary as its root.")
            return ProjectGenerator(base_path, structure_dict)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file {yaml_file_path}: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while loading YAML: {e}")


# --- Example Usage ---
if __name__ == "__main__":

    yaml_file_path = "project_structure.yaml"  # Path to the YAML file defining the project structure
    print("Welcome to the Project Structure Generator!")
    # read file yaml the project structure in a YAML string
    def read_yaml(file_path):
        with open(file_path, 'r') as f:
            return f.read()
        
    
    # Generate the project structure from yaml file ---
    print("Generating project structure from YAML file...")
    # Create a ProjectGenerator instance from the YAML file
    # Assuming the YAML file is named 'project_structure.yaml' and is in the current directory
    if not os.path.exists(yaml_file_path):
        print(f"YAML file {yaml_file_path}  not found. Please create it with the desired structure.")
        exit(1)
    # Create a ProjectGenerator instance from the YAML file
    print(f"Reading YAML file: {yaml_file_path}")
    yaml_structure_content = read_yaml(file_path = yaml_file_path)

    base_path = ""  # Set the base path where the project structure will be created
    print(f"Base path for project structure: {base_path}")

    project_generator = ProjectGenerator.from_yaml(
        yaml_file_path = yaml_file_path, 
        base_path = base_path
    )
    project_generator.generate_structure()


    print("\n--- Done ---")