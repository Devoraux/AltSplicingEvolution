# AltSplicingEvolution
Here lives the master script for processing orthogroups. 
The script provided is given to you, the user, without any guarentee of user support. I am busy, but chances are if you need help just email me KADENISLAM@GMAIL.COM and I will probably be very flattered and help you.

This guide will be in three parts. You can read more about the programs and approaches of these python scripts in my thesis work detailed here at this link:
https://docs.google.com/document/d/1ukSkgzTakW6a2njR3FpanAXTtB2ENgC5mf9LB_Z66OQ/edit?usp=sharing

The parts detailed:
1. Creating gene orthogroups across species with PairwiseOrthogrouper
2. Creating exon orthogroups using Exorthist Output
3. Extracting PSI and Informative Reads from tissue samples using RMATS
4. Creating informative read and 
To use PairwiseOrthogrouper-
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
