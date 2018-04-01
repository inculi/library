# ModularFlask

Greetings und willkommen to ModularFlask, a collection of files that aim to help you create a modular Flask application. Usually I don't mind writing boilerplate for Flask projects, however I really like this project structure and wanted to share it. I tried to not make it too bloated, so don't expect your templates to be set up and everything. This is to simply be able to define your routes, logging settings, etc. in different files like a sane person.

# Installation

All the packages required for its use can be found within `requirements.txt`. If the thought of opening this file scares you, you can alternatively do the following:

`pip install flask flask_assets`

As I didn't want to name your project for you, the main folder of code is named `appname`. If you wish to change it (*which... you probably should*) you will need to change the import statements in the following files:

```
run.py
appname/__init__.py
appname/views/__init__.py
appname/views/users.py
```

The last of these is technically just an example file, so really you could just delete it, but you seem like a smart person so I'm sure you'll figure it out.

As for other bits of configuration, the only thing there really is for you to change is the name of the logging file in `config.py`.

# Usage

- Put your classes in `appname/models.py`
- Create your pages in `appname/views/`
- Import your page blueprints in `appname/views/__init__.py` and attach them to the app.
- `$ python run.py`


# Credits

- I originally organized these files for [Sue](https://github.com/inculi/Sue).
- A good deal of inspiration for code structure came from the [Nyaa](https://github.com/nyaadevs/nyaa) project.
- To [Jeff](https://github.com/jeff-hykin) for irritating me with his daily creation of boilerplate projects.


# Todo

- I want to add boilerplate for setting up a database. I think that'd be nice.