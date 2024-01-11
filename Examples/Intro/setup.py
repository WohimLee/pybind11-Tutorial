
import os
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension


setup(
    name = "swish",
    packages=["swish"],
    ext_modules=[
        CUDAExtension(
            name = "swish.swish_c",
            sources =[
                
            ],
            extra_compile_args = {"nvcc": ["-I", ]}
        )
    ],
    cmdclass={
        "build_ext" : BuildExtension
    }
)