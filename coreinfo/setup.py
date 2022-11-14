from setuptools import setup

setup(name="Twitter Aggregate Generator",
        version="1.0.2",
        description="A program to collect and aggregate large amounts of twitter data via the Twitter API.",
        author="Branden Kunkel",
        author_email="kunkel.branden6130@gmail.com",
        maintainer="Branden Kunkel",
        maintainer_email="kunkel.branden6130@gmail.com",
        url="https://github.com/Branden-Kunkel/twitter_aggregate_generator",
        python_requires="==3.8.10",
        install_requires=["requests == 2.28.1"],
)