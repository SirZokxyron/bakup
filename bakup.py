import argparse
import shutil
import os
import sys

# === Functions === #

def check_exist(file: str, quiet: bool=False):
    exists = os.path.exists(file)
    if not exists:
        if not quiet:
            print(f'bakup: WARNING, `{file}` doesn\'t exist')
    return exists


def copy(source: str, destination: str):
    is_directory = os.path.isdir(source)
    if is_directory:
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination) 

def backup_file(source_file: str, quiet: bool=False):
    backup_file = f'.{source_file}.bak'
    copy(source_file, backup_file)
    if not quiet:
        print(f'bakup: `{source_file}` backed up to `{backup_file}`')

def restore_file(source_file: str, quiet: bool=False):
    backup_file = f'.{source_file}.bak'
    copy(backup_file, source_file)
    if not quiet:
        print(f'bakup: `{source_file}` restored from `{backup_file}`')

def clean(quiet: bool=False, force: bool=False):
    if not force:
        confirmation = input('bakup: sure you want to delete all backup in your current working directory? [y|N] ')
        if confirmation != 'y' :
            if not quiet:
                print('bakup: operation cancelled')
            sys.exit(0)
    
    files_to_remove = filter(lambda x: x.endswith('.bak'), os.listdir())
    for file in files_to_remove:
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
        if not quiet:
            print(f'bakup: deleted `{file}`')

# === Parser === #

parser = argparse.ArgumentParser(description='A simple bakup utility.')

operation_group = parser.add_mutually_exclusive_group(required=True)
operation_group.add_argument('-b', '--backup', action='store_true', help='backup the given files or directories')
operation_group.add_argument('-r', '--restore', action='store_true', help='restore the given files or directories')
operation_group.add_argument('-c', '--clean', action='store_true', help='delete all backups in the current working directory')

parser.add_argument('-f', '--force', action='store_true', help='skip the confirmation of backup deletion')
parser.add_argument('-q', '--quiet', action='store_true', help='prevent the verbose output')
parser.add_argument('files', nargs='*', help='files or directories to operate on')

# === Main === #

if __name__ == '__main__':
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(-1)

    args = parser.parse_args()
    
    if args.clean:
        clean(quiet=args.quiet, force=args.force)

    elif args.backup:
        for file in args.files:
            if check_exist(file, args.quiet):
                backup_file(file, args.quiet)
    
    elif args.restore:
        for file in args.files:
            backup_file = f'.{file}.bak'
            if check_exist(backup_file, args.quiet):
                restore_file(file, args.quiet)
