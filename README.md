# This code is so boring.nvim
Launches a video with subway surf gameplay in nvim

# Usage
## NVim commands
- ```:ThisCodeIsSoBoring``` - start default subway surf gameplay video in the current window. 
- ```":ThisCodeIsSoBoring {video}``` - start your subway surf gameplay video in the current window, ```video``` is url or path on your computer.

- ```:SetThisCodeIsSoBoringVideo {video}``` - set default subway surf gameplay video, ```video``` is url or path on your computer.

# Install
## Requirements
For all install methods you need to have nvim, python3 and  [pynvim](https://github.com/neovim/pynvim)

## Manual install
1. Clone this repo
2. Install python requirements:
```pip install --user -r requirements.txt```
3. Add plugin folder in ```runtimepath```
4. Run ```:UpdateRemotePlugins``` in nvim
5. Restart nvim

## Install using [lazy](https://github.com/folke/lazy.nvim)
1. Add this lines in your lazy section of init.lua:
```lua
{
  "INoorik/ThisCodeIsSoBoring.nvim",
    keys = {
    },
    config = function()
      vim.api.nvim_eval('UpdateRemotePlugins')
      vim.api.nvim_eval('!pip install --user -r requirements.txt')
    end,
}
```
3. Run ```:Lazy install``` in nvim
4. Restart nvim

## Install using [packer.nvim](https://github.com/wbthomason/packer.nvim)
1. Add this lines in your packer section
```lua
use { 'INoorik/ThisCodeIsSoBoring.nvim', run={'pip install --user -r requirements.txt', ':UpdateRemotePlugins'}}
```
2. run ```:PackerInstall``` in nvim
3. Restart nvim

## Install using [vim-plug](https://github.com/junegunn/vim-plug)
1. Add this lines in your vim-plug section
```vim
Plug 'INoorik/ThisCodeIsSoBoring.nvim', {'do': ':UpdateRemotePlugins \|!pip install --user -r requirements.txt'}
```
2. Run ```:PlugInstall``` in nvim
3. Restart nvim
