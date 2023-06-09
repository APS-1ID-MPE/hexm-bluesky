"""
Load devices and plans for bluesky queueserver.

How to start the queueserver process:
See file ``./run_qstarter_py.sh```
"""

import pathlib
import sys

sys.path.append(
    str(pathlib.Path(__file__).absolute().parent)
)

from instrument import iconfig
from instrument.queueserver import *


print_instrument_configuration()
print_devices_and_signals()
print_plans()
print_RE_metadata()
