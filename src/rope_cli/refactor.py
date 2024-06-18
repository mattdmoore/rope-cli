from rope.base.project import Project
from rope.base import libutils
from rope.refactor.rename import Rename

PROJECT = Project('.')

def rename(path, old_name, new_name):
    resource = libutils.path_to_resource(PROJECT, path)
    content = resource.read()

    offset = content.find(old_name)
    if offset == -1:
        raise ValueError(f"'{old_name}' not found in {path}")
    
    changes = Rename(PROJECT, resource, offset).get_changes(new_name)
    print(f'Renamed {old_name} to {new_name} in {path}')
    apply_changes(changes)

def undo():
    try:
        result = PROJECT.history.undo()
        print(f"Successfully undid: {result}")
    except Exception as e:
        print(f"Undo failed: {e}")

def redo():
    try:
        result = PROJECT.history.undo()
        print(f"Successfully undid: {result}")
    except Exception as e:
        print(f"Undo failed: {e}")

def apply_changes(changes):
    PROJECT.validate(PROJECT.root)
    PROJECT.do(changes)
    PROJECT.close()
