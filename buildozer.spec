[app]
# (str) Title of your application
title = 电表助手

# (str) Package name
package.name = dianbiaoapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.walxk

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,xlsx,ico

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) The Python interpreter to use for the app (default: python3)
python.command = python3

# (str) The Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid unnecessary Internet downloads when building
android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
entry_point = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entry_point to set custom Java class instead of PythonActivity
#android.appactivity = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the AndroidManifest.xml file
#extra_manifests = 

# (str) Extra xml to write directly inside the AndroidManifest.xml (additions to the root element)
#extra_manifest_xml = ./AndroidManifest.xml

# (str) Android background services to start (comma separated)
#android.services = 

# (str) Android additional libraries to link against (comma separated)
#android.add_libs_armeabi = 
#android.add_libs_armeabi_v7a = 
#android.add_libs_arm64_v8a = 
#android.add_libs_x86 = 
#android.add_libs_mips = 

# (str) Android additional jars to link against (comma separated)
#android.add_jars = 

# (str) Android additional aars to link against (comma separated)
#android.add_aars = 

# (str) Put files in the assets directory (relative to the app source)
#android.add_assets = 

# (str) Put files in the resources directory (relative to the app source)
#android.add_resources = 

# (str) Logcat filters to apply when running the app on device (comma separated)
#android.logcat_filters = 

# (bool) Enable Android auto backup feature (requires Android 4.0+)
#android.allow_backup = True

# (str) Override the default Android manifest XML file
#android.manifest_template = 

# (str) Android activity launch mode (standard, singleTop, singleTask, singleInstance)
#android.launch_mode = standard

# (str) Android window layout mode (behind, system, local)
#android.window_layout = 

# (str) Android window soft input mode (resize, pan, nothing)
#android.window_soft_input = 

# (str) Android theme to apply to the activity
#android.theme = 

# (str) Android icon (default: icon.png)
#icon.filename = %(source.dir)s/icon.ico

# (str) Presplash image (default: presplash.jpg)
#presplash.filename = 

# (str) Splash screen image (default: splash.png)
#splash.filename = 

# (str) Splash screen color (default: #000000)
#splash.color = #000000

# (str) Splash screen scale (center, scale, fit)
#splash.scale = 

# (str) Splash screen aspect ratio (default: keep)
#splash.aspect = 

# (str) Splash screen gravity (top, bottom, left, right, center, fill)
#splash.gravity = 

# (str) Splash screen repeat (repeat, no-repeat)
#splash.repeat = 

# (str) Splash screen duration (in milliseconds)
#splash.duration = 

# (str) Android keystore name (default: debug.keystore)
#android.keystore = 

# (str) Android keystore alias (default: androiddebugkey)
#android.keystore_alias = 

# (str) Android keystore password (default: android)
#android.keystore_password = 

# (str) Android keystore key password (default: android)
#android.keyalias_password = 

# (str) Android signing configuration (debug, release)
#android.signing = debug

# (str) Android gradle build tools version
#android.gradle_build_tools_version = 

# (str) Android gradle plugin version
#android.gradle_plugin_version = 

# (str) Android gradle wrapper version
#android.gradle_wrapper_version = 

# (str) Android gradle distribution url
#android.gradle_distribution_url = 

# (str) Android gradle distribution sha256 sum
#android.gradle_distribution_sha256_sum = 

# (str) Android gradle distribution type (bin, src)
#android.gradle_distribution_type = bin

# (str) Android gradle distribution base url
#android.gradle_distribution_base_url = 

# (str) Android gradle distribution archive name
#android.gradle_distribution_archive_name = 

# (str) Android gradle distribution archive extension
#android.gradle_distribution_archive_extension = zip

# (str) Android gradle distribution archive path
#android.gradle_distribution_archive_path = 

# (str) Android gradle distribution archive checksum
#android.gradle_distribution_archive_checksum = 

# (str) Android gradle distribution archive checksum algorithm
#android.gradle_distribution_archive_checksum_algorithm = sha256

# (str) Android gradle distribution archive checksum file
#android.gradle_distribution_archive_checksum_file = 

# (str) Android gradle distribution archive checksum file url
#android.gradle_distribution_archive_checksum_file_url = 

# (str) Android gradle distribution archive checksum file extension
#android.gradle_distribution_archive_checksum_file_extension = 

# (str) Android gradle distribution archive checksum file path
#android.gradle_distribution_archive_checksum_file_path = 

# (str) Android gradle distribution archive checksum file algorithm
#android.gradle_distribution_archive_checksum_file_algorithm = 

# (str) Android gradle distribution archive checksum file content
#android.gradle_distribution_archive_checksum_file_content = 

# (str) Android gradle distribution archive checksum file content url
#android.gradle_distribution_archive_checksum_file_content_url = 

# (str) Android gradle distribution archive checksum file content extension
#android.gradle_distribution_archive_checksum_file_content_extension = 

# (str) Android gradle distribution archive checksum file content path
#android.gradle_distribution_archive_checksum_file_content_path = 

# (str) Android gradle distribution archive checksum file content algorithm
#android.gradle_distribution_archive_checksum_file_content_algorithm = 

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa, etc) storage, absolute or relative to spec file
bin_dir = ./bin