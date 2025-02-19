#!/bin/bash

# Get some spec file info

spec_file=./gamescope-session-guide.spec

author=$(grep '%global author\s.*$' $spec_file | awk '{ print $3 }')
main_repo=$(grep '%global repository\s.*$' $spec_file | awk '{ print $3 }')

current_main_commit=$(grep '%global maincommit\s.*$' $spec_file | awk '{ print $3 }')
