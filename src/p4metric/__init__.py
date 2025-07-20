from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('p4-metric')
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

from .core import p4_metric

__all__ = ["p4_metric", "__version__"]
