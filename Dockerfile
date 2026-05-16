# ─── STAGE: Base image ───────────────────────────────────────────
# FROM tells Docker: "start from this base image"
# python:3.11-slim = Python 3.11 on minimal Linux (smaller size)
# Think of it like: your app needs a phone to run on.
# This is the phone's operating system.
FROM python:3.11-slim

# ─── Set working directory ────────────────────────────────────────
# All commands after this run inside /app inside the container
# Like: cd /app (but inside the container's file system)
WORKDIR /app

# ─── Copy dependencies file FIRST ─────────────────────────────────
# Why copy requirements.txt before the rest of the code?
# Docker caches each step. If your code changes but requirements.txt
# doesn't, Docker reuses the cached pip install step → faster builds.
COPY requirements.txt .

# ─── Install Python dependencies ──────────────────────────────────
# Runs pip install inside the container
# --no-cache-dir = don't store pip cache (keeps image smaller)
RUN pip install --no-cache-dir -r requirements.txt

# ─── Copy the rest of your code ───────────────────────────────────
# Now copy everything else (app.py, tests/, etc.)
# The . on the right means "into the WORKDIR (/app)"
COPY . .

# ─── Tell Docker which port the app uses ──────────────────────────
# This doesn't actually open the port — it's documentation.
# The actual port mapping happens in docker-compose.yml
EXPOSE 5000

# ─── Start command ────────────────────────────────────────────────
# What to run when the container starts.
# Using a list format (not a string) is best practice.
CMD ["python", "app.py"]
