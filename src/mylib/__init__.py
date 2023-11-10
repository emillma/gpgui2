from pathlib import Path
from torch.utils.cpp_extension import load
import torch


thisdir = Path(__file__).parent
sources = list(thisdir.glob("*.cu"))
try:
    mylib = load(
        name="mylib", sources=sources, build_directory=thisdir / "build", verbose=True
    )
except Exception as e:
    print(e)
    raise e


def myfunc(tensor: torch.Tensor):
    return mylib.myfunc(tensor)
