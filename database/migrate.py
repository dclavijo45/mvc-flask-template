import os

def define_models():
    """
    Dynamically imports all model modules from the 'database/models' directory whose filenames contain '_model.py'.

    This function scans the 'database/models' folder for Python files with names containing '_model.py',
    then imports each as a module under the 'database.models' package. This is typically used to ensure
    that all model definitions are loaded and registered (e.g., with an ORM) before performing database migrations.

    Raises:
        FileNotFoundError: If the 'database/models' directory does not exist.
        ImportError: If a module cannot be imported.
    """
    folder = os.path.abspath('database/models')
    for filename in os.listdir(folder):
        if filename.__contains__('_model.py'):
            name = filename[:-3].lower()
            __import__(f'database.models.{name}', fromlist=[name])