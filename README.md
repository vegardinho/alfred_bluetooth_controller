# Alfred Workflow: Bluetooth Controller <!-- omit in toc -->

A powerful toolkit for managing your bluetooth connections. Includes Remote Trigger, to manage your Bluetooth devices on
the big screen.

## Contents <!-- omit in toc -->

- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
    - [Manage bluetooth status](#manage-bluetooth-status)
    - [Toggle Device Connections](#toggle-device-connections)
    - [Manage favorite device](#manage-favorite-device)
    - [Pair/Unpair Device](#pairunpair-device)
    - [Large-Type Bluetooth Status](#large-type-bluetooth-status)
  - [Safe Mode](#safe-mode)
  - [Remote triggers](#remote-triggers)
- [Attribution](#attribution)
- [Remove quarantine with terminal](#remove-quarantine-with-terminal)
- [Installation images](#installation-images)
- [Screenshots](#screenshots)

---

## Installation

1. Download the [Alfred workflow](https://github.com/vegardinho/alfred_bluetooth_controller/releases/latest) and
   double-click to install!
2. Allow `blueutil` and `notificator` to run (remove the quarantine attribute from the bundled binary). This can alternatively be done [using the terminal](#Remove-quarantine-with-terminal).
   1. Open workflow folder in Finder by right clicking workflow ([see image](#installation-images)).
   2. Right-click on `blueutil` and click 'open' ([see image](#installation-images)).
   3. Confirm open when dialog appears.
   4. Repeat with `notificator` file.
3. Enjoy!

---

## Usage

### Commands

#### Manage bluetooth status

- Turn bluetooth on: `bton`
- Turn bluetooth off: `btoff`
- Toggle bluetooth status: `bttoggle`
- Reset (disable, wait 1.5 seconds, enable: `btreset`

#### Toggle Device Connections

- Connect/disconnect from device: `btd` + `device name`

#### Manage favorite device

- Set favorite device: `btsetfavorite` + `device name`
- Toggle connection with favorite device:
  - with hotkey: `cmd-ctr-option-f`
  - with keyword: `btfavorite`
- Remove device as favorite:
  - `btd` + `device name` + press modifier key `shift`
  - `btsetfavorite` + `device name` + press modifier key `shift`

#### Pair/Unpair Device

- Pair:
  - `btp` + `device name`
  - Wait 5 seconds for results to show up.
- Unpair:
  - `btd` + `device name` + press modifier key `cmd`

#### Large-Type Bluetooth Status

- See status of bluetooth connection and paired devices.
- `btstatus`

### Safe Mode

Set environment variable `confirm` in workflow to `true` if you want to force user confirmation on toggle and
deactivation commands. (Useful for iMacs and Mac Minis who that would have trouble turning Bluetooth on again without
any input devices.)

### Remote triggers

Most, or all, the listed commands have their own Remote Trigger. (You're welcome to add ones that are missing.)

---

## Attribution

- [blueutil](https://github.com/toy/blueutil) binary is used for bluetooth functionality.
- [notificator](https://github.com/vitorgalvao/notificator) binary is used for notifications.

---

## Remove quarantine with terminal

Use the following command once in directory:

- Blueutil: `xattr -d com.apple.quarantine ./blueutil`
- Notificator: `xattr -d com.apple.quarantine ./notificator`

---

## Installation images

!["How to open directory in Finder"](img/open-in-finder.png)
!["How to open directory in Finder"](img/open-in-terminal.png)
![How to open binary file](img/open-manually.png)

---

## Screenshots

![Screenshot of all options](img/screenshot_bt.png)
![Screenshot of device toggle](img/screenshot_btd.png)
