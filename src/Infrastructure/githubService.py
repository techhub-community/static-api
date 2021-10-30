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

            response = await self.__callGetAPI(self.hostUrl +
                                               self.endPoints["repos"])



            return response

        except (Exception):
            raise Exception(Exception.message)

    async def getContributorsForRepo(self, repoName):

        try:

            response = await self.__callGetAPI(
                self.hostUrl +
                self.endpoints["contributors"].replace("{repoName}", repoName))

            return response

        except(Exception):

            raise Exception(Exception.message)

    async def __callGetAPI(url, headers={}):

        try:

            response = await requests.get(url, headers=headers)
            if response.status_code != 200:
                raise APICallFailed(response.status_code)

            jsonResponse = json.loads(response.text)

            return jsonResponse

        except:

            raise Exception("Exception occured when parsing json response")