# Copyright (c) Meta Platforms, Inc. and affiliates. All Rights Reserved.

from setuptools import setup, find_packages
from torch.utils.cpp_extension import CUDAExtension
from torch.utils import cpp_extension

setup(
    name="dpf_cpp",
    packages=find_packages(include=["dpf_gpu"]),
    ext_modules=[
        CUDAExtension(
            "dpf_cpp",
            sources=[
                "dpf_wrapper.cu",
            ],
            extra_compile_args=["-std=c++17"],
        )
    ],
    cmdclass={"build_ext": cpp_extension.BuildExtension},
)
