# bakup

> a simple backup command line utility.

## Installation

It's a singular python file.

## Usage

- `bakup -h` will bring you the help message
- `bakup -b <file1> <file2> ...` will create a hidden copy of the given files
- `bakup -r <file1> <file2> ...` will attempt to restore the given file to their hidden copy state
- `bakup -c` will delete every hidden copy in the current working directory

There are two other arguments:

- `-f` to use in conjunction with `-c` will force the deletion of backup up file, skipping confirmation.
- `-q` will remove the verbose output of the program

## Known issues

Doesn't work on Windows yet™️  :^)

## Improvements

There are cool features that could be added like per-directory config that could specify the backup file extension, or compressing the backups to save on disk space, etc.
But I'm intentionally keeping this very simple because it's enough for my needs.
Feel free to fork it and upgrade it if you feel like it.

## Copyright

Copyright © 2025 SirHugo <<hugo.bensbia@gmail.com>>  
This work is free. You can redistribute it and/or modify it under the  
terms of the Do What The Fuck You Want To Public License, Version 2,  
as published by Sam Hocevar. See the LICENSE file for more details.  
