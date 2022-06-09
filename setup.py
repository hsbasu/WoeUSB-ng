import os

from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    data_files=[
        ("share/applications", ["miscellaneous/WoeUSB-ng.desktop"]),
        ("share/polkit-1/actions", ["miscellaneous/com.github.woeusb.woeusb-ng.policy"]),
        ("share/icons/hicolor/scalable/apps", ["src/WoeUSB/data/woeusb-logo.png"]),
    ],
    install_requires=[
        'termcolor',
        'wxPython',
    ]
)
