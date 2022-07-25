from setuptools import setup
import os
from glob import glob

package_name = 'low_level'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), 
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Frank Fourlas',
    maintainer_email='frank.fourlas@gmail.com',
    description='Low level control processes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'buzzer = ' + package_name + '.buzzer:main',
            'motor = ' + package_name + '.motor:main',
        ],
    },
)
