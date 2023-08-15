#! /bin/bash

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/wsl_desktop_key
ssh -T git@github.com
