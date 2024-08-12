import arcade
import math  # Importa el módulo math de Python
from bresenham import get_line, get_circle

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dibujo de una Casa"

# Función para dibujar un rectángulo usando get_line
def draw_rectangle(x, y, width, height, color):
    bottom_line = get_line(x, y, x + width, y)
    top_line = get_line(x, y + height, x + width, y + height)
    left_line = get_line(x, y, x, y + height)
    right_line = get_line(x + width, y, x + width, y + height)
    for point in bottom_line + top_line + left_line + right_line:
        arcade.draw_point(point[0], point[1], color, 2)

# Función para dibujar un triángulo usando get_line
def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    line1 = get_line(x1, y1, x2, y2)
    line2 = get_line(x2, y2, x3, y3)
    line3 = get_line(x3, y3, x1, y1)
    for point in line1 + line2 + line3:
        arcade.draw_point(point[0], point[1], color, 2)

# Función para dibujar un círculo usando get_circle
def draw_circle(xc, yc, r, color):
    points = get_circle(xc, yc, r)
    for point in points:
        arcade.draw_point(point[0], point[1], color, 2)

# Función para dibujar un pentágono usando get_line
def draw_pentagon(x, y, size, color):
    angle = 72  # Ángulo de separación entre cada vértice (360° / 5 lados)
    points = []
    for i in range(5):
        x1 = x + size * math.cos(math.radians(i * angle))
        y1 = y + size * math.sin(math.radians(i * angle))
        x2 = x + size * math.cos(math.radians((i + 1) * angle))
        y2 = y + size * math.sin(math.radians((i + 1) * angle))
        points += get_line(int(x1), int(y1), int(x2), int(y2))
    for point in points:
        arcade.draw_point(point[0], point[1], color, 2)

class HouseWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Coordenadas y dimensiones del cuerpo de la casa (rectángulo)
        house_x = 200
        house_y = 100
        house_width = 300
        house_height = 200
        draw_rectangle(house_x, house_y, house_width, house_height, arcade.color.BROWN)

        # Coordenadas del techo (triángulo)
        roof_x1, roof_y1 = house_x - 50, house_y + house_height
        roof_x2, roof_y2 = house_x + house_width + 50, house_y + house_height
        roof_x3, roof_y3 = house_x + house_width // 2, house_y + house_height + 150
        draw_triangle(roof_x1, roof_y1, roof_x2, roof_y2, roof_x3, roof_y3, arcade.color.DARK_RED)

        # Coordenadas y tamaño de la ventana (círculo)
        window_xc, window_yc = house_x + house_width // 2, house_y + house_height // 2
        window_radius = 30
        draw_circle(window_xc, window_yc, window_radius, arcade.color.LIGHT_BLUE)

        # Coordenadas y tamaño de la ventana (pentágono)
        pentagon_x, pentagon_y = house_x + house_width // 4, house_y + house_height // 2
        pentagon_size = 30
        draw_pentagon(pentagon_x, pentagon_y, pentagon_size, arcade.color.YELLOW)

if __name__ == "__main__":
    window = HouseWindow()
    arcade.run()
