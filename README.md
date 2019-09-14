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

New tests should be added as modules where their names start with *test_* under *test* directory.


## Authors

* [**Farhad Maleki**](https://github.com/FarhadMaleki) - *Initial work* 

