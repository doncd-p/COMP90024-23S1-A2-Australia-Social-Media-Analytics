#!/bin/bash

. ./unimelb-comp90024-2023-grp-9-openrc.sh; ansible-playbook create_mrc_instances.yaml --ask-become-pass -vvv