#!/usr/bin/python

import sqlite3
conn=sqlite3.connect('rnaseq.db')
print 'connected to database'

################################################################ Metadata Table ###############################################			
## table metadata schema:
#CREATE TABLE metadata(
#   experiment_id   int  NOT NULL,
#   library        varchar(15)     NOT NULL,
#   experiment_name   varchar(100),
#   tissue_used   varchar(30),
#   sequence_platform   varchar(30),
#   sequencing_machine   varchar(30),
#   sequencing_mode    varchar(30),
#   sequence_length int,
#   PRIMARY KEY(experiment_id)
#);

#prepare query for inserting into database
query = """INSERT INTO metadata VALUES (?,?,?,?,?,?,?,?)"""

#read the file
with open("metadata_with_header.csv", "r") as file:
    file.readline()
    for line in file:
	#read a line from cvs files
	words=line.split(',')

	#read the cells into variables
	library=words[0]
	experiment_id=int(words[1])
	experiment_name=words[2]
   	tissue_used=words[3]
   	sequence_platform=words[4]
 	sequencing_machine=words[5]
	sequencing_mode=words[6]
	sequence_length=int(words[7])

	#ararnge the values to insert
	vals=(experiment_id, library, experiment_name, tissue_used, sequence_platform, sequencing_machine, sequencing_mode, sequence_length)
	
        #there might be error while inserting, so it should be within 'try-catch-except'
	try:
		cursor=conn.execute(query, vals);
	except:
		print 'run into error'
        	pass


################################################################ Gene Table ###############################################			
#CREATE TABLE gene(
#   gene_model varchar(30) NOT NULL,
#   experiment_id    int   NOT NULL,
#   rpkm        real     NOT NULL,
#   annotation       varchar(100),
#   FOREIGN KEY(experiment_id) REFERENCES metadata(experiment_id),
#   PRIMARY KEY(gene_model, experiment_id)
#);

#prepare query for inserting into database
query = """INSERT INTO gene VALUES (?,?,?,?)"""

with open("gene_model_with_header.csv", "r") as file:
    file.readline();	
    for line in file:
	#read a line from cvs files
	words=line.split(',')

	#read the cells into variables
	gene_model=words[0]
	experiment_id=int(words[1])
	rpkm=words[2]
   	annotation=words[3]

	#ararnge the values to insert
	vals=(gene_model,experiment_id,rpkm,annotation)
	
        #there might be error while inserting, so it should be within 'try-catch-except'
	try:
		cursor=conn.execute(query, vals);
	except:
		print 'run into error'
        	pass
			
			
			

#commit and close the database connection
conn.commit()
print "Operation done successfully";
conn.close()
