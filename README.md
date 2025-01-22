## Welcome!

### Pre-requisites 

- Ensure you have python version 3.9 or higher installed.
- Ensure you have node version 18.18 or later.

### Installation

1. Install django dependencies

- install poetry with `curl -sSL https://install.python-poetry.org | python3 -` 
- install dependencies with `cd api && poetry install`

2. Install nextjs dependencies

- install dependencies with `cd nextjs && npm install` 

### Start servers:

It is recommended that you use a terminal with multiple panes so that you can see the terminals running side by side. Start each
of the below commands in their own pane.

- django: `cd api && poetry run python manage.py runserver`
- next: `cd nextjs && npm run dev`

Note: if you do not have something that automatically activates the poetry environment installed on your system, to run commands from
inside the virtual environment create you have to prefix with `poetry run`. You can also manually activate the environment by running
`eval $(poetry env activate)`.

