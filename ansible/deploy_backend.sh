#!/bin/bash

export ANSIBLE_CONFIG=configure/ansible.cfg

ansible-playbook deploy_backend.yaml --ask-become-pass -vvv