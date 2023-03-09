import simple_draw as sd
sd.resolution = (1200, 600)

def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step = 5
    for color in rainbow_colors:
        sd.line(sd.get_point(1000, 635 - step), sd.get_point(1200, 400 - step), color=color, width=5)
        step += 5