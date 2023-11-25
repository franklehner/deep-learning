"""setup"""
from setuptools import setup, find_packages


setup(
    name="deeplearning",
    version="0.0.0",
    author="Frank Lehner",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "atari-py",
        "gym",
        "opencv-python",
        "tensorboard",
        "torch",
        "torchvision",
        "pytorch-ignite",
        "tensorboardX",
        "tensorflow",
        "ptan",
    ],
)
