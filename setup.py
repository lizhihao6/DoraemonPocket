from setuptools import setup
from setuptools import find_packages

# change this.
NAME = "DoraemonPocket"
VERSION = "0.0.1"
AUTHOR = "lizhihao6"
EMAIL = "lizhihao6@outlook.com"
URL = "https://github.com/lizhihao6/DoraemonPocket"
LICENSE = "MIT License"
DESCRIPTION = "Python library of computational videography "

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=open("./README.md", "r").read(),
        long_description_content_type='text/markdown',
        # change package_name to your package name.
        entry_points={
            "console_scripts": [
                "package_name=DoraemonPocket.shell:run"
            ]
        },
        package_data={
            # change package_name to your package name.
            "DoraemonPocket": ["src/*.txt"]
        },
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6"
    )
