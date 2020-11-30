input.set_loud_sound_threshold(200)
def on_loud_sound():
    pass
    light.show_animation(light.rainbowAnimation, 10000)
input.on_loud_sound(on_loud_sound)
pause(10000)
light.stop_all_animations()
light.clear()