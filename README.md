stratDeployWhirr
==============

Notice: This script is a prototype and needs adjustment in the files conf/* and scripts/*. Severall issues occurred while developing
and was only successfully tested on Ubuntu 12.04. A test on 13.10 failed.
See it as a fragile running proof of conecpt.

Running the script
-------------------

1. Create certificates for ssh access
2. Create security group for provisioning instance
3. Write configuration file
4. run {python StartWhirrInstance.py}


Configuration file
-------------------
- conf/instances.cfg - configuration file needs adjustment (ssh keys, amazon credentials,...)
- scripts/AutoWhirrInstall.txt - script running on provisioning instance, needs adjustmen (ssh keys, amazon credentials,...)



