
class Search:
    def __init__(self, api):
        self.api = api

    def tweets(self, words: str):
        return self.api.search(words, lang='pt')

    def find_hashtags(self, terms, location=23424768):
        # BRAZIL_WOEID = 23424768
        trends = self.api.trends_place(location)
        hashtags = [t["name"] for t in trends[0]["trends"] if t["name"].startswith("#")]
        matched_hashtags = [
            ht for term in terms for ht in hashtags if term.lower() in ht.lower()
        ]
        return matched_hashtags
