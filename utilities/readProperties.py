import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURl():
        url = config.get('common info', 'base_URL')
        return url

    @staticmethod
    def getAdminEmail():
        adminEmail = config.get('common info', 'adminEmail')
        return adminEmail

    @staticmethod
    def getAdminPassword():
        password = config.get('common info', 'password')
        return password
