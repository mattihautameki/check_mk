#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2013 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

group = "checkparams"

subgroup_applications = _("Applications, Processes &amp; Services")

register_check_parameters(
    subgroup_applications,
    "stalesvc",
    _("Parameter for stale Servicecheck"),
    Dictionary(
        help = _("All services older then 1.0 * checkinterval are reported to the check by the agent. Here you can set exceptions for named services or hosts by regex."),
        elements = [
            ("search_pattern",
             TextAreaUnicode(
	         title = _("Regex for service filtering or host"),
                 unit = _("regex"),
                 help = _("Format: $hostname|$service|warn|crit NEWLINE  $hostname1|$service1|warn|crit... when you use this rule make sure to deploy the most significat regex in the last line ('.*|.*|1.5|2.0')"),
                 default_value = ".*|.*|1.5|2.0",
             ),
            ),
            ("hide_pending",
             FixedValue(
                 "1",
                 totext = "",
	         title = _("Hide active checks which not yet succeded."), 
                 ),
            ),
        ]
    ),
    TextAscii(
        title = _("Name of service"),
        allow_empty = False,
    ),
    "dict",
)
