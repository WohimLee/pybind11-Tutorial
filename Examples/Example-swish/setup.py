
import os.path as osp
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension


setup(
    name = "swishdddd",
    packages=["swish"], # 跟存放源代码的文件夹相同
    ext_modules=[
        CUDAExtension(
            name = "swish._C", # swish: 文件夹名, _C: 文件夹里面的库名
            sources =[
                "swish/swish.cu",
                "swish/ext.cpp"
            ],
            # gcc
            # nvcc -> gcc + cuda 语法
            extra_compile_args = {
                "nvcc": [
                    # "-I", osp.join(osp.join(osp.dirname(osp.abspath(__file__))))
                ], 
                "cxx" : [
                    
                ]
            }
        )
    ],
    cmdclass={
        "build_ext" : BuildExtension
    }
)