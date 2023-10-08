#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare same data
X = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9,  10]

#prepre the output_file
output_file("03.Line.html")

#create line plot
f = figure()

#create line plot
f.line(X, y)

show(f)