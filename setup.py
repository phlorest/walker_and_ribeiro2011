from setuptools import setup


setup(
    name='cldfbench_walker_and_ribeiro2011',
    py_modules=['cldfbench_walker_and_ribeiro2011'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'walker_and_ribeiro2011=cldfbench_walker_and_ribeiro2011:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
