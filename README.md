# Steps
# Curso Phyton PIP PLATZI

# Game 
Para ejecutar el juego: 
```
cd game
python3 main.py
```
# Graficos
Para instalar

Instrucciones
```sh
git clone https://github.com/jonasalvarado/curso-python-pip.git
cd app
python3 -m venv virtual-env
source virtual-env/bin/activate
pip3 -r requirements.txt
python3 main.py
(desactivar entorno virtual)
deactivate
``` 
Para crear un contenedor en docker
```sh
docker-compose build # Para crear el docker
docker-compose up -d # Para lanzarlo
docker-compose ps # Para ver el estado del contenedor
docker-compose exec app-csv bash # Para ingresar al docker y desarrollar ahi
exit # salir del contenedor
```