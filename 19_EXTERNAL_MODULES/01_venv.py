# =========================
# Create Virtual Environment
# =========================

# python -m venv .venv
# or
# py -m venv .venv

# =========================
# Activate Virtual Environment
# =========================
#PS
# .\.venv\Scripts\Activate.ps1
# bash
# source .venv/Scripts/activate
# or
# . .venv/Scripts/activate

# =========================
# Install Packages
# =========================

pip install library_name

pip install library_name==version

pip install numpy==1.20.0

# =========================
# View Installed Packages
# =========================

pip list

# =========================
# Upgrade Package
# =========================

pip install --upgrade library_name

# =========================
# Uninstall Package
# =========================

pip uninstall library_name

# =========================
# Export Installed Packages
# =========================

pip freeze > requirements.txt

# =========================
# Install from requirements.txt
# =========================

pip install -r requirements.txt

# =========================
# Deactivate Virtual Environment
# =========================

deactivate
