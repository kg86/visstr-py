import os
import uuid
from IPython.display import HTML, display, Javascript

lib_local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vis_str.umd.js")
lib_url = "https://unpkg.com/visstr@0.0.5/lib/vis_str.umd.js"
lib_tag = f'<script type="text/javascript" src="{lib_url}"></script>'

try:
    import google.colab

    IN_COLAB = True
except:
    IN_COLAB = False

# Each cell in google colaboratory is hosted by iframe,
# but one in Jupyter is not.
# Due to this difference, we read visstr JS library in
# a different way for each environment.
# If the library is called in google colaboratory,
# we insert script tag to read the library into each cell.
# If the library is called in Jupyter,
# we insert script tag only once when the library is imported,
# and the code is shared to all cells.

if not IN_COLAB:
    display(Javascript(open(lib_local, "r").read()))


def Str(s, ranges, font_size=32, width=None, height=None):
    img_style_dic = dict()
    if width:
        img_style_dic["width"] = f"{width}px"
    if height:
        img_style_dic["height"] = f"{height}px"
    img_style = "; ".join([f"{k}: {v}" for k, v in img_style_dic.items()])

    canvas_id = uuid.uuid4()
    img_id = uuid.uuid4()
    html = lib_tag if IN_COLAB else ""

    html += f"""
    <canvas id="{canvas_id}" style="display:none; border: 1px solid #000000; background-color: white"></canvas>
    <img id="{img_id}" style="{img_style}"/>
    <script type="text/javascript">
    (function (){{
      const canvas = document.getElementById("{canvas_id}")
      const s = "{s}"
      const vstr = new visstr.VisStr(canvas, {font_size})
      const range_groups = vstr.makeGroupRangesAutoColor({ranges}, "arrow")
      const ranges = range_groups
        .map((x) => vstr.nonOverlapRanges(x))
        .reduce((acm, x) => acm.concat(x), [])
      vstr.draw(s, ranges)
      const img = document.getElementById("{img_id}")
      img.src = canvas.toDataURL("image/png")

    }})()
    </script>
    """
    return HTML(html)
