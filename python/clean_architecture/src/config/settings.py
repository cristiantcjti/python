from decouple import config


class Config:
    """
    Base configuration, this class contains most of the variables and default values.
    """

    ENVIRONMENT = config("ENVIRONMENT")
    DATABASE_NAME = config("DATABASE_NAME")
    DATABASE_USER = config("DATABASE_USER")
    DATABASE_PASSWORD = config("DATABASE_PASSWORD")
    DATABASE_HOST = config("DATABASE_HOST")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    """Configuration to be used on Production."""

    pass


class Homolog(Config):
    """Configuration to be used on Homolog."""

    pass


class Qa(Config):
    """Configuration to be used on Qa."""

    pass


class Stage(Config):
    """Configuration to be used on Staging."""

    pass


class Development(Config):
    """Configuration to be used during development."""

    pass


class Testing(Config):
    """Testing configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_ECHO = False
