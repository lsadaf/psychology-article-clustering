# Psychology Article Clustering (NLP, University of Tehran)

This project collects psychology research articles from the University of Tehran, processes the abstracts and keywords using NLP (Persian text analysis), and then applies clustering techniques to discover thematic groups within the research corpus.  

## Project Overview
1. **Crawling** (`crawl.py`)  
   - Scrapes 300 article abstracts and keywords from [japr.ut.ac.ir](https://japr.ut.ac.ir).  
   - Saves results into a CSV (`all_articles300.csv`).  

2. **Keyword Extraction & NLP Processing** (`find_keywords.py`)  
   - Uses [Hazm](https://github.com/sobhe/hazm) for Persian text normalization, tokenization, lemmatization, and POS tagging.  
   - Filters irrelevant word types (punctuation, verbs, pronouns, etc.).  
   - Produces a cleaned list of keywords per article.  
   - Saves processed data into `all_keywords300.csv`.  

3. **Clustering Preparation** (`main.py`)  
   - Builds a term–document matrix from the cleaned keywords.  
   - Computes TF–IDF features for clustering and analysis.  
   - Saves matrices for further analysis (`.mat` files for MATLAB / Python).  

4. **Analysis**  
   - Clustered articles are grouped by topic.  
   - Each cluster is interpreted by reviewing its dominant terms and sample articles.  

## Project Structure
```
├── crawl.py # Crawl abstracts & keywords from University of Tehran psychology articles
├── find_keywords.py # NLP preprocessing with Hazm
├── main.py # Build matrices & TF-IDF for clustering
├── all_articles300.csv # Raw crawled data (URL, abstract, keywords)
├── all_keywords300.csv # Processed keywords (after NLP)
├── totaldocuments.mat # Saved term-document matrix
├── analysis.ipynb # Clustering + results interpretation
└── README.md # Project documentation
```
## Requirements
Install dependencies:  
```
pip install requests beautifulsoup4 hazm pandas numpy scipy scikit-learn matplotlib
```
## Usage
  1. **Crawl Data**
```
python crawl.py
```
  2. **Extract & Process Keywords**
```
python find_keywords.py
```
  3. **Prepare Matrices for Clustering**
```
python main.py
```
→ Saves term-document matrices (.mat format).

  4. **Run Clustering & Analysis**
    Open the Jupyter Notebook:
```
jupyter notebook analysis.ipynb
```
→ Performs clustering

## Results

  - 300 psychology articles crawled.

  - Cleaned Persian keywords extracted via Hazm NLP.

  - Term–document and TF–IDF matrices generated.

  - Clusters identified around themes such as cognitive psychology, clinical studies, and educational research.
