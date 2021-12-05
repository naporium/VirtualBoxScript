### MachineOrchestrator.py
This script create 4 new virtual machines, based on the virtualbox command VBoxManage clonevm
(One may adapt the settings)

### Who may want to use the tool
One that needs a virtual lab for tests, using __ORACLE VirtualBox__

### How to use it  
run the script 
```
$ python MachineOrchestrator.py
```

__NOTE:__ This script create 4 new virtual machines, based on the virtualbox command 'VBoxManage clonevm'

If we just nead one machine, we may configure the settings accordingly

 - [x] E.G.
   How to ADD a Custom Machine 
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



