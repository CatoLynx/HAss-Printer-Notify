# Home Assistant notifications on a serial printer
This is a small REST server that works in conjunction with the RESTful notification integration of Home Assistant.
It prints every received notification on a serial printer.

# License
Public domain, do whatever you want.

# Setup
Just add this to your `configuration.yaml`:

```
notify:
  - platform: rest
    name: Printer
    resource: "http://127.0.0.1:2342/notify.json"
```