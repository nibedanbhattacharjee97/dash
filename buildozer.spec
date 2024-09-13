[app]
# (list of other options)
title = MyApp
package.name = myapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*
source.exclude_exts = spec
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.arch = armeabi-v7a
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.sdk = 31
android.gradle_dependencies = com.google.android.material:material:1.4.0
android.add_aapt2 = True
android.entrypoint = main:main
android.additional_java_dirs = src

[buildozer]
# (list of other options)
log_level = 2

[deploy]
# (list of other options)
target = android

[python]
# (list of other options)
# Uncomment to add Python path
# path = /path/to/python

[global]
# (list of other options)
# Uncomment to specify the location of the SDK and NDK
# sdk_dir = /path/to/sdk
# ndk_dir = /path/to/ndk

[log]
# (list of other options)
# Uncomment to specify log level
# level = 2

[requirements]
# (list of other options)
# Uncomment to specify additional requirements
# extra_requirements = sqlite3, pandas

[package]
# (list of other options)
# Uncomment to specify additional package options
# packages = mypackage
