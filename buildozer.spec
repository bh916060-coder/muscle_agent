[app]
title = MuscleAgent
package.name = muscleagent
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,urllib3,chardet,idna
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET,VIBRATE,FOREGROUND_SERVICE,WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_update = False
android.log_level = 2
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
