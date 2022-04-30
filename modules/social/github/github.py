import httpx

from typing import Optional

from squiz.abc import BaseModel, BaseModule
from squiz.types import Username


class GitHubProfile(BaseModel):
    login: str
    avatar_url: str
    html_url: str
    followers: int
    created_at: str
    updated_at: str

    name: Optional[str]
    location: Optional[str]
    email: Optional[str]
    bio: Optional[str]
    twitter_username: Optional[str]

    @property
    def created_at_date(self) -> str:
        """Get the date"""
        return self.created_at.split("T")[0]

    @property
    def updated_at_date(self) -> str:
        """Get the date"""
        return self.updated_at.split("T")[0]

    render_fields = {
        "Name": "name",
        "Username": "login",
        "URL": "html_url",
        "Followers": "followers",
        "Location": "location",
        "Avatar": "avatar_url",
        "Email": "email",
        "Bio": "bio",
        "Twitter": "twitter_username",
        "Created": "created_at_date",
        "Updated": "updated_at_date",
    }


class Module(BaseModule):
    name = "GitHub"
    target_types = (Username,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = httpx.get(f"https://api.github.com/users/{target.value}")

        try:
            data = GitHubProfile(**response.json())
        except Exception:
            return

        self.results.append(data)
