import asyncio

from Infrastructure.githubService import GithubService

from Persistance.githubRepository import GithubRepository


class UpdateGithubDetails:
    def __init__(self):

        self._githubService = GithubService()

        self._githubRepository = GithubRepository()

    def updateGithubDetails(self):

        contributors, repos = asyncio.gather(
            self._githubService.getContributorsForRepo(),
            self._githubService.getRepos())


        



