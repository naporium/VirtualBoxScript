### MachineOrchestrator.py
This script create 4 new virtual machines, based on the virtualbox command VBoxManage clonevm

__(One may adapt the settings)__

### Who may want to use the tool
Could be useful for rapidly create and virtual labs for tests, when using __ORACLE VirtualBox__

### Requirements
1 virtual machine should exist and be registered in virtual box.

### How to use it  
run the script 
```
$ python MachineOrchestrator.py
```

__NOTE:__ This script create 4 new virtual machines, based on the virtualbox command 'VBoxManage clonevm'

If we just nead one machine, we may configure the settings accordingly.

   

### How to ADD a Custom Machine 
```
# define Existing machine in virtualbox used as base machine for cloning
WHICH_MACHINE_TO_CLONE = "Existing_vm_machine_name"

# define internal network name
INTERNAL_INTERFACE_NAME = f"'{'NEW_virtualBoxNetwork'}'"

# create new machine settings
radius_server = Machine(
        name="radiusServer",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_3.value,
        interface_type=InterfaceAdapterType.INTERNAL.value,
        interface_name=INTERNAL_INTERFACE_NAME
    )
# clone the machine
clone_virtual_machine(clone_this_machine=WHICH_MACHINE_TO_CLONE, machine=machine)   

# modify settings
modify_machine_settings(machine=linux_router)
``` 
### Set virtual box adapter4 for the DHCP_SERVER1 to Bridge
```
# create configurations, so that we can change network adapter 4 to a bridge
    dhcp_server = Machine(
        name="DHCP_SERVER1",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_4.value,
        interface_type=InterfaceAdapterType.BRIDGED.value,
        interface_name=None
    )
    modify_interface(dhcp_server)
```

### Set virtual box adapter3 for the DHCP_SERVER1 to NAT
```
# create configurations, so that we can change network adapter 4 to a bridge
    dhcp_server = Machine(
        name="DHCP_SERVER1",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_3.value,
        interface_type=InterfaceAdapterType.NAT.value,
        interface_name=None
    )
    modify_interface(dhcp_server)
```



