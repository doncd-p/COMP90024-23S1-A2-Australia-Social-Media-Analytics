#!/bin/bash

export ANSIBLE_CONFIG=configure/ansible.cfg

ansible-playbook deploy_crawler.yaml --ask-become-pass -vvv