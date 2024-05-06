# from pkg_resources import get_distribution, DistributionNotFound

# try:
#     __version__ = get_distribution("atpdataset").version
# except DistributionNotFound:
#     # package is not installed
#     __version__ = None
#     pass

from importlib.metadata import version

from . import csv
from .dataset import AtpDataset

__version__ = version("atpdataset")
