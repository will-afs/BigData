# 🌐 BigData
Repository for source code of "Big Data (Hadoop, Map reduce, Hive)" lecture at MS SIO, CentraleSupélec

Setup the VPN to connect to Adaltas infrastructure
==================================================
    
    sudo apt-get install network-manager-openvpn network-manager-openvpn-gnome ubuntu-desktop
    
- Download the .ovpn file from the mail received from Adaltas (check william.afonso@student-cs.fr mailbox)
- Open network settings
- On VPN, click on "+"
- Import from file
- Select the .ovpn file previously downloaded
- check the connexion to Adaltas infrastructure : ping edge-1.au.adaltas.cloud

Export scientific articles metadata to HDFS
===========================================

Prepare the environment to use the applications that will follow
----------------------------------------------------------------
(On Ubuntu) Install the required libraries:

    sudo apt-get install gcc python-dev libkrb5-dev

Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install python requirements:

    pip install --upgrade pip
    pip install -r requirements.txt
    
Generate a CSV as an aggregation of articles metadata
-----------------------------------------------------
Clone the current project onto your machine:

    git clone https://github.com/will-afs/BigData.git
    
Go into the BigData folder:

    cd BigData
    
Generate the .csv database of PDF metadata :

    python3 generate_csv.py
    
Push the CSV to HDFS
--------------------
Activate the VPN

Get a Kerberos ticket to connect to the applications that will follow (password : AdaltasWill2000):

    kinit w.afonso-cs
   
The ticket can be checked with the following command:
   
    klist

Push the CSV to HDFS

    python3 push_csv_to_hdfs.py

Connect to the edge HDFS of Adaltas Cloud by SSH and check the .CSV has been stored into the HDFS
-------------------------------------------------------------------------------------------------
Connect to Adaltas server with password 'AdaltasWill2000':

    ssh w.afonso-cs@edge-1.au.adaltas.cloud

Check HDFS content:

    hdfs dfs -ls /education/cs_2022_spring_1/w.afonso-cs/fil-rouge/
    
The result should be as follows:

<img src="https://github.com/will-afs/BigData/blob/main/img/HDFS%20content.JPG">

Process data with HQL
=====================
Connect to Zeppelin through a web browser (login: w.afonso-cs, password: AdaltasWill2000):

    http://zep-1.au.adaltas.cloud:9995/#/
    
Run the following Zeppelin Notebook:

<img src="https://github.com/will-afs/BigData/blob/main/img/Zeppelin%20HQL%20script%20location.JPG">

Creation of a Hive table from the CSV file previously stored in HDFS:

<img src="https://github.com/will-afs/BigData/blob/main/img/Create%20table.JPG">

Check the table is duely created:

<img src="https://github.com/will-afs/BigData/blob/main/img/Check%20table%20is%20created.JPG">

Plot extracted PDfs in function of time:
