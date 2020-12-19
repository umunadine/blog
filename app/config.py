import os 


class Config:
    '''
    General configuration parent class
    '''
    QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    pass



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
    QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    DEBUG = True