# Alfred Workflow: Bluetooth Controller
A powerful toolkit for managing your bluetooth connections. Includes Remote Trigger, to manage your Bluetooth devices on the big screen.

### Installation

Download the [Alfred workflow](https://github.com/vegardinho/alfred_bluetooth_controller/releases/latest) and double-click to install!

## Usage

![usage snippet](alfred_bluetooth_long.gif "Usage snippet")


### Manage bluetooth
- Turn bluetooth on: `bton`
- Turn bluetooth off: `btoff`
- Reset (disable, wait 1.5 seconds, enable: `btr`

### Toggle device connections
- Connect/disconnect from device: `btd` + `device name`
- By typing an argument, the workflow will automatically search through all devices prevously paired with the computer.

### Manage favorite device
- Set favorite device: `btsetfavorite` + `device name`
- Connect to favorite device with hotkey (`cmd-ctr-option-x` by default)

### Pair new device
- `btp` + `device name`
- Wait 5 seconds for results to show up

### Status
- See status of bluetooth connection and paired devices: `btstatus`

### Safe mode
Set environment variable `confirm` in workflow to `true` if you want to force user confirmation on toggle and deactivation commands. (Useful for iMacs and Mac Minis who that would have trouble turning Bluetooth on again without any input devices.)

_All the listed commands have their own Remote Trigger._

## Troubleshooting

If you get errors when using the workflow referring to not being able to use `blueutil` as it cannot be checked, you will need to manually remove the quarantine attribute from the bundled binary.
This can be done like so: `xattr -d com.apple.quarantine /Users/User Name/Library/Application\ Support/Alfred/Alfred.alfredpreferences/workflows/user.workflow.*/blueutil`
(Substitute User Name with your OSX username).
