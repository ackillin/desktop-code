#! /bin/bash

eval "$(ssh-agent -s)"
eval $SSH_AUTH_SOCK
ssh-add wsl_desktop_key_copy
ssh -T git@github.com
