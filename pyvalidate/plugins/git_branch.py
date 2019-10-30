from git import Repo
from pyvalidate.plugin import Plugin


class BranchChecker(Plugin):

    @property
    def plugin_name(self):
        return "BranchChecker"

    def run(self):
        repo = Repo(self.module_path)
        branch_name = repo.active_branch.name
        # TODO -> Branch validation
        print(branch_name)
