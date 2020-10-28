def main():
    x, y = 100, 100
    width, height = 200, 200

    draw_house(x, y, width, height)


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
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


def draw_house_foundation(x, y, width, height):
    """
    Нарисовать основание домика ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x серидины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую основание', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    """
    Нарисовать основание домика ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x серидины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую стены', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    """
    Нарисовать крышу домика ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата x серидины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую крышу', x, y, width, height)
    pass


main()
