import graphics as gr

window = gr.GraphWin('house', 600, 600)

def draw_sun():
    sun = gr.Circle(gr.Point(500, 100), 50)
    sun.setFill('yellow')
    sun.draw(window)

def draw_background():
    horizont = gr.Line(gr.Point(0,300), gr.Point(600, 300))
    grass = gr.Rectangle(gr.Point(0, 600), gr.Point(600, 300))
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(600, 300))

    grass.setFill('chartreuse') 
    sky.setFill('blue')

    sky.draw(window)
    horizont.draw(window)
    grass.draw(window)

def draw_house():
    house = gr.Rectangle(gr.Point(100, 450), gr.Point(300, 250))
    glass = gr.Rectangle(gr.Point(150,400), gr.Point(250, 300))
    roof = gr.Polygon(gr.Point(100, 250), gr.Point(300, 250), gr.Point(200, 180))


    house.setFill('grey')
    glass.setFill('yellow')
    roof.setFill('brown')

    house.draw(window)
    glass.draw(window)
    roof.draw(window)

def draw_window():    
    line1 = gr.Line(gr.Point(150,350), gr.Point(250, 350))
    line2 = gr.Line(gr.Point(150,300), gr.Point(250, 300))
    line3 = gr.Line(gr.Point(150,400), gr.Point(250, 400))
    line4 = gr.Line(gr.Point(150,300), gr.Point(150, 400))
    line5 = gr.Line(gr.Point(200,300), gr.Point(200, 400))
    line6 = gr.Line(gr.Point(250,300), gr.Point(250, 400))
    
    line1.setWidth(4)
    line2.setWidth(4)
    line3.setWidth(4)
    line4.setWidth(4)
    line5.setWidth(4)
    line6.setWidth(4)

    line1.draw(window)
    line2.draw(window)
    line3.draw(window)
    line4.draw(window)
    line5.draw(window)
    line6.draw(window)

def draw_clouds():
    cloud1 = gr.Circle(gr.Point(70, 70), 25)
    cloud2 = gr.Circle(gr.Point(90, 70), 25)
    cloud3 = gr.Circle(gr.Point(110, 70), 25)
    cloud4 = gr.Circle(gr.Point(80, 60), 25)
    cloud5 = gr.Circle(gr.Point(100, 60), 25)

    cloud1.setFill('White')
    cloud2.setFill('White')
    cloud3.setFill('White')
    cloud4.setFill('White')
    cloud5.setFill('White')

    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)

def draw_tree():
    tree1 = gr.Polygon(gr.Point(350, 450), gr.Point(550, 450), gr.Point(450, 380))
    tree2 = gr.Polygon(gr.Point(350, 390), gr.Point(550, 390), gr.Point(450, 320))
    tree3 = gr.Polygon(gr.Point(350, 330), gr.Point(550, 330), gr.Point(450, 260))
    stick = gr.Rectangle(gr.Point(440, 510), gr.Point(460 ,450))
    
    tree1.setWidth(4)
    tree2.setWidth(4)
    tree3.setWidth(4)
    stick.setWidth(3)

    tree1.setFill('green')
    tree2.setFill('green')
    tree3.setFill('green')
    stick.setFill('brown')

    tree1.setOutline('black')
    tree2.setOutline('black')
    tree3.setOutline('black')
    stick.setOutline('black')

    tree1.draw(window)
    tree2.draw(window)
    tree3.draw(window)
    stick.draw(window)



def draw_picture():
    draw_background()
    draw_sun()
    draw_house()
    draw_window()
    draw_clouds()
    draw_tree()

draw_picture()    
    
