import numpy as np
import fatiando as ft

shape = (41, 41)
x, y = ft.grd.regular((-10, 10, 30, 50), shape)
height = 800 - 1000*ft.utils.gaussian2d(x, y, 3, 1, x0=0, y0=37)
rel = -7000*ft.utils.gaussian2d(x, y, 3, 5, x0=0, y0=40)
thick = height - rel
dens = 1900*np.ones_like(thick)
data = np.transpose([x, y, height, thick, dens])
with open('layers.txt', 'w') as f:
    f.write("# Synthetic layer model of sediments and topography\n")
    f.write("# Columns are:\n")
    f.write("#   lon   lat   height   thickness   density\n")
    np.savetxt(f, data, fmt='%g')
ft.vis.figure(figsize=(4, 3))
ft.vis.title('Depth of sediments [m]')
ft.vis.axis('scaled')
ft.vis.pcolor(x, y, rel, shape)
ft.vis.colorbar()
ft.vis.savefig('depth.png')
ft.vis.figure(figsize=(4, 3))
ft.vis.title('Topography [m]')
ft.vis.axis('scaled')
ft.vis.pcolor(x, y, height, shape)
ft.vis.colorbar()
ft.vis.savefig('topography.png')
ft.vis.figure(figsize=(4, 3))
ft.vis.title('Thickness of sediment layer [m]')
ft.vis.axis('scaled')
ft.vis.pcolor(x, y, thick, shape)
ft.vis.colorbar()
ft.vis.savefig('thickness.png')
ft.vis.show()