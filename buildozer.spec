[app]
# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Ensure this line is only specified once and includes all necessary dependencies.
requirements = python3,kivy,cython

# (list) Permissions required for your app (only for Android)
# Example: (list) permissions required for the app, such as access to the internet, etc.
# android.permissions = INTERNET

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) The path to the icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) The format used to package the app (e.g., apk, ipa, app)
package_format = apk

# (list) Additional files to include in the APK
# source.include_exts = png, jpg, kv, atlas

# (str) The default entry point for your application
# If left blank, Buildozer will assume 'main.py'
entrypoint = main.py

# (bool) Copy library dependencies into the apk or leave them in the system path
android.copy_libs = 1

# Other configurations as needed...
