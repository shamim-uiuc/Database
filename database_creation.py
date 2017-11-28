#!/usr/bin/python
import sqlite3

#create the database
conn=sqlite3.connect('rnaseq.db')
#print "Database connection successful"

#create 'gene' table
try:
	conn.execute('''CREATE TABLE gene(
	Gene_id varchar(30) NOT NULL,
	Gene_length NOL NULL,
   	Annotation       varchar(100),
	Pathway varchar(100),
   	PRIMARY KEY(Gene_id)   
	);''')
except:
	print 'Run into error'
	pass


#create table 'metadata'
try:
        conn.execute('''CREATE TABLE metadata(
        Experiment_id   int  NOT NULL,
        Project_name   varchar(100),
        Tissue   varchar(30),
        Sequencing_platform   varchar(30),
        Sequencing_machine   varchar(30),
        Sequencing_mode    varchar(30),
        Sequence_length int,
        PRIMARY KEY(Experiment_id)
        );''')
except:
        print 'Run into error'
        pass

#create table 'expression'
try:
        conn.execute('''CREATE TABLE expression(
        Experiment_id   int  NOT NULL,
        Gene_id varchar(30) NOT NULL,
	Norm_method varchar(50) NOT NULL,
	Expression_level real NOT NULL,
  	FOREIGN KEY(Gene_id) REFERENCES gene(Gene_id),
  	FOREIGN KEY(Experiment_id) REFERENCES metadata(Experiment_id),
        PRIMARY KEY(Gene_id, Experiment_id, Norm_method)
        );''')
except:
        print 'Run into error'
        pass

	

#print "Tables are created successfully"
conn.commit()
conn.close()
