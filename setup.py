from setuptools import setup
import os
from glob import glob
package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hikaru Nemoto',
    maintainer_email='s23C1105ZV@s.chibakoudai.jp',
    description='ロボットシステム学',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cpuutilization = mypkg.cpuutilization:main',
            'listener_test = mypkg.listener_test:main',
        ],
    },
)
