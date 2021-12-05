#!/usr/bin/bash

# 
# DEFINE CONST
#
CLONED_MACHINE_NAME="DebianBase"


NEW_MACHINE_NAME='DEBIAN_DHCP'
# the name for the new cloned machine


# Clone MAchine 
VBoxManage clonevm $CLONED_MACHINE_NAME --name=$NEW_MACHINE_NAME --register --mode=all

NUMBER_CPUS='2'
MEMORY='2048'
vboxmanage modifyvm $NEW_MACHINE_NAME --cpus=$NUMBER_CPUS --memory=$MEMORY
# MODIFY MACHINE SETTINGS: CPU AND MEMORY


INTERFACE_ID=3
# COULD BE 1,2,3,4 [We want to change adapter interface number id 3]
INTERNAL_NETWORK_NAME="novaRede"

vboxmanage modifyvm $NEW_MACHINE_NAME --nic$INTERFACE_ID intnet --intnet$INTERFACE_ID $INTERNAL_NETWORK_NAME
# MODIFY NETWORK for adapter3: 
# vboxmanage modifyvm DebianBaseClone --nic3 intnet --intnet3 "NOVA" 



