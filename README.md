#### search_articles
Find projects in NCBI BioProject db with query key words and check if they are linked to any articles in PubMed Central (search.py)

Output: 
* Output.txt (accession number + article id + title + abstract)
* ids_checked.txt (BioProject ids already checked with a script. The script goes through this file not to double-check the same project again in case if you run the script several times)
* Error (BioProject ids which were found with key words you specified, but any further NCBI server requests failed for them. They still can be linked to articles!)
