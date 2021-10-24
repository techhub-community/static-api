import requests
import json

import sys, traceback

from Domain.Exceptions.APICallFailed import APICallFailed

import asyncio


class GithubService:
    def __init__(self):
        self.hostUrl = "https://api.github.com"
        self.endPoints = {
            "repos": "/users/techhub-community/repos",
            "contributors": "/repos/techhub-community/{repoName}/contributors"
        }

    async def getRepos(self):
        try:

            response = await requests.get(self.hostUrl +
                                          self.endPoints["repos"])
            if response.status_code != 200:
                raise APICallFailed(response.status_code)

            jsonResponse = json.loads(response.text)

            return jsonResponse

        except:
            raise Exception("Exception occured when parsing json response")

    async def getContributorsForRepo(self, repoName):

        try:

            response = await requests.get(
                self.hostUrl +
                self.endpoints["contributors"].replace("{repoName}", repoName))

            if response.status_code != 200:
                raise APICallFailed(response.status_code)

            jsonResponse = json.loads(response.text)

            return jsonResponse

        except:

            raise Exception("Exception occured when parsing json response")
