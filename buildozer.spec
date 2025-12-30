[app]

# (str) Title of your application
title = System Diagnostic

# (str) Package name
package.name = sysdiag

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# MODIFICATION : Ajout de pycryptodome pour le chiffrement
requirements = python3,kivy,requests,pycryptodome

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# MODIFICATION : Suppression du '#' et activation des accès Micro/Internet/Stockage
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API
android.ndk_api = 21

# (list) The Android archs to build for
# MODIFICATION : Activation des architectures 64 bits et 32 bits
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

#
# Python for android (p4a) specific
#

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

#
# iOS specific
#

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1