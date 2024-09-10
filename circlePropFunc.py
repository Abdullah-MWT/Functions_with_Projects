# ++++++++ Function that tells the circumference and Area of a Circle by giving just radius of a Circle ++++++++

import math
def circle_Prop(radius):
    # Circumference
    circumference = 2 * math.pi * radius

    # Area
    area = math.pi * radius ** 2
    print(f'Circumference of a circle is {round(circumference, 2)} and Area of a Circle is {round(area,2)}')

circle_Prop(3.4)