from pathlib import Path
import sys

sys.path.append(str((Path(__file__).parent.parent)).replace("\\", "/"))
import constants

__all__ = ("constants",)
