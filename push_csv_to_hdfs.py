from hdfs.ext.kerberos import KerberosClient
from  hdfs.ext.dataframe import write_dataframe
import pandas as pd

#csv_filename = 'DataBase.csv'
#df = pd.read_csv (csv_filename)
#print('Loaded dataframe from CSV \"{}\":\n\n{}'.format(csv_filename, df))

client = KerberosClient('http://hdfs-nn-1.au.adaltas.cloud:50070')

print('Connected to client {}'.format(client))

# export DataBase.csv to /education/cs_2022_spring_1/$USER/fil-rouge/
hdfs_path = '/education/cs_2022_spring_1/w.afonso-cs/fil-rouge/'


client.upload(hdfs_path, 
            '/home/william/Programming/BigData/DataBase.csv', 
            n_threads=1, 
            temp_dir=None, 
            overwrite = True,
            chunk_size=65536, 
            progress=None, 
            cleanup=True)
