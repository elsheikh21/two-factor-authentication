from twilio.rest import Client
from random import randint
from configparser import ConfigParser

account_sid = ''
auth_token = ''
from_phone = ''
rand = ''


def setDefaults():
    cfg = ConfigParser()
    cfg.read('config.ini')
    account_sid = cfg.get('TwilioConfigurationParameters', 'account_sid')
    auth_token = cfg.get('TwilioConfigurationParameters', 'auth_token')
    from_phone = cfg.get('TwilioConfigurationParameters', 'from_phone')
    rand = randint(1000, 9999)
    # sendMessage(account_sid, auth_token, from_phone, rand)

# Write to configuration files


def writeToConfig():
    cfg = ConfigParser()
    # """ WRITE TO CONFIG FILE """
    cfg['TwilioConfigurationParameters'] = {}
    cfg['TwilioConfigurationParameters']['account_sid'] = 'AC5e6226d3ec01c1b13f9ab8a52e641beb'
    cfg['TwilioConfigurationParameters']['auth_token'] = '485fccb21d77f3f7e1eb7b2fcc7ce7c5'
    cfg['TwilioConfigurationParameters']['from_phone'] = '+18285481610'

    # """ OR """
    # cfg['TwilioConfigurationParameters'] = {'account_sid': 'AC5e6226d3ec01c1b13f9ab8a52e641beb',
    # 'authentication_token': '485fccb21d77f3f7e1eb7b2fcc7ce7c5',
    # 'from_number': '+18285481610'}
    with open('config.ini', 'w') as configfile:
        cfg.write(configfile)

# Read from configuration files


def readFromConfig():
    cfg = ConfigParser()
    cfg.read('config.ini')
    # print(cfg.sections())
    # print(cfg.items())
    # print(cfg.getboolean())
    # print(cfg.getint())
    print(cfg.get('TwilioConfigurationParameters', 'auth_token'))

# def sendMessage(account_sid, auth_token, from_phone, rand):
#     client = Client(account_sid, auth_token)
#     msg = client.messages.create(
#         to="+201117770505",
#         from=str(from_phone),
#         body="your authentication code is: " + str(rand)
#     )


if __name__ == "__main__":
    setDefaults()
    print("Auth_TOKEN: " + auth_token)
    # app.run()
