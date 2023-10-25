import unittest
import datetime
from newscover import fetch_latest_news

API_KEY=""

class _test_newscover(unittest.TestCase):
    def test_no_keyword(self):
        try:
            fetch_latest_news("APIKEY")
            assert False
        except AssertionError as e:
            assert True
    
    def test_lookback_days(self):
        latest_news = fetch_latest_news(API_KEY, "Apple", 12)

        current_date = datetime.date.today()
        lookback_date = current_date - datetime.timedelta(days=12)

        for news in latest_news['articles']:
            original_date = datetime.datetime.strptime(news['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            formatted_date = original_date.strftime("%Y-%m-%d")
            formatted_date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d").date()
            
            if formatted_date < lookback_date:
                assert False
        
        assert True

    def test_invalid_keyword(self):
        try:
            fetch_latest_news(API_KEY, "Ap1ple", 12)
            assert False
        except AssertionError as e:
            assert True
        
    

if __name__ == "__main__":
    unittest.main()