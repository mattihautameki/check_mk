#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

group = "checkparams"

subgroup_applications = _("Applications, Processes &amp; Services")

register_check_parameters(
    subgroup_applications,
    "clamav",
    _("Times for clamav database age."),
    Dictionary(
        help = _("Here you can override the default levels for the clamav check."),
        elements = [
            ( "max_old",
                Tuple(
                title = _("Age of CVD"),
                elements = [
                    Integer(title = _("Warning at"), default_value = 48, unit = _("hours")),
                    Integer(title = _("Critical at"), default_value = 72, unit = _("hours")),
                ],
                ),
            ),
        ],
    ),
    TextAscii(
        title = _("Name of service"),
        allow_empty = False,
    ),
    "dict",
)

