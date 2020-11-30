input.setLoudSoundThreshold(230)
input.onLoudSound(function on_loud_sound() {
    
    light.showAnimation(light.cometAnimation, 10000)
    light.clear()
})
