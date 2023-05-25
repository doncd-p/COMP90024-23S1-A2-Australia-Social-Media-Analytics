#!/bin/bash

export ANSIBLE_CONFIG=configure/ansible.cfg

ansible-playbook configure_mrc_instances.yaml --ask-become-pass --ask-vault-pass -vvv