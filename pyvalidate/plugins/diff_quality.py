from diff_cover.tool import generate_quality_report
from diff_cover.violationsreporters.base import QualityReporter
from diff_cover.violationsreporters.violations_reporter import PylintDriver
from pyvalidate.plugin import Plugin


class DiffQuality(Plugin):

    @property
    def plugin_name(self):
        return 'DiffQuality'

    def run(self):
        quality_driver = PylintDriver()
        quality_reporter = QualityReporter(driver=quality_driver)
        quality_percentage = generate_quality_report(
            tool=quality_reporter, compare_branch='origin/master')
        return round(quality_percentage)
