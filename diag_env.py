import sys
import os
print('executable:', sys.executable)
print('prefix:', sys.prefix)
print('path[0:5]:', sys.path[:5])
lib_dir = os.path.join(sys.prefix, 'Lib')
print('lib exists:', os.path.exists(lib_dir), lib_dir)
print('cgi exists:', os.path.exists(os.path.join(lib_dir, 'cgi.py')))
print('site-packages exists:', os.path.exists(os.path.join(sys.prefix, 'Lib', 'site-packages')))
print('setuptools exists:', os.path.exists(os.path.join(sys.prefix, 'Lib', 'site-packages', 'setuptools')))
