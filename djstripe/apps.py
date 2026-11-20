"""
dj-stripe - Django + Stripe Made Easy
"""
from importlib.metadata import version

from django.apps import AppConfig

__version__ = version("dj-stripe")


class DjstripeAppConfig(AppConfig):
    """
    An AppConfig for dj-stripe which loads system checks
    and event handlers once Django is ready.
    """

    name = "djstripe"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        import stripe

        from . import (  # noqa: Register the checks and event handlers
            checks,
            event_handlers,
        )

        # Set app info
        # https://stripe.com/docs/building-plugins#setappinfo
        stripe.set_app_info(
            "dj-stripe",
            version=__version__,
            url="https://github.com/dj-stripe/dj-stripe",
        )
