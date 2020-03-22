# Alfred Workflow: Bluetooth Controller
A powerful toolkit for managing your bluetooth connections.

# Installation
## Summary
Install [blueutil](http://www.frederikseiffert.de/blueutil/), Python 3, and open alfred configuration file!

## Instructions
1. Install [blueutil](http://www.frederikseiffert.de/blueutil/): 

Using package manager [Homebrew](https://brew.sh/):

```sh
# install
brew install blueutil

# update
brew update
brew upgrade blueutil

# uninstall
brew remove blueutil
```

Using package manager [MacPorts](https://www.macports.org/):

```sh
# install
port install blueutil

# update
port selfupdate
port upgrade blueutil

# uninstall
port uninstall blueutil
```

2. Verify that Python 3 installed, install if otherwise.
```sh
python3 --version
```


Install using package manager [Homebrew](https://brew.sh/):

```sh
# install
brew install python3

# update
brew update
brew upgrade python3

# uninstall
brew remove python3
```


Install using package manager [MacPorts](https://www.macports.org/):

```sh
# install
port install python3

# update
port selfupdate
port upgrade python3

# uninstall
port uninstall python3
```


3. Open alfred installation file!


# Usage

![usage snippet](alfred_bluetooth_long.gif "Usage snippet")

## Manage bluetooth
- Toggle bluetooth on and off: `bt`
- Turn bluetooth on: `bton`
- Turn bluetooth off: `btoff`

## Toggle device connections
- Connect/disconnect from device: `btd` + `device name`
- By typing an argument, the workflow will automatically search through all devices prevously paired with the computer.

## Manage favorite device
- Set favorite device: `btsetfavorite` + `device name`
- Toggle connection to favorite device: `btx`
