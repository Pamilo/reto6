# Reto 6

## Despliegue del cluster 
El cluster fue creado atraves de AWS CLI para esto primero (asumiedo que ya se tienen una key pair a utilizar) se crea un bucket en S3 usando el comando
```bash
aws s3api create-bucket --bucket bucket-reto --region us-east-1
```
lo cual no genera el siguiente resultado
![imagen](https://github.com/Pamilo/reto6/assets/81716232/1be5db73-6ac0-46dd-8e32-1d5575540792)
![imagen](https://github.com/Pamilo/reto6/assets/81716232/d2152dda-0636-424b-bb14-c8d15a470f1d)
con esto ya se puede crear el cluster ERM con el siguiente comando
```bash
aws emr create-cluster \
--release-label "emr-7.1.0" \
--name "Reto6" \
--applications Name=Spark Name=Hadoop Name=Pig Name=Hive \
--ec2-attributes KeyName=emr-key.pem \
--instance-type m5.xlarge \
--instance-count 3 \
--use-default-roles \
--no-auto-terminate \
--log-uri "s3://bucket-reto" 
```
Lo cual da el siguiente resultado
![imagen](https://github.com/Pamilo/reto6/assets/81716232/76b57987-447f-421b-903e-9244dbef33cd)
Aparte de esto se instalaro lo siguiente: Git, mrjob y pip atravez de los siguientes comandos
```bash
sudo yum update
sudo yum install git
sudo yum install pip
sudo pip install mrjob
```
![imagen](https://github.com/Pamilo/reto6/assets/81716232/0e3ae12d-d9e0-4a5e-933f-38c9ce83d497)
![imagen](https://github.com/Pamilo/reto6/assets/81716232/3457e12d-57fa-4745-bda2-05d48540d8a3)


Con esto instalado se debe clonar de los contenidos del repositorio usando
```bash
sudo git clone https://github.com/Pamilo/reto6.git
```
![imagen](https://github.com/Pamilo/reto6/assets/81716232/ac53efd0-41c3-4358-bc33-8c241c2f3757)

con esto  se tiene todo

## Ejecucion de programa WordCount
### En Local
Iniciamos ejecutando "wordcount-local.py" para esto se usa el comando
```bash
cd ejercicios/wordcount
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

### En Hadoop
para ejecutar en hadoopprimero conectate a el maestro de el cluster
```bash
cd <Donde tengas tu key>
ssh -i ./emr-key.pem.pem hadoop@ec2-18-215-182-149.compute-1.amazonaws.com
```
con esto hay que crear el dataset en hadoop  con los siguientes comandos
```bash
hdfs dfs -mkdir -p /user/hadoop/datasets/gutenberg-small/
hdfs dfs -copyFromLocal ../../datasets/gutenberg-small/*.txt /user/hadoop/datasets/gutenberg-small/
```
con eso se obtiene este resultado
![imagen](https://github.com/Pamilo/reto6/assets/81716232/c70091a1-f8c4-478d-9c35-59df3c9673a8)

con eso ejecuta el siguiente comando
```bash
python <archivo a ejecutar> hdfs://<direccion del dataset> -r hadoop --output-dir hdfs:/<direccion de archivo resultante> -D mapred.reduce.tasks=10
```
En este caso especifico
```bash
python wordcount-mr.py hdfs:///user/hadoop/datasets/gutenberg-small/* -r hadoop --output-dir hdfs:///user/hadoop/output/results.txt -D mapred.reduce.tasks=10
```
lo cual nos da el siguiente resultado
![imagen](https://github.com/Pamilo/reto6/assets/81716232/db85ad6d-033a-4944-890e-21eb17b23e9d)

esto se guardara en la carpeta de hadoop /user/hadoop/output/results.txt si se obtienelos contenidos de esta se puede ver el resultado devidido en partes como se puede observar a continuacion, esto se puede ver con el comando
```bash
hdfs dfs -ls /user/hadoop/output/results.txt
```
![imagen](https://github.com/Pamilo/reto6/assets/81716232/bc2d4404-2305-4c25-a37b-cf4369a71cf8)

 aqui hay un ejemplo del contenido de uno de estos archivos obtenido atravez de 
```bash
 hdfs dfs -cat /user/hadoop/output/results.txt/part-00000
```
![imagen](https://github.com/Pamilo/reto6/assets/81716232/5c7f3818-97c4-4363-8305-ce8918cf8b34)

## Ejecutar los codigos  de los ejercicios
Antes que nada hay que incluir los datasets en hadoop, en este caso usando el comando 
```bash
hdfs dfs -put -f ../../datasets/otros/ /user/hadoop/datasets/
```
esto hace una copia de la carpeta datasets/otros/ en /user/hadoop/datasets/ ya con esto se puede ejecutar los codigos presentes en este repositorio.
Aqui se va s mostrar el resultado de dicha ejecucion y los resultados (o minimamente la mayoria del mismo) estos se obtiene con los comandos
```bash
hdfs dfs -ls <direccion de archivo resultante>
hdfs dfs -cat <direccion particion del archivo>
```
estos resultados son las respectivas salidas seriales que se pueden ver en las respectivas carpetas
### 1 DIAN
#### A El salario promedio por Sector Económico (SE)
ejecutado con el comando 
```bash
python dianA.py hdfs:///user/hadoop/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/hadoop/output/dianResA.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/800dc6a6-cc98-42ad-b631-c5fd9064406c)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/ce648e86-58ec-4ce7-ac50-e8a961c561ac)
#### B El salario promedio por Empleado
ejecutado con el comando 
```bash
python dianB.py hdfs:///user/hadoop/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/hadoop/output/dianResB.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/8fcad934-a9ed-4626-b45f-7265c0890579)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/e5b63833-300a-4a62-9537-3a5ad1bf977e)

#### C Número de SE por Empleado que ha tenido a lo largo de la estadística
ejecutado con el comando 
```bash
python dianC.py hdfs:///user/hadoop/datasets/otros/dataempleados.txt -r hadoop --output-dir hdfs:///user/hadoop/output/dianResC.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/1f8e253c-73ae-409e-9db8-d82540ff17e7)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/05718fac-7e77-4b22-ad8f-fb6757b99005)

### 2 Bolsa
#### A Por acción, dia-menor-valor, día-mayor-valor
ejecutado con el comando 
```bash
python bolsaA.py hdfs:///user/hadoop/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/stockResA.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/cf7eb020-caca-4fee-8863-f9c485e42875)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/756dfc02-f2b2-4234-8ab6-b060c3f82c57)
#### B Listado de acciones que siempre han subido o se mantienen estables.
ejecutado con el comando 
```bash
python bolsaB.py hdfs:///user/hadoop/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/stockResB.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/5113a016-db73-4d50-9dc5-3d39f308a429)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/adada236-74b6-4525-84c6-2c0188c4dd66)


#### C DIA NEGRO
ejecutado con el comando 
```bash
python bolsaC.py hdfs:///user/hadoop/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/stockResC.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/9fc98c88-90a9-4975-9200-4827773b81c4)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/5ee30e33-9319-4b9c-849f-e09e28b232ef)

### 3 Peliculas
#### A Número de películas vista por un usuario, valor promedio de calificación
ejecutado con el comando 
```bash
python peliculasA.py hdfs:///user/hadoop/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/moviekResA.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/fff17587-c8f3-48c9-a143-f9b803ba51a2)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/5b6744ff-23ee-47ce-b110-1e2fddc488f4)
![imagen](https://github.com/Pamilo/reto6/assets/81716232/1b263c7e-109e-4fdd-b02e-c10249af54e4)


#### B-C Día en que más  y menos películas se han visto
ejecutado con el comando 
```bash
python peliculasB-C.py hdfs:///user/hadoop/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/moviekResB-C.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/23a6023d-910a-4e43-99e9-ccae169f25c8)

y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/a01cbe0c-0d99-4ce9-9e4a-2073e8bd782c)

#### D Número de usuarios que ven una misma película y el rating promedio
ejecutado con el comando 
```bash
python peliculasD.py hdfs:///user/hadoop/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/moviekResD.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/9fc98c88-90a9-4975-9200-4827773b81c4)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/5ee30e33-9319-4b9c-849f-e09e28b232ef)

#### E-F Día en que peor evaluación en promedio han dado los usuarios
ejecutado con el comando 
```bash
python bolsaB.py hdfs:///user/hadoop/datasets/otros/dataempresas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/stockResB.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/3dfd15d1-751e-4111-8bdb-909f23e99328)

y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/169d1712-1293-4311-9c80-91b468b4832a)


#### G La mejor y peor película evaluada por genero
ejecutado con el comando 
```bash
python peliculasG.py hdfs:///user/hadoop/datasets/otros/datapeliculas.txt -r hadoop --output-dir hdfs:///user/hadoop/output/moviekResG.txt -D mapred.reduce.tasks=10
```
esto genera 
![imagen](https://github.com/Pamilo/reto6/assets/81716232/618d24e0-57fc-4939-a3c0-7963281388d4)
y el resultado es
![imagen](https://github.com/Pamilo/reto6/assets/81716232/3abdf694-e37b-4652-a14c-c210a5b01699)

## Video 
https://youtu.be/lCUeSTeSmDs











 





