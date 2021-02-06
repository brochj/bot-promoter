
class Search:
    BRAZIL_WOEID = 23424768

    def __init__(self, api):
        self.api = api

    def tweets(self, words: str):
        return self.api.search(words, lang='pt')

    def trends(self, location=BRAZIL_WOEID) -> list:
        trends = self.api.trends_place(location)
        return [t["name"] for t in trends[0]["trends"]]

    def trend_hashtags(self, location=BRAZIL_WOEID) -> list:
        trends = self.api.trends_place(location)
        hashtags = [t["name"] for t in trends[0]["trends"] if t["name"].startswith("#")]
        return hashtags

    def matched_hashtags(self, terms, location=BRAZIL_WOEID) -> list:
        hashtags = self.trend_hashtags()
        matched_hashtags = [
            ht for term in terms for ht in hashtags if term.lower() in ht.lower()
        ]
        return matched_hashtags

    def matched_trends(self, terms, location=BRAZIL_WOEID) -> list:
        trends = self.trends()
        matched_trends = [
            td for term in terms for td in trends if term.lower() in td.lower()
        ]
        return matched_trends
