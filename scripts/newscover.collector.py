import argparse 
import json
import os
from src.newscover import fetch_latest_news

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', required=True, help="api key for NewsAPI")
    parser.add_argument('-b', '--days', default=10, help="news articles published within the last given days")
    parser.add_argument('-i', '--input', required=True, help="input file is a json file containing a dictionary of named keyword lists")
    parser.add_argument('-o', '--output', required=True, help="directory that we want to store the outputs into")

    args = parser.parse_args()

    api_key = args.key
    lookback_days = args.days
    input_json = args.input
    output_dir = args.output

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(input_json, 'r') as json_file:
        data = json.load(json_file)

    for name, keywords in data.items():
        for keyword in keywords:
            file_path = output_dir + "/" + name + ".json"
            with open(file_path, "w") as output_file:
                news = fetch_latest_news(api_key, keyword, lookback_days)
                json.dump(news, output_file)


if __name__ == "__main__":
    main()