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
python wordcount-mr.py hdfs:///user/hadoop/datasets/gutenberg-small/* -r hadoop --output-dir hdfs:///user/hadoop/output/results.txt -D mapred.reduce.tasks=10
```
lo cual nos da el siguiente resultado
![imagen](https://github.com/Pamilo/reto6/assets/81716232/db85ad6d-033a-4944-890e-21eb17b23e9d)

esto se guardara en la carpeta de hadoop /user/hadoop/output/results.txt si se obtienelos contenidos de esta se puede ver el resultado devidido en partes como se puede observar a continuacion
![imagen](https://github.com/Pamilo/reto6/assets/81716232/bc2d4404-2305-4c25-a37b-cf4369a71cf8)

 aqui hay un ejemplo del contenido de uno de estos archivos
![imagen](https://github.com/Pamilo/reto6/assets/81716232/5c7f3818-97c4-4363-8305-ce8918cf8b34)











 





