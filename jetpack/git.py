import subprocess


def get_git_tag():
    """Get the latest tag 

    If the current working directory is a git repository
    return the latest tag on it. If not tags exists return
    the latest commit hash. If both of these fail return None
    """
    try:
        label = subprocess.check_output(['git', 'describe']).decode().strip()
        return label
    except subprocess.CalledProcessError as grepexc:
        return get_git_commit()


def get_git_commit():
    """Get the latest git commit

    If the current working directory is a git repository
    return the latest commit else return None
    """
    try:
        label = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
        return label
    except subprocess.CalledProcessError as grepexc:
        return None