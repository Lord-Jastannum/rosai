import subprocess

scripts = [
    "src.generators.01_generate_countries",
    "src.generators.02_generate_currencies",
    "src.generators.03_generate_departments",
    "src.generators.04_generate_roles",
]

for script in scripts:
    print(f"\nRunning {script}")
    subprocess.run(["python", "-m", script], check=True)

print("\nAll generators completed.")