[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (unique identifier)
package.domain = org.example

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# Ensure this is a single, unique line
requirements = python3,kivy

# (str) Supported screen orientations
orientation = all

# (bool) Whether to include the source code in the final APK
source.include_exts = py,png,jpg,kv,atlas

# (str) The filename of the entry point file
entrypoint = main.py

# (list) Permissions required by your app
android.permissions = INTERNET

# (list) Supported Android architecture
android.arch = arm64-v8a, armeabi-v7a

# (list) The list of java .jar files to add to the libs dir
#android.add_jars = foo.jar,bar.jar,baz.jar

# (list) The list of Java classes to add to the activity options
#android.activity_class = org.kivy.android.PythonActivity

# (str) The application icon
icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Display the banner in the application
#android.debug = 1
