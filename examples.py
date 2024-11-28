import glob as glob
import os as os


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        #typically top of the file, doing it this way can increase speed though
        import math

        return math.pi * self.radius * self.radius

#-----------------------------------------
#running code
#-----------------------------------------
my_circle = Circle(10)
my_rectangle = Rectangle(5,3)

my_shapes = [my_circle, my_rectangle]
#get_area() exists in both classes and can both be called. Is polymorphism
total_area = sum(shape.get_area() for shape in my_shapes)
#-----------------------------------------
class JSONDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        from inflammation import models

        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))

        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data_loc = map(models.load_csv, data_file_paths)
        return list(data_loc)

#-----------------------------------------
#running code
#-----------------------------------------
"""
_, extension = os.path.splitext(infiles[0])
if extension == '.json':
  data_source = JSONDataSource(os.path.dirname(infiles[0]))
elif extension == '.csv':
  data_source = CSVDataSource(os.path.dirname(infiles[0]))
else:
  raise ValueError(f'Unsupported data file format: {extension}')
analyse_data(data_source)
"""
#-----------------------------------------