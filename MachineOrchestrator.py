#!/usr/bin/env python

__author__ = "Naporium"
__license__ = "USE AT YOUR OWN RISK"
__version__ = 2021

# SOURCES:
# https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-clonevm.html
# https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-modifyvm.html#

from enum import Enum
from subprocess import Popen, PIPE, CalledProcessError
from collections import namedtuple


class InterfaceAdapter(Enum):
    INTERFACE_1 = 1
    INTERFACE_2 = 2
    INTERFACE_3 = 3
    INTERFACE_4 = 4


class InterfaceAdapterType(Enum):
    NAT = "nat"
    NAT_NETWORK = "natnetwork"
    BRIDGED = "bridged"
    INTERNAL = "intnet"
    HOST_ONLY = "hostonly"
    NOT_PRESENT = "none"


Machine = namedtuple("Machine", ("name",
                                 "cpu",
                                 "memory",
                                 "interface_adapter",
                                 "interface_type",
                                 "interface_name")
                     )


def validate_existing_machine(verify_this_machine_name):
    """
    Check if a name is a Valid Virtual box Virtual Machine
    :param verify_this_machine_name:
    :return: <Boolean> True if is valid, False otherwise
    """

    os_command_to_run = (f'vboxmanage list vms')
    cmd = os_command_to_run
    # bufsize, if given, has the same meaning as the corresponding argument to the built-in open() function:
    # 0 means unbuffered,
    # 1 means line buffered,
    # any other positive value means use a buffer of (approximately) that size.
    # A negative bufsize means to use the system default, which usually means fully buffered.
    # The default value for bufsize is 0 (unbuffered).
    with Popen(cmd, stdout=PIPE, bufsize=-1, universal_newlines=True, shell=True) as p:
        data = []
        for line in p.stdout:
            data.append(line)

    if p.returncode == 0:
        print(data)
        # print(json.dumps(result, indent=4))
        for line in data:
            vm_name = line.split(' ')[0]
            vm_name = vm_name.split('"')[1]
            if verify_this_machine_name == vm_name:
                return True  # Return means that machine name already exists
        return False  # machine does exist
    if p.returncode != 0:
        raise RuntimeError(p.returncode, p.args)


def clone_virtual_machine(clone_this_machine, machine=None):

    # check if machine to be cloned exist
    if validate_existing_machine(clone_this_machine) is False:
        raise RuntimeError(f"Machine does not exist {clone_this_machine}")
    else:
        print(f"Machine to Clone exist: {clone_this_machine}")

    # CHECK IF MACHINE ALREADY EXIST: if a machine with this name already exists in virtualbox, we should warn the user
    if validate_existing_machine(machine.name) is True:
        raise RuntimeError(f"Machine (machine name to create) already exists: {machine.name}"
                           f"\nChange the name or erase existing machine")
    else:
        print(f"Ready to Create a Clone...")

    # Verify that there is a configuration setting for the new machine
    # TODO: should very parameters.
    #  we are assuming, correct values for each key...
    if machine is None:
        raise RuntimeError("We need configuration for the machine to be cloned")

    os_command_to_run = (f'VBoxManage clonevm {clone_this_machine} --name={machine.name} --register --mode=all')
    cmd = os_command_to_run
    # bufsize, if given, has the same meaning as the corresponding argument to the built-in open() function:
    # 0 means unbuffered,
    # 1 means line buffered,
    # any other positive value means use a buffer of (approximately) that size.
    # A negative bufsize means to use the system default, which usually means fully buffered.
    # The default value for bufsize is 0 (unbuffered).

    _subprocess = Popen(cmd, stdout=PIPE, bufsize=-1, universal_newlines=True, shell=True)
    _subprocess.wait()
    if _subprocess.returncode == 0:
        return True
    else:
        raise RuntimeError("Something Went wrong")


def modify_machine_settings( machine=None):
    # Verify that there is a configuration setting for the new machine
    # TODO: should very parameters.
    #  we are assuming, correct values for each key... ANd keys are OK!
    if machine is None:
        raise RuntimeError("We need configuration settings so that we can modify the machine settings")

    # check if machine to be cloned exist
    if validate_existing_machine(machine.name) is False:
        raise RuntimeError(f"Machine does not exist {machine.name}. Create or clone one machine  first")
    else:
        print(f"Ready to modify: {machine.name}")

    os_command_to_run = (f'vboxmanage modifyvm {machine.name} --nic{machine.interface_adapter} {machine.interface_type}'
                         f' --{machine.interface_type}{machine.interface_adapter} {machine.interface_name} '
                         f'--cpus={machine.cpu} --memory={machine.memory}')
    # "vboxmanage modifyvm $NEW_MACHINE_NAME --cpus=$NUMBER_CPUS --memory=$MEMORY --nic3 intnet --intnet3 my_new_internal_network "
    print(f"Virtual Box Command to execute:{os_command_to_run}")
    cmd = os_command_to_run

    _subprocess = Popen(cmd, stdout=PIPE, bufsize=-1, universal_newlines=True, shell=True)
    _subprocess.wait()
    if _subprocess.returncode == 0:
        return True
    else:
        raise RuntimeError("Something Went wrong")

