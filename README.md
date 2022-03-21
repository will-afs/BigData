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

Connect to the edge HDFS of Adaltas Cloud by SSH
================================================
- Activate the VPN
- Connect by SSH, with password 'AdaltasWill2000':

    ssh w.afonso-cs@edge-1.au.adaltas.cloud

Export scientific articles metadata to HDFS
===========================================

Prepare the environment to connect to the applications that will follow
-----------------------------------------------------------------------

Install hdds python requirements:

    pip install --upgrade pip
    pip install requests_kerberos kerberos hdfs avro pandas
    
Get a Kerberos ticket to connect to the applications that will follow (password : AdaltasWill2000):

    kinit w.afonso-cs
   
The ticket can be checked with the following command:
   
    klist
    
Generate a CSV as an aggregation of articles metadata
-----------------------------------------------------
Clone the current project onto the machine:

    git clone https://github.com/will-afs/BigData.git
    
Go into the BigData folder:

    cd BigData
    
Generate the .csv database of PDF metadata :

    python3 generate_csv.py

    
