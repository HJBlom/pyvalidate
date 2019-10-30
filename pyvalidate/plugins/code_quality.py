from pylint.lint import Run
from pyvalidate.plugin import Plugin


class CodeQuality(Plugin):

    @property
    def plugin_name(self) -> str:
        return "CodeQuality"

    def run(self) -> int:
        results = Run([self.module_name], do_exit=False)
        score = round(results.linter.stats.get('global_note', 0) * 10, 0)
        return score
