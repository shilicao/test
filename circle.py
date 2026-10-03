"""Print a circle in the terminal using text characters."""


def draw_circle(radius=10):
    """Draw a filled circle, compensating for tall terminal characters."""
    horizontal_scale = 2
    for y in range(-radius, radius + 1):
        row = []
        for x in range(-radius * horizontal_scale, radius * horizontal_scale + 1):
            distance_squared = (x / horizontal_scale) ** 2 + y**2
            row.append("*" if distance_squared <= radius**2 else " ")
        print("".join(row).rstrip())


if __name__ == "__main__":
    draw_circle()
