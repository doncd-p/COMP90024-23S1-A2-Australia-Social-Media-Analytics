# Deployment

## Deply on remote instance
ansible-playbook -i inventory/mrc.ini remote_playbook.yaml --ask-become-pass

# Requirement
ansible >= 7.5.0
python >= 3.11

conda install ansible
or pip install ansible
