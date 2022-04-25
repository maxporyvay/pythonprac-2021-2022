DOIT_CONFIG = {'default_tasks': ['diagram']}

def task_diagram():
    """Convert dot diagram to png"""
    return {
            "actions": ["dot -Tpng diagram.dot -o diagram.png"],
            "file_dep": ["diagram.dot"],
            "targets": ["diagram.png"],
    }


def task_icon():
    """Create an icon"""
    iname = "prog/icon.png"
    return {
            "actions": [f"convert diagram.png -crop 200x200+100+100 -resize 64x64 {iname}"],
            "file_dep": ["diagram.png"],
            "targets": [iname],
    }


def task_cleanup():
    """Remove all"""
    return {
            "actions": ["rm *.png prog/*.png"],
    }
