from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'vision_rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'meshes'),glob('meshes/*')),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share',package_name,'worlds'),glob('worlds/*')),
        (os.path.join('share',package_name,'launch'),glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='max',
    maintainer_email='maxino4646@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'publisher_node = vision_rpi_bot.publisher:main',
                'subsriber_node = vision_rpi_bot.subscriber:main',
                'qr_maze_solving_node = vision_rpi_bot.qr_maze_drive:main',
        ],
},
)
