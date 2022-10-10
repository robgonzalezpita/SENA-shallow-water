import sys
sys.path.append("../../src/python")

from shallow_water_geometry_config import ShallowWaterGeometryConfig


test_default = ShallowWaterGeometryConfig()

print("Test __init__ method of ShallowWaterGeometryConfig class \n", test_default)

test_yamlpath = ShallowWaterGeometryConfig(yamlpath="../test_input/test_shallow_water_config.yml")

print("Test __call__ method of ShallowWaterGeometryConfig class \n", test_yamlpath)

test_args = ShallowWaterGeometryConfig(nx=5,ny=5,xmax=25,ymax=25)

print("Test __init__ method of ShallowWaterGeometryConfig class with nx, ny, xmax, ymax args")
print(test_args)
