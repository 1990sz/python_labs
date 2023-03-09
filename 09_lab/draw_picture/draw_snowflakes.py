import simple_draw as sd

def snowflakes():
    N = 20
    len = [sd.random_number(10, 20) for _ in range(N)]
    x_coord = [i for i in range(100, 201, 5)]
    y_coord = [sd.random_number(25, 40) for _ in range(20)]
    for i in range(N):
        point = sd.get_point(x_coord[i], y_coord[i])
        sd.snowflake(point, length=len[i])