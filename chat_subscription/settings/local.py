from .base import *  # noqa

# MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "qinspect": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}


MEDIA_ROOT = "/tmp"
MEDIA_URL = "/files/"
