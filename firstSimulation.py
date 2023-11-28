import numpy as np

from VoxcraftVXA import VXA
from VoxcraftVXD import VXD

# Generate a Base VXA file
# See here for list of vxa tags: https://gpuvoxels.readthedocs.io/en/docs/
vxa = VXA(EnableExpansion=1, TempEnabled=1, VaryTempEnabled=1, TempPeriod=0.1, TempBase=25, TempAmplitude=20)
mat1 = vxa.add_material(RGBA=(0,255,0), E=1e9, RHO=1e3) # passive
mat2 = vxa.add_material(RGBA=(255,0,0), E=1e7, RHO=1e6, CTE=0.01) # active
vxa.write("data/base.vxa")

# Create random body array between 0 and maximum material ID
body = np.ones(shape=(3,3,3))

vxd = VXD()
vxd.set_tags(RecordVoxel=1)
vxd.set_data(body)
vxd.write("data/robot1.vxd")