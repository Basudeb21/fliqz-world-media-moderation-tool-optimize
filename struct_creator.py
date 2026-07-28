from pathlib import Path
import venv
import os

PROJECT_ROOT = Path.cwd()

directories = [
    "app",

    "app/api",

    "app/core",
    "app/core/config",
    "app/core/logger",
    "app/core/redis",
    "app/core/queue",
    "app/core/storage",
    "app/core/gpu",
    "app/core/metrics",
    "app/core/events",
    "app/core/constants",
    "app/core/exceptions",
    "app/core/security",

    "app/contracts",

    "app/coordinator",

    "app/pipeline",

    "app/scheduler",

    "app/workers",
    "app/workers/base",

    "app/modules",
    "app/modules/detectors",
    "app/modules/detectors/base",
    "app/modules/detectors/minor",
    "app/modules/detectors/nsfw",
    "app/modules/detectors/weapon",
    "app/modules/detectors/violence",
    "app/modules/detectors/pii",
    "app/modules/detectors/alcohol",
    "app/modules/detectors/smoking",
    "app/modules/detectors/drugs",
    "app/modules/detectors/animal",
    "app/modules/detectors/face",
    "app/modules/detectors/age",
    "app/modules/detectors/logo",
    "app/modules/detectors/self_harm",
    "app/modules/detectors/custom",

    "app/modules/policies",
    "app/modules/policies/base",
    "app/modules/policies/instagram",
    "app/modules/policies/onlyfans",
    "app/modules/policies/fansly",
    "app/modules/policies/reddit",
    "app/modules/policies/custom",

    "app/modules/models",
    "app/modules/models/yolo",
    "app/modules/models/owlvit",
    "app/modules/models/onnx",
    "app/modules/models/tensorrt",
    "app/modules/models/triton",

    "app/modules/storage",
    "app/modules/storage/local",
    "app/modules/storage/minio",
    "app/modules/storage/s3",

    "app/aggregation",

    "app/database",
    "app/database/models",
    "app/database/repositories",
    "app/database/migrations",

    "app/monitoring",

    "app/cleanup",

    "app/common",

    "storage",
    "storage/uploads",
    "storage/frames",
    "storage/evidence",
    "storage/reports",
    "storage/temp",
    "storage/archive",

    "logs",
    "logs/coordinator",
    "logs/scheduler",
    "logs/workers",
    "logs/aggregation",
    "logs/database",
    "logs/cleanup",

    "tests",
    "tests/unit",
    "tests/integration",
    "tests/performance",
    "tests/stress",

    "docker",
    "docker/coordinator",
    "docker/worker",
    "docker/aggregation",
    "docker/monitoring",
    "docker/compose",

    "scripts",

    "docs",
    "docs/architecture",
    "docs/api",
    "docs/detectors",
    "docs/deployment",
    "docs/developer_guide",
]

files = [
    ".env",
    ".env.example",
    ".gitignore",
    "README.md",
    "LICENSE",
    "pyproject.toml",
    "docker-compose.yml",
    "requirements.txt",

    "app/__init__.py",
    "app/main.py",

    "app/api/__init__.py",

    "app/core/__init__.py",
    "app/core/config/__init__.py",
    "app/core/logger/__init__.py",
    "app/core/redis/__init__.py",
    "app/core/queue/__init__.py",
    "app/core/storage/__init__.py",
    "app/core/gpu/__init__.py",
    "app/core/metrics/__init__.py",
    "app/core/events/__init__.py",
    "app/core/constants/__init__.py",
    "app/core/exceptions/__init__.py",
    "app/core/security/__init__.py",

    "app/contracts/__init__.py",

    "app/coordinator/__init__.py",

    "app/pipeline/__init__.py",

    "app/scheduler/__init__.py",

    "app/workers/__init__.py",
    "app/workers/base/__init__.py",

    "app/modules/__init__.py",
    "app/modules/detectors/__init__.py",
    "app/modules/policies/__init__.py",
    "app/modules/models/__init__.py",
    "app/modules/storage/__init__.py",

    "app/aggregation/__init__.py",

    "app/database/__init__.py",
    "app/database/models/__init__.py",
    "app/database/repositories/__init__.py",

    "app/monitoring/__init__.py",

    "app/cleanup/__init__.py",

    "app/common/__init__.py",
]


def touch(path: Path):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()


print("Creating directories...")

for directory in directories:
    (PROJECT_ROOT / directory).mkdir(parents=True, exist_ok=True)

print("Creating files...")

for file in files:
    touch(PROJECT_ROOT / file)

print("Creating detector package files...")

detectors = [
    "minor",
    "nsfw",
    "weapon",
    "violence",
    "pii",
    "alcohol",
    "smoking",
    "drugs",
    "animal",
    "face",
    "age",
    "logo",
    "self_harm",
    "custom",
]

for detector in detectors:
    detector_path = PROJECT_ROOT / "app/modules/detectors" / detector

    for filename in [
        "__init__.py",
        "detector.py",
        "model.py",
        "voting.py",
        "evidence.py",
        "schemas.py",
        "utils.py",
    ]:
        touch(detector_path / filename)

print("Creating virtual environment (.venv)...")

venv_dir = PROJECT_ROOT / ".venv"

if not venv_dir.exists():
    venv.create(venv_dir, with_pip=True)
else:
    print(".venv already exists")

requirements = """fastapi
uvicorn
redis
sqlalchemy
pymysql
pydantic
pydantic-settings
opencv-python
pillow
numpy
python-dotenv
ultralytics
torch
torchvision
ffmpeg-python
prometheus-client
"""

(PROJECT_ROOT / "requirements.txt").write_text(requirements)

gitignore = """
.venv/
__pycache__/
*.pyc
.env
.idea/
.vscode/
storage/
logs/
"""

(PROJECT_ROOT / ".gitignore").write_text(gitignore.strip())

print()
print("=" * 60)
print("✅ FliqzWorld Media Moderation project created successfully!")
print("=" * 60)
print()
print("Next steps:")
print("1. source .venv/bin/activate")
print("2. pip install -r requirements.txt")
print()