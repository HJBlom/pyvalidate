## Pyvalidate

Pyvalidate wraps **coverage**, **pytest**, **pylint**, **diff-cover** and **diff-quality**. By using pyvalidate,
we can ensure that our projects are tested and that our code is of good quality. This project is still in development
and should not be used on production systems.

### Plugins

Some sample plugins are available in the plugin directory. This will be updated to used more dynamically.

### Usage

```bash
$: pyvalidate --help
Usage: pyvalidate [OPTIONS] MODULE_PATH MODULE_NAME

Options:
  --exclude TEXT  List of relative paths to working directory to exclude from
                  testing.
  --version       Show the version and exit.
  --help          Show this message and exit.
```

### Example Usage

```bash
$: pyvalidate . pyvalidate

```
