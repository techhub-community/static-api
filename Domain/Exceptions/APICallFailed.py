class APICallFailed(Exception):
    def __init__(self, statusCode):

        self.statusCode = statusCode

        self.message = "API call from failed with " + str(statusCode) + " status code"

        super().__init__(self.message)
