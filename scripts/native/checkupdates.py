import os
from box64droid import ver
print("Checking for Box64Droid updates...")
ver2=104243
if ver != ver2:
    print("New update available! Updating scripts...")
    os.system("wget https://cdn.gitmirror.com/gh/Ilya114/Box64Droid/main/scripts/native/box64droid.py &>/dev/null")
    os.system("wget https://cdn.gitmirror.com/gh/Ilya114/Box64Droid/main/scripts/native/start-box64.py &>/dev/null")
    os.system("mv box64droid.py start-box64.py $PREFIX/bin/")
    print("Updating glibc-prefix...")
    os.system("wget -q --show-progress https://github.com/Ilya114/Box64Droid/releases/download/alpha/glibc-prefix.tar.xz")
    os.system("tar -xJf glibc-prefix.tar.xz -C $PREFIX/")
    os.system("rm glibc-prefix.tar.xz")
    print("Update done!")
    print("Changes (01.04.24):")
    print("- Updated Box64")
    print("- Updated Turnip (64 bit)")
    print('- Now config folder named "Box64Droid (native)" (@Th_Fvck asked)')
else:
    print("Updates not found")
os.system("sleep 2")
os.system("rm $PREFIX/bin/checkupdates.py")
os.system("python3 $PREFIX/bin/box64droid.py --start")
exit()
