[app]
title = Konfigaar
package.name = konfigaar
package.domain = org.konfigaar.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
