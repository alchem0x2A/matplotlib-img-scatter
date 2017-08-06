import sys
if sys.version_info < (3, 0):
    import img_scatter
else:
    from . import img_scatter
