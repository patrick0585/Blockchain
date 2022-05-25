# Blockchain
Simple Blockchain in Python

## Usage

### 1.) Crate Blockchain
```chain = Blockchain()```

### 4.) Add new Block to Blockchain
```chain.build_block("Block - Test")```


## Flask

First, make sure virtualenv is installed
----------------------------------------
```pip3 install virtualenv```

Create your virtual environment
--------------------------------------
```virtualenv venv --system-site-packages```

Activate the virtual environment
---------------------------------
```source venv/bin/activate```

Make sure Flask is installed
----------------------------
```pip3 install Flask```


Set the FLASK_APP system variable
---------------------------------
```(venv) $ export FLASK_APP=my_new_flask_app.py```


## Todos
- ```__init__`` Funktion bei der Blockchain erstellen [erledigt 24.05.2022]
- in der ``__init__```Funktion der Blockchain den Genesis-Block erstellen und hinzufügen [erledigt 24.05.2022]
- Beim Block einen ```timestamp``` wie auch ```transactions``` hinzufügen 
- ```Flask```hinzufügen, damit das Projekt mit einer API und GUI gestartet werden kann