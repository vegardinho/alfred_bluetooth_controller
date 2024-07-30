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
- [Troubleshooting](#troubleshooting)
  - [Notifications not working, or notificator error](#notifications-not-working-or-notificator-error)
  - [Error `xcrun: error: invalid active developer path`](#error-xcrun-error-invalid-active-developer-path)
  - [Remove quarantine using terminal](#remove-quarantine-using-terminal)
  - [Allow Alfred to control bluetooth](#allow-alfred-to-control-bluetooth)
  - [Why do I need to install blueutil with Homebrew?](#why-do-i-need-to-install-blueutil-with-homebrew)
- [Installation images](#installation-images)
- [Screenshots](#screenshots)
- [Attribution](#attribution)

---

## Installation

1. Download the [Alfred workflow](https://github.com/vegardinho/alfred_bluetooth_controller/releases/latest) and
   double-click to install.
2. Run [Resolve Dependencies](https://www.alfredapp.com/help/kb/dependencies/) in Alfred Preferences.
3. [Allow Alfred to control bluetooth](#allow-alfred-to-control-bluetooth).
4. Enjoy!

Please see [troubleshooting section](#troubleshooting) if you experience any issues, and post an issue if the problem persists. Description of commands can be found below.

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

Set workflow configuration variable `confirm` in workflow to `true` if you want to force user confirmation on toggle and
deactivation commands. (Useful for iMacs and Mac Minis who that would have trouble turning Bluetooth on again without
any input devices.)

### Remote triggers

Most, or all, the listed commands have their own Remote Trigger. (You're welcome to add ones that are missing.)

---

## Troubleshooting

### Notifications not working, or notificator error

Have you granted [Alfred access to controlling bluetooth](#allow-alfred-to-control-bluetooth)? If you still experience issues after granting access, these problems probably stems from the `notificator` binary being blocked by Gatekeeper. We therefore need to allow it to run (remove the quarantine attribute from the bundled binary):

1.  Open workflow folder in Finder by right clicking workflow ([see image](#installation-images)).
2.  Right-click on `notificator` and click 'open' ([see image](#installation-images)).
3.  Confirm open when dialog appears.
4.  This can alternatively be done [using the terminal](#remove-quarantine-using-terminal).

### Error `xcrun: error: invalid active developer path`

If you experience the error `xcrun: error: invalid active developer path`, Command Line Tools is likely not installed properly. More info, as well as instructions on how to install it, can be found here: https://apple.stackexchange.com/a/254381

### Remove quarantine using terminal

Use the following command once in directory:

- Notificator: `xattr -d com.apple.quarantine ./notificator`</br>
  ![How to open directory in Terminal](img/open-in-terminal.png)

### Allow Alfred to control bluetooth

Go to `System Preferences -> Privacy & Security -> Bluetooth` and add the Alfred version you are using (e.g., Alfred 5). If you have already added Alfred, ensure it is turned on.</br>
![Allow bluetooth in System Preferences](img/security_bluetooth.png)

### Why do I need to install blueutil with Homebrew?

Many users with silicon chip macs experienced issues with the local binaries provided in the workflow. It also required manual removal of quarantine for many users, and relied on workflow updates for every new release of `blueutil`. After the implementation of Alfred's new [Resolve Dependecies feature], use of Homebrew installed tools suddenly became a lot more user friendly. I decided the time had come for letting Homebrew manage `blueutil`.

---

## Installation images

(Note: in the second image, the binary should be `notificator`, not `blueutil`.)
!["How to open directory in Finder"](img/open-in-finder.png)
![How to open binary file](img/open-manually.png)

---

## Screenshots

![Screenshot of all options](img/screenshot_bt.png)
![Screenshot of device toggle](img/screenshot_btd.png)

---

## Attribution

- [blueutil](https://github.com/toy/blueutil) binary is used for bluetooth functionality.
- [notificator](https://github.com/vitorgalvao/notificator) binary is used for notifications.
