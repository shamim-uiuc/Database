#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('rnaseq.db')
print "Opened database successfully";

################################################################ Gene Table ###############################################			
#CREATE TABLE gene(
#   gene_model varchar(30) NOT NULL,
#   experiment_id    int   NOT NULL,
#   rpkm        real     NOT NULL,
#   annotation       varchar(100),
#   FOREIGN KEY(experiment_id) REFERENCES metadata(experiment_id),
#   PRIMARY KEY(gene_model, experiment_id)
#);

output_file=open("gene_anno_expression.txt", "wb");
output_file.write("Gene_id, Annotation, Expression1, Expression2, Expression3\n");

############################################################################# simple query reading from a single table
print 'Reading data from metadata table\n'
cursor = conn.execute("SELECT gene_model,annotation,rpkm from  gene")
rows=cursor.fetchall() 

i=0;
while (i<len(rows)):
	#read next 3 rows: i, i+1, i+2 for 3 expression data
	print >> output_file, rows[i][0], ",", rows[i][1].strip(), ",", rows[i][2], ",", rows[i+1][2], ",", rows[i+2][2], "\n" 
	i=i+3

print "Operation done successfully";
conn.close()
output_file.close();
