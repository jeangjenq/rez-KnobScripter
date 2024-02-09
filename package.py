name = "nuke_KnobScripter"
version = "3.1"
authors = [
    "Adrian Pueyo"
]

description = \
    """
    KnobScripter is a full script editor for Nuke that can script python
    on .py files and knobs as well as BlinkScript, with all the functionality
    from the default script editor in Nuke plus syntax helpers,predictions,
    snippets and other handy features.
    """

build_command = "python {root}/build.py"

requires = []

_category = "ext"

def commands():
    env.NUKE_PATH.append("{root}")