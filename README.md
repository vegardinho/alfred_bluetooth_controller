# Alfred Workflow: Bluetooth Controller

A powerful toolkit for managing your bluetooth connections. Includes Remote Trigger, to manage your Bluetooth devices on
the big screen.

## Contents

---------------

- [Contents](#contents)
- [Installation](#installation)
- [Usage](#usage)
    - [Manage Bluetooth Status](#manage-bluetooth-status)
    - [Toggle Device Connections](#toggle-device-connections)
    - [Manage Favorite Device](#manage-favorite-device)
    - [Pair/Unpair Device](#pairunpair-device)
    - [Large-Type Bluetooth Status](#large-type-bluetooth-status)
    - [Safe Mode](#safe-mode)
    - [Remote Trigger](#remote-trigger)
- [Troubleshooting](#troubleshooting)

## Installation

----------

Download the [Alfred workflow](https://github.com/vegardinho/alfred_bluetooth_controller/releases/latest) and
double-click to install! If you encounter issues related to the blueutil or notificator scripts,
see [troubleshooting section](#troubleshooting).

## Usage

----------
![usage snippet](img/alfred_bluetooth_long.gif "Usage snippet")

### Manage Bluetooth Status

- Turn bluetooth on: `bton`
- Turn bluetooth off: `btoff`
- Reset (disable, wait 1.5 seconds, enable: `btr`

### Toggle Device Connections

- Connect/disconnect from device: `btd` + `device name`
- By typing an argument, the workflow will automatically search through all devices prevously paired with the computer.

### Manage Favorite Device

- Set favorite device: `btsetfavorite` + `device name`
- Connect to favorite device:
    - with hotkey: `cmd-ctr-option-f`
    - with keyword: `btf` + `device name`

### Pair/Unpair Device

- Pair:
    - `btd` + `device name`
    - Wait 5 seconds for results to show up.
- Unpair:
    - `btu` + `device name` + press modifier key `cmd`

### Large-Type Bluetooth Status

- See status of bluetooth connection and paired devices.
- `btstatus`

### Safe Mode

Set environment variable `confirm` in workflow to `true` if you want to force user confirmation on toggle and
deactivation commands. (Useful for iMacs and Mac Minis who that would have trouble turning Bluetooth on again without
any input devices.)

### Remote triggers
Most, or all, the listed commands have their own Remote Trigger. (You're welcome to add ones that are missing.)


## Troubleshooting

------

If you get errors when using the workflow referring to not being able to use `blueutil` as it cannot be checked, you will need to manually remove the quarantine attribute from the bundled binary.
This can be done like so: 

1. Open workflow folder in Terminal by right clicking workflow (as shown in image below) ![open-in-terminal](img/open-in-terminal.png "How to open directory in Terminal")
2. Use the following command once in directory: `xattr -d com.apple.quarantine ./blueutil`
