ELKpi
=====

This is an ansible playbook for installing an ELK stack on Raspberry pi 2 or 3
Please change the values in vars-rpi.yml then launch ansible-playbook -i hosts elk-rpi.yml

Troubleshoot
----------

Kibana service is not always starting. I suggest you launch it with
```
cd /opt/kibana/bin
sudo ./kibana "-c /opt/kibana/config/kibana.yml"
```

Issues are welcome.
