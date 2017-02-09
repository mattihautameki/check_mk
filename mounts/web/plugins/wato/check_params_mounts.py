group = "checkparams"

subgroup_applications = _("Applications, Processes &amp; Services")
register_check_parameters(
    subgroup_storage,
    "fs_mount_options",
    _("Filesystem mount options (Linux/UNIX)"),
    Dictionary(
        elements = [
            ( "must_contain",
                ListOfStrings(
                   title = _("Options must contain"),
                   help = _("Specify all mount options here which have to be in use on "
                     "the specific mountpoint and/or host. Options specified here will "
                     "be shown as missing when they are not in use."),
                   valuespec = TextUnicode(),
                ),
            ),
            ( "must_not_contain",
                ListOfStrings(
                   title = _("Options must not contain"),
                   help = _("Specify all mount options which are not allowed. Options "
                     "specified here will be shown as exceeding when this options are "
                     "in use."),
                   valuespec = TextUnicode(),
                ),
            ),
            ( "exact_match",
                ListOfStrings(
                   title = _("List of exact mount options"),
                   help = _("Specify all expected mount options here. If the list of "
                     "actually found options differs from this list, the check will go "
                     "warning or critical. Just the option <tt>commit</tt> is being "
                     "ignored since it is modified by the power saving algorithms."),
                   valuespec = TextUnicode(),
                ),
            ),
        ],
    ),
    TextAscii(
        title = _("Mount point"),
        allow_empty = False),
    "dict"
)

