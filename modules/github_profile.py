import httpx

from typing import Optional

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
    company: Optional[str] = None
    blog: str
    location: Optional[str] = None
    email: Optional[str] = None
    hireable: bool
    bio: Optional[str] = None
    twitter_username: Optional[str] = None
    public_repos: int
    public_gists: int
    followers: int
    following: int

    render_fields: dict[str, str] = {
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
    name = "Github profile"
    target_types = (Username,)

    def execute(self, **kwargs):
        with self.ignore():
            self < GithubResponse(
                **httpx.get(f"https://api.github.com/users/{kwargs['target']}").json()
            )
