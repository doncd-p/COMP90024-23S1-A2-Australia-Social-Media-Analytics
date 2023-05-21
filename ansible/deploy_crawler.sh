#!/bin/bash

export ANSIBLE_CONFIG=configure/crawler.cfg

ansible-playbook deploy_crawler.yaml --ask-become-pass -vvv