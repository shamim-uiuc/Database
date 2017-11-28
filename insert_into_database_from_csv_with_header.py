#!/usr/bin/python

import sqlite3
conn=sqlite3.connect('rnaseq.db')
#print 'connected to database'

################################################################ Metadata Table ###############################################			
## table metadata schema:
#CREATE TABLE metadata(
#        Experiment_id   int  NOT NULL,
#        Project_name   varchar(100),
#        Tissue   varchar(30),
#        Sequencing_platform   varchar(30),
#        Sequencing_machine   varchar(30),
#        Sequencing_mode    varchar(30),
#        Sequence_length int,
#        PRIMARY KEY(Experiment_id)
#        );


#prepare query for inserting into database
query = """INSERT INTO metadata VALUES (?,?,?,?,?,?,?)"""

#read the file
with open("Metadata.csv", "r") as file:
    file.readline()
    for line in file:
	#read a line from cvs files
	words=line.split(',')
	
	#read the cells into variables
	Experiment_id=words[0]
	Project_name=words[1]
   	Tissue=words[2]
   	Sequencing_platform=words[3]
 	Sequencing_machine=words[4]
	Sequencing_mode=words[5]
	Sequence_length=int(words[6].strip())

	#ararnge the values to insert
	vals=(Experiment_id, Project_name, Tissue, Sequencing_platform, Sequencing_machine, Sequencing_mode, Sequence_length)
	
        #there might be error while inserting, so it should be within 'try-catch-except'
	try:
		cursor=conn.execute(query, vals);
	except:
		print 'run into error'
        	pass

#print "Insert into metadata successful"
################################################################ Gene Table ###############################################			
#CREATE TABLE gene(
#        Gene_id varchar(30) NOT NULL,
#        Gene_length NOL NULL,
#        Annotation       varchar(100),
#        Pathway varchar(100),
#        PRIMARY KEY(Gene_id)
#        );


#prepare query for inserting into database
query = """INSERT INTO gene VALUES (?,?,?,?)"""

with open("Gene.csv", "r") as file:
    file.readline();	
    for line in file:
	#read a line from cvs files
	words=line.split(',')

	#read the cells into variables
	Gene_id=words[0]
	Gene_length=words[1]
	Annotation=words[2]
   	Pathway=words[3].strip()

	#ararnge the values to insert
	vals=(Gene_id,Gene_length,Annotation, Pathway)
	
        #there might be error while inserting, so it should be within 'try-catch-except'
	try:
		cursor=conn.execute(query, vals);
	except:
		print 'run into error'
        	pass
		
#print "insert into gene successfull"	
#####################################################################################################################################################################
#CREATE TABLE expression(
#        Experiment_id   int  NOT NULL,
#        Gene_id varchar(30) NOT NULL,
#        Norm_method varchar(50) NOT NULL,
#        Expression_level real NOT NULL,
#        FOREIGN KEY(Gene_id) REFERENCES gene(Gene_id),
#        FOREIGN KEY(Experiment_id) REFERENCES metadata(Experiment_id),
#        PRIMARY KEY(Gene_id, Experiment_id, Norm_method)
#        );			
#
#prepare query for inserting into 'expression; table
#prepare query for inserting into database
query = """INSERT INTO expression VALUES (?,?,?,?)"""

with open("Expression.csv", "r") as file:
    file.readline();
    for line in file:
        #read a line from cvs files
        words=line.split(',')

        #read the cells into variables
        Experiment_id=Experiment_id=words[0]
        Gene_id=words[1]
        Norm_method=words[2]
        Expression_level=words[3].strip()

        #ararnge the values to insert
        vals=(Experiment_id,Gene_id,Norm_method,Expression_level)

        #there might be error while inserting, so it should be within 'try-catch-except'
        try:
                cursor=conn.execute(query, vals);
        except:
                print 'run into error'
                pass







			



#commit and close the database connection
conn.commit()
#print "Operation done successfully";
conn.close()
