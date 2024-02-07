import pyvan


OPTIONS = {"main_file_name": "quiz.py", 
            "show_console": False,
            "use_pipreqs": True,
            "install_only_these_modules": [],
            "exclude_modules":[],
            "include_modules":[]
            }

pyvan.build(**OPTIONS)
