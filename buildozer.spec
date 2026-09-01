[app]
title = Konfigaar
package.name = konfigaar
package.domain = com.konfigaar.app
source.dir =.
source.include_exts = py,png
version = 0.1
requirements = python3==3.10.13,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.archs = arm64-v8a, armeabi-v7a
