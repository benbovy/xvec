from importlib.metadata import PackageNotFoundError, version

from .index import GeoVectorIndex  # noqa
from .strtree import ShapelySTRTreeIndex  # noqa

try:
    __version__ = version("xvec")
except PackageNotFoundError:  # noqa
    # package is not installed
    pass