def modify_interface(machine=None):
    """
    Change virtual box adapter to Nat or bridged
    :param machine:
    :return:
    """


    # Verify that there is a configuration setting for the new machine
    # TODO: should very parameters.
    #  we are assuming, correct values for each key... ANd keys are OK!
    if machine is None:
        raise RuntimeError("We need configuration settings so that we can modify the machine settings")

    # check if machine to be cloned exist
    if validate_existing_machine(machine.name) is False:
        raise RuntimeError(f"Machine does not exist {machine.name}. Create or clone one machine  first")
    else:
        print(f"Ready to modify: {machine.name}")

    os_command_to_run = (f'vboxmanage modifyvm {machine.name} --nic{machine.interface_adapter} '
                         f' {machine.interface_type}')
    # "vboxmanage modifyvm $NEW_MACHINE_NAME --cpus=$NUMBER_CPUS --memory=$MEMORY --nic3 intnet --intnet3 my_new_internal_network "
    print(f"Virtual Box Command to execute:{os_command_to_run}")
    cmd = os_command_to_run

    _subprocess = Popen(cmd, stdout=PIPE, bufsize=-1, universal_newlines=True, shell=True)
    _subprocess.wait()
    if _subprocess.returncode == 0:
        return True
    else:
        raise RuntimeError("Something Went wrong")


if __name__ == "__main__":
    """
    This script will clone 4 virtual box virtual machines: A Dchp Server, Dns master, Dns Slave, Linux_Router 
    """

    # CONFIGURE SETTINGS for 4 machines:
    INTERNAL_INTERFACE_NAME = f"'{'NOVA'}'"

    dhcp_server = Machine(
        name="DHCP_SERVER1",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_3.value,
        interface_type=InterfaceAdapterType.INTERNAL.value,
        interface_name=INTERNAL_INTERFACE_NAME
    )

    dns_master = Machine(
        name="DnsMaster",
        cpu=2,
        memory=2048,
        interface_adapter=InterfaceAdapter.INTERFACE_3.value,
        interface_type=InterfaceAdapterType.INTERNAL.value,
        interface_name=INTERNAL_INTERFACE_NAME
    )
    dns_slave = Machine(
        name="DnsSlave",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_3.value,
        interface_type=InterfaceAdapterType.INTERNAL.value,
        interface_name=INTERNAL_INTERFACE_NAME
    )
    linux_router = Machine(
        name="LinuxRouter",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_3.value,
        interface_type=InterfaceAdapterType.INTERNAL.value,
        interface_name=INTERNAL_INTERFACE_NAME
    )

    # CHANGE THIS: THIS MACHINE WILL BE THE MACHINE THAT EXISTS IN VIRTUALBOX AND WE WILL USE TO CLONE
    WHICH_MACHINE_TO_CLONE = "DebianBase"

    machines = (dhcp_server, dns_master, dns_slave, linux_router)
    for machine in machines:
        clone_virtual_machine(clone_this_machine=WHICH_MACHINE_TO_CLONE, machine=machine)
        print(f"New Virtual box machine name is {machine.name}")
        modify_machine_settings(machine=machine)

    # ADD ONE MORE INTERFACE TO LINUX ROUTER
    linux_router = Machine(
        name="LinuxRouter",
        cpu=1,
        memory=1024,
        interface_adapter=InterfaceAdapter.INTERFACE_4.value,
        interface_type=InterfaceAdapterType.INTERNAL.value,
        interface_name="SecondPrivateNetwork"
    )
    modify_machine_settings(machine=linux_router)

    # create configurations, so that we can change network adapter 4 to a bridge
    dhcp_server = Machine(
        name="DHCP_SERVER1",
        interface_adapter=InterfaceAdapter.INTERFACE_4.value,
        interface_type=InterfaceAdapterType.BRIDGED.value,
    )
    modify_interface(dhcp_server)