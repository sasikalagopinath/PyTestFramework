import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\configData.ini")

class ReadConfig:
    # @staticmethod # using static method, we can directly use it into our location
    # def getBaseURL(self):
    #     url = config.get("commonData", "baseURL")
    #     return url
    #
    # @staticmethod
    # def getUserName(self):
    #     username = config.get("commonData", "username")
    #     return username

    @staticmethod
    def getCommonData(rowKey, key_value):
        value = config.get(rowKey, key_value)
        return value