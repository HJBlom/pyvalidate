from typing import Iterable

from pyvalidate.plugins import DiffCover, DiffQuality

# TODO - Refactor how plugins are loaded. This is set for testing purposes.
PLUGINS_TO_USE = [DiffCover, DiffQuality]


def run_plugins(module_path: str, module_name: str, exclude_paths: Iterable[str]) -> bool:
    scores = []

    # Run each plugin and keep track of it's score
    for plugin in PLUGINS_TO_USE:
        active_plugin = plugin(module_path, module_name, exclude_paths)

        print(f'Running: {active_plugin.plugin_name}')
        active_plugin.set_up()
        score = active_plugin.run()
        active_plugin.tear_down()

        scores.append(score)

    # Determine exit code based on scores.
    if any(map(lambda x: x < 90, scores)):
        # Fail if any plugin scored below 90%
        return 1
    return 0
