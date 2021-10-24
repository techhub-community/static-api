import os
import json


class GithubRepository:
    def __init__(self):

        dirname = os.path.dirname(__file__)
        self.reposDataFile = os.path.join(dirname, '../Data/githubRepos')
        with open(self.reposDataFile, "r") as f:
            self.githubRepos = json.load(f)

        self.contributorsDataFile = os.path.join(dirname,
                                                 '../Data/githubContributors')
        with open(self.contributorsDataFile, "r") as f:
            self.githubContributors = json.load(f)

        self.DatabaseFiles = {
            "repos": self.reposDataFile,
            "contributors": self.contributorsDataFile
        }

        self.DataBases = {
            "repos": self.githubRepos,
            "contributors": self.githubContributors
        }

    def getGithubReposData(self):
        return self.githubRepos

    def getGithubContributorsData(self):

        return self.githubContributors

    async def injectIntoReposDB(self, data):
        self.githubRepos = {
            "projects": data["projects"],
            "stars": data["stars"]
        }

        await self.__updateDB("repos")

    async def __updateDB(self, dbName):
        fileName = self.DatabaseFiles[dbName]

        data = self.Databases[dbName]

        try:
            with open(fileName, "w") as f:
                await json.dump(data, f, indent=2)

        except:

            raise Exception("Failed to write to DB")