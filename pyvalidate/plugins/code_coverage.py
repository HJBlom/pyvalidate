from io import StringIO

from coverage import Coverage
from coverage.xmlreport import XmlReporter
from pytest import main

from pyvalidate.plugin import Plugin


class CodeCoverage(Plugin):

    @property
    def plugin_name(self) -> str:
        return 'CodeCoverage'

    def run(self) -> int:
        coverage = Coverage()
        coverage.start()
        exit_code = main(['-v', 'tests'])
        coverage.stop()

        # Set score to zero if exit code was non-zero
        if exit_code != 0:
            return 0

        # Generate xml report in StringIO file
        coverage.get_data()
        coverage.config.from_args(
            ignore_errors=None,
            report_omit=None,
            report_include=None,
            xml_output=None,
        )
        data = StringIO()
        reporter = XmlReporter(coverage, coverage.config)
        reporter.report(None, data)
        data.seek(0)

        return round(coverage.report(show_missing=True))
