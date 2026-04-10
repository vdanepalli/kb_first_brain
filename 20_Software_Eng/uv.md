# `uv` Package Manager

**Tags:** #uv
**Related:** [[]]

## TL;DR

```bash
brew install uv

uv init # initialize project; creates .git .python-version main.py pyproject.toml README.md; lazy -- doesn't create .venv until needed
uv python pin 3.14 # tell which version to use

uv add pandas requests # installs and updates pyproject.toml accordingly; creates uv.lock; creates .venv
uv remove pandas

uv run file.py

uv lock # automatic
uv sync # pip install -r requirements.txt; creates .venv
uv tree # visualizes the project dependency graph

uv tool install ruff # creates an isolated env for Ruff without conflicting system and exposes ruff command globally. 
uvx pycosway "Hello Captain!" # uvx = uv tool run; run a tool one-off (ephemeral); replaces pipx

uv sync --frozen # fails if uv.lock is out of date preventing accidental upgrades in production
uv export --format requirements-txt > requirements.txt
uv cache clean # nuke the cache if something feels corrupted

uv init --lib fd_utils # create a library project; default is considered as application (when not using --lib); configures pyproject.toml for distributed package; creates src/fd_utils layout

uv add --editable ../fd_utils # when something is modified, the change is reflected immediately without having to reinstall because of --editable
uv add git+https://github.com/username/fd_utils.git
uv add git+ssh://git@github.com/username/fd_utils.git # uv locks it to specific commit hash; future pushes won't break the library later

uv add /Users/user/path/to/fd_utils # Path Dependency (does not lock to a git hash); relies on package version. if code changed but forgot to bump version number, uv might get confused.
uv add "git+file:///Users/VinayD/python_projects/packages/fd_utils" # Git Dependency; uv clones repo at a specific moment. 

uv lock --upgrade-package fd_utils & uv sync # pulls the latest commits if available

uv add "git+file:///...?branch=main"
uv add "git+file:///...?tag=v1.o"
```

## Details

- **Global Cache:** uv downloads packages in a central cache directory; ~/Library/Caches/uv or ~/.cache/uv  
- **Reflinks:** uv uses copy-on-write (reflinks); Only copies metadata (pointers); Only when one of the file changes, you create an actual copy. 
- **Cache Mounting (Docker):** since uv uses global cache, standard Docker builds can't see it unless you mount it. 
- uv looks for packages on the public PyPI registry. 

```py
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas",
#     "snowflake-connector-python",
#     "rich",
# ]
# ///

import pandas as pd
from rich import print

print("[bold green]Starting cleanup...[/bold green]")
# Your ETL logic here
```

- you can embed dependencies inside the script file. uv supports PEP 723, allowing you to declare dependencies in comments. 
- `uv run cleanup.py` reads comments, creates temporary ephemeral (lasting very short) environment, installs packages, runs script, cleans up. 

```ini
[project]
name = "ccfd-monorepo"
version = "0.1.0"
requires-python = ">=3.12"

[tool.uv.workspace] # tell uv where to look for projects
members = [
    "packages/*", 
    "dept/division/station/*", 
    "dept/**" # everything with a pyproject.toml
]

exclude = [
    "dept/div/station/deprecated_proj"
]
```

- Using a workspace means creating one giant virtual env at the root. All projects share a compatible python version. 


<br/><br/>