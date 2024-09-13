[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain
package.domain = org.example

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported screen orientations
orientation = all

# (str) The filename of the entry point file
entrypoint = main.py

# (list) Permissions required by your app
android.permissions = INTERNET

# (list) Supported Android architecture
android.arch = arm64-v8a, armeabi-v7a

# (str) The application icon
icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1
