# import graphics
# win=graphics.GraphWin();
# cper=int(input("tangs: "))
from graphics import *
win=GraphWin("存款计算器",320,400);
win.setBackground("white")
Text(Point(20, 230), ' 0.0K').draw(win)
Text(Point(20, 180), ' 2.5K').draw(win)
Text(Point(20, 130), ' 5.0K').draw(win)
Text(Point(20, 80), ' 7.5K').draw(win)
Text(Point(20, 30), '10.0K').draw(win)
principal = float(input("Enter the initial principal: "))
apr = float(input("Enter the annualized interest rate: "))
height = principal * 0.02
bar = Rectangle(Point(40, 230), Point(65, 230-height))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)
# Draw bars for successive years
for year in range(1,11):
# calculate value for the next year
   principal = principal * (1 + apr)
# draw bar for this value
xll = year * 25 + 40
height = principal * 0.02
bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)
input("Please input Enter to quit")










