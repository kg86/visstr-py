from __init__ import lib_url

import requests

res = requests.get(lib_url)
open("vis_str.umd.js", "wb").write(res.content)
