input.setLoudSoundThreshold(200)
input.onLoudSound(function on_loud_sound() {
    
    light.showAnimation(light.rainbowAnimation, 10000)
})
pause(10000)
light.stopAllAnimations()
light.clear()
