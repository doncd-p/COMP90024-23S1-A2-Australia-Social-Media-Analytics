#!/bin/bash

export ANSIBLE_CONFIG=configure/ansible.cfg

ansible-playbook deploy_couchdb_cluster.yaml --ask-become-pass -vvv