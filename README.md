# Reto 6

## Despliegue del cluster 
El cluster se desplego colonando una instancia de los utilizados para el reto 6 para mas detalle acerca de lo que eso implica mirar este video : https://youtu.be/a3F0zb2Dctk .
Aparte de esto se instalaro lo siguiente: Git, mrjob y pip atravez de los siguientes comandos
```bash
sudo yum update
sudo yum install git
sudo yum install pip
sudo pip install mrjob
```
Con esto instalado se realiza el pull de los contenidos del repositorio usando
```bash
git pull https://github.com/Pamilo/reto6.git
```
con esto  se tiene todo
### Despliegue usando AWS CLI
En el orden de ideas de el despliegue del cluster el despliegue de el cluster atravez de AWS CLI tambien se hizo atravez de la opcion de clonar como se puede ver en las siguientes imagenes
![imagen](https://github.com/Pamilo/reto6/assets/81716232/a21e5965-4de8-4768-99b5-b49be933bd65)
![imagen](https://github.com/Pamilo/reto6/assets/81716232/945a8ab5-5213-4377-8831-236c154abe34)

aqui estan los resultados de corre ese comando, esto se hizo en cloudshell de amazon:
![imagen](https://github.com/Pamilo/reto6/assets/81716232/fc21e192-3897-4787-9d63-a145854771b1)
![imagen](https://github.com/Pamilo/reto6/assets/81716232/e3136053-cb64-4654-97bd-a017e990db58)

## Ejecucion de programa WordCount
### En Local
Iniciamos ejecutando "wordcount-local.py" para esto se usa el comando
```bash
python wordcount-local.py ./*.txt > salida-serial.txt
```
lo cual revisa los archivos datos1.txt y datos2.txt que se encuentran en la carpeta worcount, ese resultado se guarda en salida-serial.txt el resultado es el siguiente
![imagen](https://github.com/Pamilo/reto6/assets/81716232/c436321a-03cc-42ff-b7eb-c0fce9942759)

### Con MRjob
Para ejecutar el programa con MRJob se ejecuta  "wordcount-mr.py" con el comando
```bash
python wordcount-mr.py ../../datasets/gutenberg-small/*.txts
```
esto es un extracto del resultado
![imagen](https://github.com/Pamilo/reto6/assets/81716232/3d439aeb-3647-4591-aa92-e1f6e7842215)
