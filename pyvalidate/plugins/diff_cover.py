from io import StringIO

from coverage import Coverage
from coverage.xmlreport import XmlReporter
from diff_cover.tool import GitPathTool, generate_coverage_report
from git import Repo
from pytest import main

from pyvalidate.plugin import Plugin


class DiffCover(Plugin):

    @property
    def plugin_name(self) -> str:
        return 'DiffCover'

    def set_up(self) -> None:
        GitPathTool.set_cwd(self.module_path)
        Repo(self.module_path).remotes.origin.fetch(refspec='master:refs/remotes/origin/master')

    def run(self) -> int:
        coverage = Coverage()
        coverage.start()
        exit_code = main(['-v', 'tests'])
        coverage.stop()

        # Early exit if pytest failed
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

        # Check diff cover compared to origin/master using xml
        score = generate_coverage_report(
            coverage_xml=[data],
            compare_branch='origin/master',
            exclude=self.exclude_paths)

        return score
