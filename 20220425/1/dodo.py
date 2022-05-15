DOIT_CONFIG = {'default_tasks': ['updatebabel', 'compilebabel', 'test']}


def task_cleanup():
    return {
            'actions': ['rm po/lineq.pot',
                        'rm po/ru/LC_MESSAGES/lineq.mo']
    }


def task_extractandinitbabel():
    return {
            'actions': ['pybabel extract -o po/lineq.pot lineq.py',
                        'pybabel init -D lineq -i po/lineq.pot -d po -l ru'],
            'targets': ['po/lineq.pot']
    }


def task_updatebabel():
    return {
            'actions': ['pybabel update -D lineq -i po/lineq.pot -d po -l ru'],
            'file_dep': ['lineq.py'],
            'targets': ['po/ru/LC_MESSAGES/lineq.po']
    }


def task_compilebabel():
    return {
            'actions': ['pybabel compile -D lineq -d po -l ru'],
            'file_dep': ['po/ru/LC_MESSAGES/lineq.po'],
            'targets': ['po/ru/LC_MESSAGES/lineq.mo']
    }


def task_test():
    return {
            'actions': ['python3 -m unittest']
    }


##def task_build():
##    return {
##            'actions': ['python3 -m build']
##    }
