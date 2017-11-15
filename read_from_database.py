#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('rnaseq.db')
print "Opened database successfully";

############################################################################# simple query reading from a single table
print 'Reading data from metadata table\n'
cursor = conn.execute("SELECT *from  metadata")
for row in cursor:
   print "Experiment_id = ", row[0]," Libaray = ", row[1]," Experiment_nameS = ", row[2]," Tissue_used = ", row[3], "\n"

############################################################################# complicated query after joining two tables
print '\nReading data from both table\n'
cursor = conn.execute("SELECT gene_model, rpkm, experiment_name, tissue_used, sequence_platform  from  metadata, gene where metadata.experiment_id=gene.experiment_id and rpkm>50")
for row in cursor:
   print "gene_model =", row[0],", rpkm =", row[1], ", experiment_name =", row[2], ", tissue_used =", row[3], ", sequence_platform=", row[4], "\n"

print "Operation done successfully";
conn.close()
