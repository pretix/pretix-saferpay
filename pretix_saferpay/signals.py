import logging
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from pretix.base.settings import settings_hierarkey
from pretix.base.signals import logentry_display, register_payment_providers

logger = logging.getLogger(__name__)


@receiver(register_payment_providers, dispatch_uid="payment_saferpay")
def register_payment_provider(sender, **kwargs):
    from .payment import (
        SaferpayBancontact, SaferpayCC, SaferpayEPrzelewy, SaferpayEPS,
        SaferpayGiropay, SaferpayIdeal, SaferpayPaydirekt, SaferpayPayPal,
        SaferpayPostfinanceCard, SaferpayPostfinancePay, SaferpayPostfinanceEfinance,
        SaferpaySepadebit, SaferpaySettingsHolder, SaferpaySofort,
        SaferpayTwint, SaferpayWero,
    )

    return [
        SaferpayBancontact,
        SaferpayEPrzelewy,
        SaferpayCC,
        SaferpayEPS,
        SaferpayGiropay,
        SaferpayIdeal,
        SaferpayPaydirekt,
        SaferpayPayPal,
        SaferpayPostfinanceCard,
        SaferpayPostfinanceEfinance,
        SaferpayPostfinancePay,
        SaferpaySepadebit,
        SaferpaySettingsHolder,
        SaferpaySofort,
        SaferpayTwint,
        SaferpayWero,
    ]


@receiver(signal=logentry_display, dispatch_uid="saferpay_logentry_display")
def pretixcontrol_logentry_display(sender, logentry, **kwargs):
    if not logentry.action_type.startswith("pretix_saferpay.event"):
        return

    plains = {
        "paid": _("Payment captured."),
        "authorized": _("Payment authorized."),
    }
    text = plains.get(logentry.action_type[22:], None)
    if text:
        return _("Saferpay reported an event: {}").format(text)


settings_hierarkey.add_default("payment_saferpay_method_cc", True, bool)
