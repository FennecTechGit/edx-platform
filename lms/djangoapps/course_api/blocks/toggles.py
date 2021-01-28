"""
Toggles for Course API.
"""


from edx_toggles.toggles import LegacyWaffleFlag, LegacyWaffleFlagNamespace  # lint-amnesty, pylint: disable=import-error

COURSE_BLOCKS_API_NAMESPACE = LegacyWaffleFlagNamespace(name=u'course_blocks_api')

# .. toggle_name: course_blocks_api.hide_access_denials
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to hide access denial messages in the course blocks.
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2019-09-27
# .. toggle_target_removal_date: None
# .. toggle_warnings: This temporary feature toggle does not have a target removal date.
# .. toggle_tickets: None
HIDE_ACCESS_DENIALS_FLAG = LegacyWaffleFlag(
    waffle_namespace=COURSE_BLOCKS_API_NAMESPACE,
    flag_name=u'hide_access_denials',
    module_name=__name__,
)
