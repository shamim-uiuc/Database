#Command to run:
chmod +x Main.py
python -B Main.py

The program will run even without -B. Actually -B is used here to avoid creation of additional .pyc files as individual scripts were imported into the Main.py script. If you do not use -B, three additional .pyc files will be generated for three scripts.

#Input Files:
Metadata.csv     = Simple metadata file about experiment, Tissue used and NGS library
Gene.csv         = Gene model and their Annotation
Expression.csv   = Gene model and their expression level in different experiments


#python Scripts:
Main.py   = This simple script calls below three scripts to create, insert and retrieve data from database
Database_creation.py    = Create sqlite database
Insert_from_CSV_file.py = Read data from CSV file and insert into sqlite database
Retrieve_data_from_database.py = Retrieve data from the database


#Expected output file:
Output_gene_expression.csv

Here output will show any gene expressed at >50 RPKM.
In addition to the above output file, output will also be printed on the terminal as well.



#For Changing Query:

If you want to change query or RPKM cut off. You can do that in Retrieve_data_from_database.py script.
After changing query. You do not need to run Main.py. You need to run: python Retrieve_data_from_database.py.

You can change your query at line 29-30 of script, Retrieve_data_from_database.py:
cursor = conn.execute("select gene.Gene_id, Annotation, Expression_level, Pathway from gene, metadata, expression where gene.Gene_id=expression.Gene_id and metadata.Experiment_id=expression.experiment_id and Norm_method='RPKM'")

You can change RPKM cut off at line 34 of script, Retrieve_data_from_database.py:
if rows[i][2] > 50:
