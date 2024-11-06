import glob
from pathlib import Path

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

library_name = "my_ops"

setup_dir = Path(__file__).resolve().parent
sources = [
    str(Path(source).relative_to(setup_dir))
    for source in glob.glob(f"{setup_dir}/csrc/*.cpp")
]

ext_modules = [
    CppExtension(
        f"{library_name}._C",
        sources,
    )
]

setup(
    name=library_name,
    packages=find_packages(),
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
)
