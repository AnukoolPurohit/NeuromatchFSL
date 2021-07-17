from pathlib import Path


def filter_files(files, include=[], exclude=[], attr=None):
    if attr is None:
        fn = lambda x: str(x)
    else:
        fn = lambda x: getattr(x, attr)
    for incl in include:
        files = [file for file in files if incl in fn(file)]
    for excl in exclude:
        files = [file for file in files if excl not in fn(file)]
    return files


def ls(self, recurse=False, include=[], exclude=[], **kwargs):
    if recurse:
        files = list(self.glob("**/*"))
    else:
        files = list(self.iterdir())
    return filter_files(files, include, exclude, **kwargs)


Path.ls = ls
