from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
transform = new_matrix()
edges = []

parse_file( 'script', edges, transform, screen, color )



# image 2: soup cans
'''clear_screen(screen)
ident(transform)
red = []
white = []
lid = []
circle = []
R = 40
h = 150
t = 1
r = 20

for i in range(360 // t):
    add_edge(lid, -R, -R, h // 2, R, R, h // 2)
    add_edge(red, R, R, 0, R, R, h // 2)
    add_edge(white, R, R, -h // 2, R, R, 0)
    add_edge(circle, 0, 0, -r, 0, 0, r)
    matrix_mult(make_rotZ(t), red)
    matrix_mult(make_rotZ(t), white)
    matrix_mult(make_rotZ(t), lid)
    matrix_mult(make_rotY(t), circle)

matrix_mult(make_rotX(-70), transform)
matrix_mult(make_translate(100,150,0), transform)
matrix_mult(make_translate(0,-45,0), circle)
matrix_mult(transform, circle)
matrix_mult(transform, red)
matrix_mult(transform, lid)
matrix_mult(transform, white)
draw_lines(white, screen, [255,255,255])
draw_lines(red, screen, [255,0,0])
draw_lines(lid, screen, [190,190,190])
draw_lines(circle, screen, [255,215,0])

ident(transform)
matrix_mult(make_translate(150,0,0), transform)
matrix_mult(transform, circle)
matrix_mult(transform, red)
matrix_mult(transform, lid)
matrix_mult(transform, white)
draw_lines(white, screen, [255,255,255])
draw_lines(red, screen, [255,0,0])
draw_lines(lid, screen, [190,190,190])
draw_lines(circle, screen, [255,215,0])

ident(transform)
matrix_mult(make_translate(150,0,0), transform)
matrix_mult(transform, circle)
matrix_mult(transform, red)
matrix_mult(transform, lid)
matrix_mult(transform, white)
draw_lines(white, screen, [255,255,255])
draw_lines(red, screen, [255,0,0])
draw_lines(lid, screen, [190,190,190])
draw_lines(circle, screen, [255,215,0])

ident(transform)
matrix_mult(make_translate(0,210,0), transform)
matrix_mult(transform, circle)
matrix_mult(transform, red)
matrix_mult(transform, lid)
matrix_mult(transform, white)
draw_lines(white, screen, [255,255,255])
draw_lines(red, screen, [255,0,0])
draw_lines(lid, screen, [190,190,190])
draw_lines(circle, screen, [255,215,0])

ident(transform)
matrix_mult(make_translate(-150,0,0), transform)
matrix_mult(transform, circle)
matrix_mult(transform, red)
matrix_mult(transform, lid)
matrix_mult(transform, white)
draw_lines(white, screen, [255,255,255])
draw_lines(red, screen, [255,0,0])
draw_lines(lid, screen, [190,190,190])
draw_lines(circle, screen, [255,215,0])

ident(transform)
matrix_mult(make_translate(-150,0,0), transform)
matrix_mult(transform, circle)
matrix_mult(transform, red)
matrix_mult(transform, lid)
matrix_mult(transform, white)
draw_lines(white, screen, [255,255,255])
draw_lines(red, screen, [255,0,0])
draw_lines(lid, screen, [190,190,190])
draw_lines(circle, screen, [255,215,0])

save_extension(screen, 'pic1.png')
display(screen)'''