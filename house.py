def draw_house(x, y, width, height):
    """
    Нарисовать домик ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x серидины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print("Типа рисую домик...", x, y, width, height)
    pass  # do nothing


x, y = 100, 100
width, height = 200, 200

draw_house(x, y, width, height)
