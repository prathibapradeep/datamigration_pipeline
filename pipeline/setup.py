
from setuptools import setup

setup(
    name='datamigration_pipeline',
    version='0.1',
    install_requires=[
        'apache-beam[gcp]',
        'google-cloud-bigquery',
    ],
    packages=['.'],
)
