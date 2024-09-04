# Steps

# Pasos para que inicialicen este proyecto

to create .gitignore file:
https://www.toptal.com/developers/gitignore/api/windows,linux,macos,python

# Game Project

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game
python3 game/main.py
```

# App Project

Para correr la app, necesitas:

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# Notas sobre el ambiente virtual

Si estas en linus o wsl debes instalar

```sh
    sudo apt install -y python3-venv
```

Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

```sh
    python3 -m venv env
```

Activar el ambiente

```sh
    source env/bin/activate
```

Salir del ambiente virtual

```sh
    deactivate
```

Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo

```sh
    pip3 install matplotlib==3.5.0
```

Verificar las instalaciones

```sh
    pip3 freeze
```

# Automatización de dependencias

```
    requirements.txt
```
