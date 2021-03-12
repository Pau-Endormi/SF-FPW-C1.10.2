class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def get_area(self):
    return self.width * self.height
  def __str__(self):
    return f"{self.__class__.__name__} ({self.width}, {self.height})"

