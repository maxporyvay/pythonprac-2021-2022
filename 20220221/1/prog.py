#!/home/maximporyvay/msu/myenv/bin/python3
# EASY-INSTALL-ENTRY-SCRIPT: 'ipsedixit==1.1.1','console_scripts','ipsedixit'
__requires__ = 'ipsedixit==1.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ipsedixit==1.1.1', 'console_scripts', 'ipsedixit')()
    )
