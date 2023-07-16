import httpx

from squiz.types import Username
from squiz.abc import BaseModule, BaseModel


class GithubResponse(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    html_url: str
    type: str
    site_admin: bool
    name: str
    company: str | None
    blog: str
    location: str | None
    email: str | None
    hireable: bool
    bio: str | None
    twitter_username: str | None
    public_repos: int
    public_gists: int
    followers: int
    following: int

    render_fields = {
        "Username": "login",
        "ID": "id",
        "PFP": "avatar_url",
        "Gravatar": "gravatar_id",
        "Profile": "html_url",
        "Account type": "type",
        "Display name": "name",
        "Company": "company",
        "Blog": "blog",
        "Location": "location",
        "Email": "email",
        "Hireable": "hireable",
        "Bio": "bio",
        "Twitter": "twitter_username",
        "Repos": "public_repos",
        "Gists": "public_gists",
        "Followers": "followers",
        "Following": "following",
    }


class Module(BaseModule):
    name = "Github"
    target_types = (Username,)

    def execute(self, **kwargs):
        with self.ignore():
            self < GithubResponse(
                **httpx.get(f"https://api.github.com/users/{kwargs['target']}")
            )
