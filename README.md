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

- `nhc_rm`: which resource manager to configure for, such as `"slurm"`, `"pbs"`, or `"torque"`. Note that setting to `""` (empty string)
   uses autodetection to determine the resource manager (Default is `"slurm"`)
- `nhc_mark_offline`: when `true` cause batch manager to drain the node if problems are detected (Default is `true`)
- `nhc_timeout`: Time in seconds till checks timeout (Default is `120` seconds)
- `nhc_check_all`: If `true` perform all checks (Default is `true`)
- `nhc_short_hostname`: If `true` NHC will use node short name (using either `HOSTNAME_S` or `hostname -s` command) (Default is `true`)
- `nhc_debug`: When `true` have NHC print out debug information (Default is `false`)

The above settings are 1-to-1 with NHC general settings, which can be explicitly set though the `nhc_settings: {}` key.

To write checks, you add them to the `nhc_checks` key as a list of dictionaries, e.g.:

```yaml
nhc_checks: []
  slurm_checks:
    - { match: "*", command: "check_reboot_slurm", comment: "Reboot if slurmd shows as DRAIN" }
```

The top-level keys are used to group checks, with each check being made up of `match` and `command` field, and optionally `comment` field)

You can also add script to the NHC process and call these as checks, by appending them to the `nhc_scripts` key. *NOTE* that you can give
absolute paths to include scripts from outside the role directory. The scripts are run through the templating engine, so ansible specific
variables can be used here.

```yaml
nhc_scripts: []
  - "csc_nvidia_smi.nhc"
  - "healthcheck.nhc"
```

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
