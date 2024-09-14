def get_distance_from_next_occurrence(current_index: int,
                                      current_color: int,
                                      colors: list[int]) -> int:
    hops = 0
    for index, color in enumerate(colors):
        if index < current_index:
            continue
        if color == current_color:
            return hops
        hops += 1
    return hops


def calculate(colors: list[int]) -> int:
    switches = 0

    first_brush = 0
    second_brush = 0

    for index, color in enumerate(colors):
        if first_brush == 0:
            first_brush = color
            switches += 1
            continue

        if first_brush == color:
            continue

        if second_brush == 0:
            second_brush = color
            switches += 1
            continue

        if second_brush == color:
            continue

        first_brush_distance = get_distance_from_next_occurrence(index, first_brush, colors)
        second_brush_distance = get_distance_from_next_occurrence(index, second_brush, colors)

        if first_brush_distance < second_brush_distance:
            second_brush = color
            switches += 1
        else:
            first_brush = color
            switches += 1

    return switches


def main():
    for _ in range(int(input())):
        unused = input()
        colors = []
        for color in input().split(' '):
            colors.append(int(color))
        print(calculate(colors))


if __name__ == '__main__':
    main()
