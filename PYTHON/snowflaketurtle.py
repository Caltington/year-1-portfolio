import turtle

window = turtle.Screen()
window.bgcolor("sky blue")

tree = turtle.Turtle()
tree.color("forest green")

def make_tree_segment(size, top_position):
    tree.begin_fill()
    tree.setposition(0, top_position)
    tree.setposition(size, top_position - size)
    tree.setposition(-size, top_position - size)
    tree.setposition(0, top_position)
    tree.end_fill()

tree_segments = ((50, 20), (80, 0), (120, -30), (150, -60))
for size, top_position in tree_segments:
    make_tree_segment(size, top_position)
    
tree_segments = ((50, 20), (80, 0), (120, -30), (150, -60))

tree.setposition(0,-210)
tree.color("brown")
tree.begin_fill()
tree.forward(25)
tree.right(90)
tree.forward(150)
tree.right(90)
tree.forward(50)
tree.right(90)
tree.forward(150)
tree.end_fill()



turtle.done()
