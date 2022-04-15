##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
