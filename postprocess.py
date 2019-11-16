from paraview.simple import *
from paraview import servermanager


reader = PVDReader(FileName=r"C:\Projects\effective_yield_surface\test.pvd")
for a in reader.PointData:
    print(a.GetName())