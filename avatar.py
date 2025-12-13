import turtle
turtle.speed (100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
turtle.bgcolor ('black')
turtle.width (1.5)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
color_i = 0
for i in range (360):
  turtle.color (colors [color_i % 6])
  turtle.forward (i)
  turtle.left (59)
  color_i += 1
turtle.mainloop ()
