class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = 'oaipb5mjcth77st8t9qds75e19bpgpia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.rambler.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "gb_flask@ro.ru"
    MAIL_PASSWORD = "Zghjuhfvvbcn0505"
