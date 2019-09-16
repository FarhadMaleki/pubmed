# pub

The purpose of **pub** is to make extraction of data from PubMed baseline files painless. The data provided by PubMed can be used for a variety of applications including training Natural Language Processing (NLP) models for applications in the Biomedical domain.

> PubMed is a free search engine accessing primarily the MEDLINE database of references and abstracts on life sciences and biomedical topics. The United States National Library of Medicine (NLM) at the National Institutes of Health maintains the database as part of the Entrez system of information retrieval.
> WIKIPEDIA


## Prerequisites

See _**requirements.txt**_ for the list of requirements.

## Installing
It is a good practice to use a virtual environment for deploying Python programs. Using **conda**, we will create an environment named *pub*. The environment name is arbitrary.

```bash
conda create -n pub python=3.6
```
To install requirements, the following command can be run.

```bash
make setup
```

## Running the tests

Regression tests can be run through the following command:

```bash
make regression
```

## Adding more tests

New tests should be added as modules where their names start with *`test_`* under the **test** directory.

## Downloading baseline files
### Creating link addresses
As link addresses change from time to time, and it is easy to compile a text file containg these links, we leave creating link addresses to the user. One can write a simple script or use command line tools to create such a file. See [**Get the Data via Bulk Download**](https://www.nlm.nih.gov/databases/download/pubmed_medline.html)

For example, on a linux machine you could use the following commands:
```bash
echo -e pubmed/baseline/pubmed19n{0001..0972}.xml.gz | tr " " "\n" > links.txt
echo -e pubmed/updatefiles/pubmed19n{0973..1476}.xml.gz | tr " " "\n" >> links.txt
```

_**Note**: The file pattern used above might change from time to time (often on a yearly basis)._

### Downloading from FTP
You can use **pubmed.py** from the command line or use the `downloader` function from [pub.utils](https://github.com/FarhadMaleki/pubmed/blob/master/pub/utils.py) to download PubMed baseline files.
```bash
python pubmed.py --config    '/path/to/config/file' \
                 --link_file '/path/to/file/containing/links' \
                 --proc 4 \
                 --output_dir '/path/to/output/directory'
```
_**Note**: You should choose the number of processes (4 in the above example) based on you bandwidth and the number of processors available._

### Loading article data
You can use `corpra` methods from [pub.utils](https://github.com/FarhadMaleki/pubmed/blob/master/pub/utils.py) to load data (see the documentation).
You might need to update the config file, which is a JSON file, to extract different information for each article (see an example of a config file [here](https://github.com/FarhadMaleki/pubmed/blob/master/test/data/config.json)).

## Authors

* [**Farhad Maleki**](https://github.com/FarhadMaleki) - *Initial work* 

