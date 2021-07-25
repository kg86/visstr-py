import os
from IPython.display import HTML, display, Javascript

num_canvas = 0

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vis_str.umd.js")
lib_src = open(lib_path, "r").read()

display(Javascript(lib_src))


def visstr(s, ranges):
    global num_canvas
    html = f"""
    <script type="text/javascript" src="{lib_path}"></script>
    <canvas id="visstr_canvas_{num_canvas}" style="border: 1px solid #000000; background-color: white"></canvas>
    <script type="text/javascript">
    (function (){{
      const canvas = document.getElementById("visstr_canvas_{num_canvas}")
      const s = "{s}"
      const vstr = new visstr.VisStr(canvas)
      const range_groups = vstr.makeGroupRangesAutoColor({ranges}, "arrow")
      const ranges = range_groups
        .map((x) => vstr.nonOverlapRanges(x))
        .reduce((acm, x) => acm.concat(x), [])
      vstr.draw(s, ranges)
    }})()
    </script>
    """
    # print(html)
    # html = template.format(num_canvas, num_canvas, s, ranges)
    num_canvas += 1
    return HTML(html)
