[app]
title = Konfigaar
package.name = konfigaar
package.domain = org.konfigaar.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
android.archs = arm64-v8a
android.allow_backup = False
android.permissions = INTERNET
