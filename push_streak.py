import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return result.returncode == 0

print("1. Adding notebook changes...")
run("git add *.ipynb")

# Agar script file khud push nahi hui hai, toh isko bhi sath me add kar lega
run("git add push_streak.py")

print("2. Generating 10 commits to secure the dark green color tier...")
for i in range(1, 11):
    run(f'git commit --allow-empty -m "Python Practice Day - Part {i}/10"')

print("3. Syncing with GitHub...")
# Pehle main branch try karega, agar fail hua toh master try karega
if run("git push origin main"):
    print("\n✅ Success! Your dark green color is locked in for today on MAIN branch!")
elif run("git push origin master"):
    print("\n✅ Success! Your dark green color is locked in for today on MASTER branch!")
else:
    print("\n❌ Error: GitHub par push nahi ho paya. Ek baar internet check karein ya repository link check karein.")