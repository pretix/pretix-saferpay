from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretix_saferpay"
    verbose_name = "Saferpay (SIX) implementation for pretix"

    class PretixPluginMeta:
        name = gettext_lazy("Saferpay (SIX)")
        author = "Raphael Michel"
        category = "PAYMENT"
        visible = True
        picture = "pretix_saferpay/logo.svg"
        version = __version__
        compatibility = "pretix>=4.20.0"

        @property
        def description(self):
            t = gettext_lazy(
                "Accept payments through Saferpay, a payment method offered by Worldline (formerly SIX Payment Services)."
            )
            t += '<div class="text text-info"><span class="fa fa-info-circle"></span> '
            t += gettext_lazy(
                "Sometimes also referred to as PAYONE. Use this extension, if PAYONE has provided you with a "
                "<em>Customer ID</em>."
            )
            t += '</div>'

            return t

    def ready(self):
        from . import signals, tasks  # NOQA
