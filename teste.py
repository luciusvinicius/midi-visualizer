def color_transition(current_color, destination_color, step):
    # Calculate the difference between each color component
    red_diff = destination_color[0] - current_color[0]
    green_diff = destination_color[1] - current_color[1]
    blue_diff = destination_color[2] - current_color[2]

    # Calculate the increment for each color component
    red_increment = red_diff / step
    green_increment = green_diff / step
    blue_increment = blue_diff / step

    # Calculate the intermediate color at the given step
    intermediate_color = (
        current_color[0] + red_increment * step,
        current_color[1] + green_increment * step,
        current_color[2] + blue_increment * step
    )

    return intermediate_color
