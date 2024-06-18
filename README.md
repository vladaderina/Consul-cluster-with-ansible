Consul cluster with ansible
=========

Deploying virtual machines by terraform using a file "virtualbox.tf"

The command to run ansible-playbook
------------
ansible-playbook playbook.yaml -i inventory.yaml --extra-vars "ansible_sudo_pass=vagrant"


Architecture
------------
3 server nodes: [10.0.2.9, 10.0.2.10, 10.0.2.11] <br />
1 client node: [10.0.2.12]

Tests
------------
1. Consul's version
2. Server check
3. Status check
