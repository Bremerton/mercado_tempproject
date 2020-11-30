input.set_loud_sound_threshold(230)
def on_loud_sound():
    pass
    light.show_animation(light.comet_animation, 10000)
    light.clear()
input.on_loud_sound(on_loud_sound)
