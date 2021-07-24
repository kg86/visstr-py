import os
from IPython.display import HTML, display

num_canvas = 0

visstr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vis_str.umd.js")
# print("visstr_path", visstr_path)

vislib = "<script>{}</script>".format(open(visstr_path, "r").read())

display(HTML(vislib))


def visstr(s, ranges):
    template = """
    <canvas id="canvas_{}" style="border: 1px solid #000000; background-color: white"></canvas>
    <script>
    function main(){{
      const canvas = document.getElementById('canvas_{}')
      const s = '{}'
      const vstr = new visstr.VisStr(canvas)
      const range_groups = vstr.makeGroupRangesAutoColor({}, 'arrow')
      const ranges = range_groups
        .map((x) => vstr.nonOverlapRanges(x))
        .reduce((acm, x) => acm.concat(x), [])
      vstr.draw(s, ranges)
    }}
    main()
    </script>
    """
    global num_canvas
    html = template.format(num_canvas, num_canvas, s, ranges)
    num_canvas += 1
    # print(num_canvas)
    return HTML(html)
