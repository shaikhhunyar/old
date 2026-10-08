print("Running... please hold...")

try:
    import requests
except ImportError:
    import os
    os.system("pip install requests")
    import requests

import shaikh