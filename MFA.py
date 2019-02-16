from configparser import ConfigParser
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client
from authy.api import AuthyApiClient

class MFA:
    account_sid = ''
    authy_api_key = ''
    auth_token = ''
    from_phone = ''
    rand = ''
    email = ''
    password = ''

    def __init__(self):
        cfg = ConfigParser()
        cfg.read('config.ini')
        self.account_sid = cfg.get('TwilioConfigurationParameters', 'account_sid')
        self.auth_token = cfg.get('TwilioConfigurationParameters', 'auth_token')
        self.from_phone = cfg.get('TwilioConfigurationParameters', 'from_phone')
        self.authy_api_key = cfg.get('AuthyConfigurationParameters', 'authy_api_key')
        self.rand = randint(100000, 999999)
        self.email = cfg.get('EmailConfigurationParameters', 'email')
        self.password = cfg.get('EmailConfigurationParameters', 'password')

    # Write to configuration files
    def write_to_config(self):
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
    def read_from_config(self):
        cfg = ConfigParser()
        cfg.read('config.ini')
        # print(cfg.sections())
        # print(cfg.items())
        # print(cfg.getboolean())
        # print(cfg.getint())
        print(cfg.get('TwilioConfigurationParameters', 'auth_token'))

    # Send a sms
    def send_sms(self):
        client = Client(self.account_sid, self.auth_token)
        msg = client.messages.create(
            body="your authentication code is: " + str(self.rand),
            to="+393272180358",
            from_=self.from_phone
        )
        print(msg.status)

    # Call a phone number
    def voice_call(self):
        client = Client(self.account_sid, self.auth_token)
        call = client.calls.create(
            to="+201117091566",
            from_=self.from_phone,
            url="https://demo.twilio.com/welcome/sms/reply/"
        )
        print(call.status)

    # Verifying using Authy
    def authy_verify(self, to_number, country_code):
        authy_api = AuthyApiClient(self.authy_api_key)
        request = authy_api.phones.verification_start(to_number, country_code, via='sms', locale='en')
        print(request.content)

    # send an email
    def send_email(self):
        from_email = self.email
        password = self.password
        to_email = ''

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Multi-Factor Authentication'

        body = "your authentication code is: " + str(self.rand)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

mfa = MFA()
mfa.send_sms()
