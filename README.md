# newscover_data_collection

```newsapi.py``` file contains a function ```fetch_latest_news(api_key, news_keywords, lookback_days=10)```.
The function queries the NewsAPI and returns a python list of english news articles (represented as dictionaries) containing those news keywords and published within the last <lookback_days>.

```newscover.collector.py``` file contains a CLI tool which contains -k, -b, -i, -o flags which refers to api key, number of days to lookback, input file, output directory. The input file is a json file containing a dictionary of named keyword lists. Like this
```{ “trump_fiasco”: [“trump”, “trial”], “swift”: [“taylor”, “swift”, “movie”] }```. For each keyword set with name N and keyword list X, the collector will execute a query for the keywords X and write the results to the <output_dir>/N.json.