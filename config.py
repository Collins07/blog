SECRET_KEY = '8f8c465d65eee4aacfe130cc64db80a7'


class Config:
    '''
    General configuration parent class
    '''



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}