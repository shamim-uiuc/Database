#!/usr/bin/python
import sqlite3

#create the database
conn=sqlite3.connect('rnaseq.db')
#print "Database connection successful"

#create 'metadata' table
try:
	conn.execute('''CREATE TABLE metadata(
   	experiment_id   int  NOT NULL,
   	library        varchar(15)     NOT NULL,
   	experiment_name   varchar(100),
   	tissue_used   varchar(30),
   	sequence_platform   varchar(30),
   	sequencing_machine   varchar(30),
   	sequencing_mode    varchar(30),
   	sequence_length int,
   	PRIMARY KEY(experiment_id)
	);''')
except:
	print 'Run into error'
	pass

#create 'gene' table
try:
	conn.execute('''CREATE TABLE gene(
   	gene_model varchar(30) NOT NULL,
   	experiment_id    int   NOT NULL,
   	rpkm        real     NOT NULL,
   	annotation       varchar(100),
  	FOREIGN KEY(experiment_id) REFERENCES metadata(experiment_id),
   	PRIMARY KEY(gene_model, experiment_id)   
	);''')
except:
	print 'Run into error'
	pass

#print "Tables are created successfully"
conn.commit()
conn.close()
