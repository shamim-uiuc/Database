#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('rnaseq.db')
#print "Opened database successfully";

output_file=open("Output_gene_expression.csv", "wb")

#read the Tissue name for experiment_id = 1
cursor=conn.execute("select tissue from metadata where experiment_id=1")
tissue1 = cursor.fetchone()[0] #retrieve the first column of the row

#read the Tissue name for experiment_id = 2
cursor=conn.execute("select tissue from metadata where experiment_id=2")
tissue2 = cursor.fetchone()[0] #retrieve the first column of the row

#read the Tissue name for experiment_id = 3
cursor=conn.execute("select tissue from metadata where experiment_id=3")
tissue3 = cursor.fetchone()[0] #retrieve the first column of the row

#create the header with the Tissue name        
line='Gene_id, Annotation, %s, %s, %s, Pathways' %(tissue1, tissue2, tissue3)
print line
print >> output_file, line


############################################################################# query
cursor = conn.execute("select gene.Gene_id, Annotation, Expression_level, Pathway from gene, metadata, expression where gene.Gene_id=expression.Gene_id and metadata.Experiment_id=expression.experiment_id and Norm_method='RPKM'")
rows=cursor.fetchall() 

i=0;
while (i<len(rows)):
    if rows[i][2] > 50:
	    #Here expression cut off is 50 RPKM and it can be changed.
    	    #read next 3 rows i, i+1, i+2
    	    #rows[i][2] is the expression of 'leaf' 
    	    #rows[i+1][2] is the expression of 'Seeds' 
    	    #rows[i+1][2] is the expression of 'Root'
    	    line='%s, %s, %s, %s, %s, %s' %(rows[i][0], rows[i][1].strip(), rows[i][2], rows[i+1][2], rows[i+2][2], rows[i][3])
    	    print line
    	    print >> output_file, line
    i=i+3

#print "Operation done successfully";
conn.close()
output_file.close();
