"""
Current version constant plus version pretty-print method.

This functionality is contained in its own module to prevent circular import
problems with ``__init__.py`` (which is loaded by setup.py during installation,
which in turn needs access to this version information.)

Borrowed from `fabric`.
"""

VERSION = (0, 3, 0, 'final', 0)


def get_version(form='short'):
    """
    Return a version string for this package, based on `VERSION`.

    Takes a single argument, ``form``, which should be one of the following
    strings:

    * ``branch``: just the major + minor, e.g. "0.2", "1.0".
    * ``short`` (default): compact, e.g. "0.2rc1", "0.2.0". For package
      filenames or SCM tag identifiers.
    * ``normal``: human readable, e.g. "0.2", "0.2.7", "0.2 beta 1". For e.g.
      documentation site headers.
    * ``verbose``: like ``normal`` but fully explicit, e.g. "0.2 final". For
      tag commit messages, or anywhere that it's important to remove ambiguity
      between a branch and the first final release within that branch.
    """
    # Setup
    versions = {}
    branch = "%s.%s" % (VERSION[0], VERSION[1])
    tertiary = VERSION[2]
    type_ = VERSION[3]
    final = (type_ == "final")
    type_num = VERSION[4]
    firsts = "".join([x[0] for x in type_.split()])

    # Branch
    versions['branch'] = branch

    # Short
    v = branch
    if (tertiary or final):
        v += "." + str(tertiary)
    if not final:
        v += firsts
        if type_num:
            v += str(type_num)
    versions['short'] = v

    # Normal
    v = branch
    if tertiary:
        v += "." + str(tertiary)
    if not final:
        if type_num:
            v += " " + type_ + " " + str(type_num)
        else:
            v += " pre-" + type_
    versions['normal'] = v

    # Verbose
    v = branch
    if tertiary:
        v += "." + str(tertiary)
    if not final:
        if type_num:
            v += " " + type_ + " " + str(type_num)
        else:
            v += " pre-" + type_
    else:
        v += " final"
    versions['verbose'] = v

    try:
        return versions[form]
    except KeyError:
        raise TypeError('"%s" is not a valid form specifier.' % form)

__version__ = get_version('short')
