# This code is so boring.nvim
Launches a video with subway surf gameplay in nvim

# Usage
## NVim commands
- ```:ThisCodeIsSoBoring``` - start default subway surf gameplay video in the current window. 
- ```":ThisCodeIsSoBoring {video}``` - start your subway surf gameplay video in the current window, ```video``` is url or path on your computer.

- ```:SetThisCodeIsSoBoringVideo {video}``` - set default subway surf gameplay video, ```video``` is url or path on your computer.

# Install
## Requirements
For fll install methods you need to have nvim, python3 and  [pynvim](https://github.com/neovim/pynvim)

## Manual install
1. Clone this repo
2. Install python requirements:
```pip install --user -r requirements.txt```
3. Add plugin folder in ```runtimepath```
4. Run ```:UpdateRemotePlugins``` in nvim
5. Restart nvim

