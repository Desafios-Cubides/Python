EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes_actually):
    """
    Return the time remaining in minutes about the cooking of lasagna
    """
    return EXPECTED_BAKE_TIME - minutes_actually

def preparation_time_in_minutes(layers_lasagna):
    """
    Return the time in minutes the cooking the layers of the lasagna
    """
    return layers_lasagna * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


testing = elapsed_time_in_minutes(3, 20)
print(testing)