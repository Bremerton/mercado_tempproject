def on_loud_sound():
    pass
    music.ba_ding.play()
    light.show_animation(light.rainbowAnimation, 10000)
    music.ba_ding.stop()
input.on_loud_sound(on_loud_sound)
