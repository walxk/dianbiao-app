[app]
title = DianBiao App
package.name = dianbiao
package.domain = org.walxk

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,xlsx

version = 0.1
requirements = python3,kivy==2.3.0,requests,openpyxl

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0

fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1