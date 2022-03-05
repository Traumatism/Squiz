import requests

from squiz.base import BaseModel, BaseModule
from squiz.types import Username

URL = (
    "https://twitter.com/i/api/graphql/7mjxD3-C6BxitPMVQ6w0-Q/UserByScreenName"
)

TOKEN = (
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
    "%3D"
    "1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
)


PAYLOAD = (
    "{"
    '"screen_name":"%s"'
    ',"withSafetyModeUserFields":true,"withSuperFollowsUserFields":true'
    "}"
)


class TwitterLegacy(BaseModel):
    """ Twitter legacy model """
    created_at: str
    description: str
    favourites_count: int
    followers_count: int
    friends_count: int
    location: str
    name: str
    url: str
    screen_name: str

    render_fields = {
        "Name": "name",
        "Screen name": "screen_name",
        "Description": "description",
        "Location": "location",
        "URL": "url",
        "Followers": "followers_count",
        "Following": "friends_count",
        "Favs": "favourites_count",
        "Creation date": "created_at"
    }


class Module(BaseModule):
    name = "Twitter"
    target_types = (Username,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        headers = {
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://twitter.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0",
            "x-twitter-active-user": "yes",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,bn;q=0.8",
            "x-twitter-client-language": "en",
            "authorization": f"Bearer {TOKEN[0]}",
        }

        response = requests.get(
            URL,
            headers=headers,
            params={"variables": PAYLOAD % target}
        )

        try:
            results = response.json()["data"]["user"]["result"]
            self.results.append(TwitterLegacy(**results["legacy"]))
        except Exception:
            return
