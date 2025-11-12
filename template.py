import os 
from pathlib import Path 

files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py", ## Only the source code,

    # we have two pipelines in ML, Training and Inferencing
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_eval.py",
    
    "src/pipeline/__init__.py",
    "src/pipeline/training.py",
    "src/pipeline/training.py",
    "src/pipeline/prediction.py",
    "src/pipeline/prediction.py",

    "src/utils/__init__.py",
    "src/utils/utils.py",

    "src/logger/logging.py",
    "src/exceptions/exception.py",


    "test/unit/__init__.py",
    "test/integration/__init__.py",

    "init_setup.sh",
    
    "requirements.txt",
    "requirements_dev.txt",

    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    
    "experiments/experiments.ipynb",
]



for filepath in files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "": 
        os.makedirs(filedir, exist_ok=True)
        
        print(f"Creating Directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open(filepath, "w") as f: 
            pass
