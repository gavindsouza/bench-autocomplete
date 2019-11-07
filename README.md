# ZSH Completions for (frappe bench)[https://github.com/frappe/bench]

## Installation

Add the following line to your `.zshrc`

```sh
rm -f ~/.zcompdump; compinit
```

Clone this repo and cd into it

```sh
git clone https://github.com/gavindsouza/bench-autocomplete && cd bench-auto-complete
```

Copy the `_bench.old` to `/usr/local/share/zsh/site-functions/_bench` (on macOS)

```sh
cp zsh/_bench.old /usr/local/share/zsh/site-functions/_bench
```

You can also create a symlink
