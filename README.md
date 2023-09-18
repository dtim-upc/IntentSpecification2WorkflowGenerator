# Ontology and Workflow Generation

## Requirements

- Python (3.11)
    - List of packages in `requirements.txt` (install with `pip install -r requirements.txt`)
        - PySHACL package available at [DTIM PySHACL repo](https://github.com/dtim-upc/pySHACL) (`requirements.txt`
          already
          has the correct link).
- Node.js (for the demo)
    - List of packages in `package.json` (install with `npm install`)

## Directory Structure

- `common/`: Common code for ontology and workflow generation, essentially namespace definition and base graph
  generation.
- `dataset_annotator/`: Code for annotating datasets with ontology terms. Check usage
  in [section below](#dataset-annotator).
- `demo/`: Code for the demo. Check usage in [section below](#demo).
- `experiment_lab`: Code for running the experiments. Check usage in [section below](#experiments).
- `ontologies/`: Ontology used in the project. Divided in three files:
    - [`tbox.ttl`](./ontologies/tbox.ttl): Schema of the Ontology.
    - [`cbox.ttl`](./ontologies/cbox.ttl): Taxonomies of the Ontology.
    - [`abox.ttl`](./ontologies/abox.ttl): Instances of the Ontology.
- `ontology_populator/`: Code for generating the ontology. Check usage in [section below](#ontology-generator).
- `pipeline_generator/`: Code for generating workflows. Check usage in [section below](#pipeline-generator).
- `pipeline_tranlsator`: Code for translating ontology workflows into KNIME workflows. Check usage
  in [section below](#pipeline-translator).

## Dataset Annotator

Utility script to annotate csv datasets with ontology terms.  
Reads all the csv files in the [`datasets`](./dataset_annotator/datasets) directory and outputs the annotated datasets
in the [`annotated_datasets`](./dataset_annotator/annotated_datasets) directory.  
Must be run from the `dataset_annotator` directory.

```bash
cd dataset_annotator
python3 main.py
```

## Experiments

## Ontology Populator

## Pipeline Generator

## Pipeline Translator

## Demo
