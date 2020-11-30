light.clear()
input.setLoudSoundThreshold(200)
input.onLoudSound(function on_loud_sound() {
    
    light.showAnimation(light.runningLightsAnimation, 10000)
    pause(10000)
    light.clear()
})
