# Deployment

## Requirement
ansible >= 7.5.0
python >= 3.11

conda install ansible
or pip install ansible

## How to run
1. To deploy instance
    1. run `./create_mrc_instance.sh`
    2. enter your openstack password
    3. enter your personal device password
2. To configure instance
    1. run `./configure_mrc_instance.sh`
    2. enter your personal device password
    3. enter your ansible vault password
3. To deploy crawler
    1. run `./deploy_crawler.sh`
    2. enter your personal device password
4. To deploy cluster
    1. run `./deploy_couchdb_cluster.sh`
    2. enter your personal device password
5. To deploy backend
    1. run `./deploy_backend.sh`
    2. enter your personal device password
6. To deploy frontend
    1. run `./deploy_frontend.sh`
    2. enter your personal device password
