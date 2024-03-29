# AltSplicingEvolution
by Imon Islam under the mentorship of Dr.Rori Rohlfs

Here lives the master script for processing orthogroups. 
The script provided is given to you, the user, without any guarentee of user support. I am busy, but chances are if you need help just email me iislam@ucsc.edu and I will probably be very flattered and help you.

You can read more about the programs and approaches of these python scripts in my thesis work detailed here at this link:
https://docs.google.com/document/d/1ukSkgzTakW6a2njR3FpanAXTtB2ENgC5mf9LB_Z66OQ/edit?usp=sharing

This guide will be in four parts. 
The parts detailed:
1. Creating gene orthogroups across species with PairwiseOrthogrouper() and Biomart Output
2. Creating exon orthogroups using Exorthist Output
3. Extracting PSI and Informative Reads from tissue samples using RMATS

-Part 1-

First, to create gene orthogroups across species you must download the data using wget. 
The following guide was created to obtain the data:
https://docs.google.com/document/d/12nzD852h4yZrDyAp7i9CY1Z_lW6P5exgP9wV08Yy-xg/edit?usp=sharing

Once you have the data downloaded via wget, your next step is to enter the path for each file into the PairwiseOrthogrouper.py script. 

Download the script PairwiseOrthogrouper and put each path for your new biomart files into the respective spots (line 35 for Human-Mouse, line 48 for Human-Chicken, line 61 for Human-Rat, line 74 for Human-Rabbit, line 87 for Human-Opossum, line 100 for Human-Macaque)

Run the script by doing the following:
python PairwiseOrthogrouper.py 
You should then have your orthogroups. Save them to a text file of some sort to be used later.

-Part 2- 

Now that you have gene orthogroups, you will use them on a program called ExoOrthist. ExOrthist takes gene orthogroups created in step 1, and a few other things, to create pairwise exon orthology observations. 
You can read about how to use the main module of ExOrthist to obtain exon pairwise data here: 
https://docs.google.com/document/d/1vBJEkIbb_eFh-QRguPwa__8DYfuvs8p5Jg7Rz0t6Bso/edit?usp=sharing

Not very straightforward, but the ultimate outcome will be a file called 'filtered_best_scored_EX_matches_by_targetgene.tab' which you will then use to create exon orthogroups. 

To take this file and create exon orthogroups, download the ExonOrthogroupMaker.py and put the path of your 'filtered_best_scored_EX_matches_by_targetgene.tab' into line 152. Run the program and you should have your exon orthogroups. If the script takes too long, then you can run it on subsets of the gene orthogroups. 

Ideally you dont have to run the script because I have included the exon orthogroups in this github for your convienience. It is the file called "BensMethodSecondAttempt.txt"

-Part 3-

To derive PSI and informative reads from developmentally equivalent samples of Cardosa Moriera data, you should read about how I did it, what options I used, and some results examples here: https://docs.google.com/document/d/1viXVaTFam4ReopJsc_8ZWqS0xQAc4uy9Go58Q6wfm54/edit?usp=sharing
