import os, sys

adb = r'C:\Users\sergi\Documents\Android\ADB\platform-tools'

os.chdir(adb)
os.system('cmd /c "adb connect 127.0.0.1:58526"')

for root, dirs, files in os.walk(adb):
    for app in files:
        if app.endswith('.apk'):
            print('Installing '+ app.removesuffix('.apk'))
            os.system('cmd /c "adb install '+ app)
            print(app.removesuffix('.apk') + ' installed')