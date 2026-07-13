import subprocess

def run(cmd):
    # Yeh background commands ko run karega aur return code check karega
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return result.returncode == 0

print("1. Adding notebook changes...")
# Jupyter notebook files ko track karega
run("git add *.ipynb")
# Script file ko bhi automatic track karega
run("git add push_streak.py")

print("2. Generating 10 commits to secure the dark green color tier...")
for i in range(1, 11):
    run(f'git commit --allow-empty -m "Python Practice Day - Part {i}/10"')

print("3. Syncing with GitHub...")
# GitHub ke standard 'main' branch par push karega
if run("git push origin main"):
    print("\n✅ Success! Your dark green color is locked in for today on MAIN branch!")
else:
    print("\n❌ Error: GitHub par push nahi ho paya. Ek baar internet check karein ya branch verify karein.")