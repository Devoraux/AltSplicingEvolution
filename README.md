# AltSplicingEvolution
Here lives the master script for processing orthogroups. 
The script provided is given to you, the user, without any guarentee of user support. I am busy, but chances are if you need help just email me KADENISLAM@GMAIL.COM and I will probably be very flattered and help you. You can modify this python script however you need, but chances are youll probably break it. 

Its not exactly simple to use, you might need some python experience, just find the full path's to your files and place them into the appropriate places in the python script. Depending on which method youll use, you will need to call on it in the main function at the bottom of the script. Once youve done this, enter into your terminal:

If using AllPossibleOrthogrouper-
python DataSorter.py < AllPossibleOrthogroups.txt > results.txt

If using PairwiseOrthogrouper-
python DataSorter.py > results.txt

To extract pairwise species data, do this:












In order to receive the data for AllPossibleOrthogrouper, enter this into your command prompt:

wget -O AllPossibleOrthogroups.txt 'http://www.ensembl.org/biomart/martservice?query=
Then paste this and hit enter:
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Attribute name = "ensembl_gene_id" /><Attribute name = "mmusculus_homolog_ensembl_gene" /><Attribute name = "ggallus_homolog_ensembl_gene" /><Attribute name = "rnorvegicus_homolog_ensembl_gene" /><Attribute name = "ocuniculus_homolog_ensembl_gene" /><Attribute name = "mdomestica_homolog_ensembl_gene" /><Attribute name = "mmulatta_homolog_ensembl_gene" /></Dataset></Query>’
In order to receive the data for AllPossibleOrthogrouper, enter this into your command prompt:

wget -O AllPossibleOrthogroups.txt 'http://www.ensembl.org/biomart/martservice?query=
Then paste this query:

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Attribute name = "ensembl_gene_id" /><Attribute name = "mmusculus_homolog_ensembl_gene" /><Attribute name = "ggallus_homolog_ensembl_gene" /><Attribute name = "rnorvegicus_homolog_ensembl_gene" /><Attribute name = "ocuniculus_homolog_ensembl_gene" /><Attribute name = "mdomestica_homolog_ensembl_gene" /><Attribute name = "mmulatta_homolog_ensembl_gene" /></Dataset></Query>
Then add a closing apostrophe(‘) and hit enter.

In order to receive the data for PairwiseOrthogrouper, repeat the above steps but instead of the one large query, you must now wget 6 separate queries into your command prompt. Don't forget the apostrophe after each query. 

For Human-Mouse Pairwise Data-
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Filter name = "with_mmusculus_homolog" excluded = "0"/><Attribute name = "ensembl_gene_id" /><Attribute name = "mmusculus_homolog_ensembl_gene" /><Attribute name = "mmusculus_homolog_orthology_type" /></Dataset></Query>
For Human-Chicken Pairwise Data-
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Filter name = "with_ggallus_homolog" excluded = "0"/><Attribute name = "ensembl_gene_id" /><Attribute name = "ggallus_homolog_ensembl_gene" /><Attribute name = "ggallus_homolog_orthology_type" /></Dataset></Query>
For Human-Rat Pairwise Data- 
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Filter name = "with_rnorvegicus_homolog" excluded = "0"/><Attribute name = "ensembl_gene_id" /><Attribute name = "rnorvegicus_homolog_ensembl_gene" /><Attribute name = "rnorvegicus_homolog_orthology_type" /></Dataset></Query>
For Human-Rabbit Pairwise Data-
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Filter name = "with_ocuniculus_homolog" excluded = "0"/><Attribute name = "ensembl_gene_id" /><Attribute name = "ocuniculus_homolog_ensembl_gene" /><Attribute name = "ocuniculus_homolog_orthology_type" /></Dataset></Query>
For Human-Opossum Pairwise Data-
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Filter name = "with_mdomestica_homolog" excluded = "0"/><Attribute name = "ensembl_gene_id" /><Attribute name = "mdomestica_homolog_ensembl_gene" /><Attribute name = "mdomestica_homolog_orthology_type" /></Dataset></Query>
For Human-Macaque Pairwise Data-
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "CSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Filter name = "with_mmulatta_homolog" excluded = "0"/><Attribute name = "ensembl_gene_id" /><Attribute name = "mmulatta_homolog_ensembl_gene" /><Attribute name = "mmulatta_homolog_orthology_type" /></Dataset></Query>
