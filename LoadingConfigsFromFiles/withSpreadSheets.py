
from jinja2 import FileSystemLoader, Environment
import os
# import xlrd  # module for working with SpreedSheets

#  SOURCE: https://subscription.packtpub.com/book/networking-and-servers/9781788998512/14/ch14lvl1sec77/generating-a-vmx-file-using-jinja2

__author__ = "naporium"
__EMAIL__ = "nm.10000.testes@gmail.com"

print("The script working directory is {}" .format(os.path.dirname(__file__)))
script_dir = os.path.dirname(__file__)

# ??????
vmx_env = Environment(
    loader=FileSystemLoader(script_dir),
    trim_blocks=True,
    lstrip_blocks=True
)