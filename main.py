import os, sys

adb = r'Your ADB drivers'

os.chdir(adb)
os.system('cmd /c "adb connect 127.0.0.1:58526"')

for root, dirs, files in os.walk(adb):
    for app in files:
        if app.endswith('.apk'):
            print('Installing '+ app.removesuffix('.apk'))
            os.system('cmd /c "adb install '+ app)
            print(app.removesuffix('.apk') + ' installed')
            print('Do you want to remove ' + app + '?')
            respuesta = input()
            if respuesta == 'yes' or respuesta == 'y' or respuesta == 'Yes' or respuesta == 'Y':
                os.remove(app)
                print(app + ' was removed.')
                print('############')
            else:
                print('############')
