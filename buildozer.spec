[app]
title = MuscleAgent
package.name = muscleagent
package.domain = org.test
source.dir = .
source.include_exts = py,kv,png
version = 0.1
# On garde le strict minimum pour eviter les conflits
requirements = python3,kivy==2.3.0,requests
orientation = portrait
android.permissions = INTERNET,VIBRATE,WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
