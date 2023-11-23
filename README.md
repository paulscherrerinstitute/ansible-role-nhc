[![Build Status](https://travis-ci.org/CSCfi/ansible-role-nhc.svg?branch=master)](https://travis-ci.org/CSCfi/ansible-role-nhc)
ansible-role-nhc
=========

Install and configure the [LBNL Node Health Checker](https://github.com/mej/nhc)

This Role has been tested for RHEL8 and SUSE 15.3 and 15.4!

Requirements
------------

- A batch scheduler, like SLURM
- Internet access to Github

Role Variables
--------------

See defaults/main.yml for a complete list

- `nhc_use_default_checks`: if `true` then all the default checks in `nhc.conf` will not be added, only the ones in `nhc_checks` list.

  ```yaml
  nhc_use_default_checks: True

  nhc_checks:
   - { match: "*", name: "check_reboot_slurm", arguments: "" }
   - { match: "{gpu[1-19]}", name: "check_hw_ib", arguments: "40" }
  ```

- `nhc_rm`: which resource manager to configure for, such as `"slurm"`, `"pbs"`, or `"torque"`. Note that setting to `""` (empty string)
   uses autodetection to determine the resource manager (Default is `"slurm"`)
- `nhc_check_gpu`: add checks for GPUs (Defaults is `false`)

Dependencies
------------

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
    - hosts: servers
      roles:
         - { role: ansible-role-nhc }
```

License
-------

MIT

Author Information
------------------
