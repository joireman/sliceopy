# Slice-o-Python Documentation

## Getting Started

### Setup

You'll first need to create a virtual environment

    $ python -m venv .venv --prompt=my-env
    $ source .venv/bin/activate
    (my-env) $

then install the dependencies

    (my-env) $ python -m pip install -r requirements.txt

### Notebooks

To run a jupyter notebook (or jupyter lab) simply issue the command

    (my-env) $ jupyter lab

this should open in your default browser but it also prints a link which you
can copy and paste into a browser window.  Then open any of the notebooks
in the `notebook` directory.

When you are finished with the environment, you can deactivate it

    (my-env) $ deactivate
    $

or simply close the terminal.   NOTE: It is also possible to edit and run the
notebook in [PyCharm Professional](https://www.jetbrains.com/pycharm/), if you own a license to it.

## Project layout

    README.md     # Main readme
    mkdocs.yml    # Documenation configuration file.
    requirements.txt    #
    data/               # data files associcated with the project
    notebooks
    docs/
        index.md        # The documentation homepage.
        ...             # Other markdown pages, images and other files.

For full documentation visit [mkdocs.org](https://www.mkdocs.org).
