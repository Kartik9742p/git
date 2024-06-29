import numpy as np

class LineModel:
    def __init__(self):
        self.slope = 0
        self.bias = 0
        self.points = []

    def add_points(self, points):
        self.points.extend(points)

    def total_distance(self):
        total_distance = 0
        for x, y in self.points:
            distance = abs(self.slope * x - y + self.bias) / (self.slope ** 2 + 1) ** 0.5
            total_distance += distance
        return total_distance

    def line_equation(self):
        return f"y = {self.slope:.2f}x + {self.bias:.2f}"

class OptimizeLineModel(LineModel):
    def __init__(self, learning_rate, iterations):
        super().__init__()
        self.learning_rate = learning_rate
        self.iterations = iterations

    def OptimizeLine(self):
        for _ in range(self.iterations):
            slope_gradient = 0
            bias_gradient = 0

            for x, y in self.points:
                distance = abs(self.slope * x - y + self.bias)
                factor = (self.slope * x - y + self.bias) / (self.slope ** 2 + 1) ** 0.5
                slope_gradient += x * factor
                bias_gradient += factor

            self.slope -= self.learning_rate * slope_gradient / len(self.points)
            self.bias -= self.learning_rate * bias_gradient / len(self.points)

points = [(1,2), (4,8), (3,6), (8,16)]

model = OptimizeLineModel(learning_rate=0.5, iterations=10)
model.add_points(points)
model.OptimizeLine()

print(f'Total distance: {model.total_distance()}')
print(f'Line equation is: {model.line_equation()}')
