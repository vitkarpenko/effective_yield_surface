from paraview import servermanager
from paraview.simple import *

reader = PVDReader(FileName=r"C:\Projects\effective_yield_surface\test.pvd")
data = servermanager.Fetch(reader)
point_data = data.GetPointData()
array = point_data.GetArray("Stress")
number_of_components = array.GetNumberOfComponents()
for i in range(number_of_components):
    print(i, array.GetComponentName(i))
print("max", max(array.GetComponent(i, 6) for i in range(array.GetNumberOfTuples())))
