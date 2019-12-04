Nextcloud
=========

[![Build Status](https://travis-ci.org/trawiasty/ansible-role-nextcloud.svg?branch=master)](https://travis-ci.org/trawiasty/ansible-role-nextcloud)

Simple ansible role for provisioning Nextcloud with PHP-FPM.

Requirements
------------

- Compatible MySQL / MariaDB
- Reverse proxy in front of the PHP-FPM

Role Variables
--------------

See `defaults/main.yml`.

Dependencies
------------

None.

Example Playbook
----------------

```
- hosts: nextcloud
  roles:
    - role: ansible-role-nextcloud
```

License
-------

BSD

Author Information
------------------

[Paweł Tatarczuk](https://trawiasty.github.io)