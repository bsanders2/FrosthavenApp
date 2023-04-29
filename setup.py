from setuptools import setup

setup(
    # ...,
    entry_points={
        'console_scripts': [
            'play = GUI.GUI:play',
        ]
    }
)