light.clear()
input.set_loud_sound_threshold(200)
def on_loud_sound():
    pass
    light.show_animation(light.running_lights_animation, 10000)
    pause(10000)
    light.clear()
input.on_loud_sound(on_loud_sound)
