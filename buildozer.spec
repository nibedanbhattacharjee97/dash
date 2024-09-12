[app]
# (str) Title of your application
title = DashboardApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed to get a reverse domain to use as a package)
package.domain = org.example

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (e.g., 1.0.0)
version = 1.0.0

# (list) Application requirements
# Add any libraries your app needs here, including Kivy, Pandas, and SQLite
requirements = python3,kivy,pandas,sqlite3

# (str) The entry point of your application
# This is typically the main file of your app
entrypoint = main.py

# (list) Permissions required by your application
# Include permissions if your app needs access to storage, internet, etc.
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Android API level to target
# You can specify the API level; default is usually fine for most cases
android.api = 30

# (int) Minimum API level required (default: 21)
# Change this if you need to support older devices
android.minapi = 21

# (str) Android NDK version to use
# This usually doesn't need to be changed from the default
android.ndk = 23b

# (bool) Enable or disable the inclusion of the compiled Python interpreter
# Keep as default unless you have a specific reason to change it
android.include_sqlite3 = true

# (str) Directory to store the compiled APK
# Specify a custom build directory if needed
build_dir = build

# (str) Icon of your application
# Replace with your app's icon if available
icon.filename = icon.png

# (str) Android architecture to target (default is armeabi-v7a)
# Specify additional architectures if needed
android.arch = armeabi-v7a

# (list) Additional files to include in your application package
# Add any additional files or directories your app needs
source.include_patterns = assets/*

# (list) Java classes to include in your APK
# Not needed unless you have custom Java code
android.add_src =

# (str) Presplash screen (before app starts)
# Replace with your app's presplash screen if available
presplash.filename = presplash.png

# (list) Dependencies required for your application (e.g., pip libraries)
# Buildozer will attempt to install these using pip
requirements = kivy, sqlite3, pandas

# (bool) Whether to use the SDL2 Java Bootstrapper
# This is generally the recommended choice
android.bootstrap = sdl2

# (str) Additional environment variables
# Set additional environment variables if needed for your app
environment =

# (bool) If True, run the logcat viewer on application start
# Useful for debugging; disable if not needed
log_level = 2

# (bool) If True, automatically run the application after building
# Useful for quick testing during development
android.auto_start = true

# (str) Orientation of your application
# Choose from 'landscape', 'portrait', 'sensor', 'all'
orientation = portrait

# (str) Screen DPI to use
# 'all' supports all DPI levels, but you can specify specific ones if needed
android.dpi = all

# (bool) Enable hardware acceleration
# Keep enabled unless there are specific reasons to disable it
android.hardware_accelerated = true
