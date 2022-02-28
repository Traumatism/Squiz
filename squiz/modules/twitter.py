# import requests

# from squiz.base import BaseModel, BaseModule
# from squiz.types import Username

# URL = (
#     "https://twitter.com/i/api/graphql/7mjxD3-C6BxitPMVQ6w0-Q/UserByScreenName"
# )

# TOKEN = (
#     "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
#     "%3D"
#     "1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",

#     "1497099626842931201"
# )


# PAYLOAD = (
#     '{'
#     '"screen_name":"%s"'
#     ',"withSafetyModeUserFields":true,"withSuperFollowsUserFields":true'
#     '}'
# )


# class TwitterLegacy(BaseModel):
#     """ Twitter legacy model """
#     created_at: str
#     description: str
#     favourites_count: int
#     followers_count: int
#     friends_count: int
#     location: str
#     name: str
#     url: str
#     screen_name: str

#     render_fields = {
#         "Name": "name",
#         "Screen name": "screen_name",
#         "Description": "description",
#         "Location": "location",
#         "URL": "url",
#         "Followers": "followers_count",
#         "Following": "friends_count",
#         "Favs": "favourites_count",
#         "Creation date": "created_at"
#     }


# class Module(BaseModule):
#     name = "Twitter"
#     target_types = (Username,)

#     def execute(self, **kwargs):
#         target = kwargs["target"]

#         headers = {
#             "content-type": "application/json",
#             "x-twitter-client-language": "en",
#             "x-twitter-active-user": "yes",
#             "x-guest-token": TOKEN[1],
#             "authorization": f"Bearer {TOKEN[0]}",
#         }

#         response = requests.get(
#             URL,
#             headers=headers,
#             params={"variables": PAYLOAD % target}
#         )

#         try:
#             results = response.json()["data"]["user"]["result"]
#             self.results.append(TwitterLegacy(**results["legacy"]))
#         except Exception:
#             return self.ExecutionError("Unexpected JSON response")

#         return self.ExecutionSuccess()
