#!/bin/bash

export ANSIBLE_CONFIG=configure/ansible.cfg

ansible-playbook deploy_frontend.yaml --ask-become-pass -vvv