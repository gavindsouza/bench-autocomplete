## AutoCompletions for the Bench CLI

Started this project because I wasn't happy with `completion.sh` that Bench ships with, or Click's auto completions due to how [Frappe](https://frappeframework.com), [Bench](https://github.com/frappe/bench) & external apps' commands work together. Currently we are working only on `zsh` completions. Mostly because it helps vastly during development.

### Installation

Just copy pasting the following block in your zsh terminal and restarting your session should do the trick:

```sh
git clone https://github.com/gavindsouza/bench-autocomplete ~/.bench-autocomplete
cp ~/.bench-autocomplete/zsh/_bench /usr/local/share/zsh/site-functions/_bench
echo 'rm -f ~/.zcompdump; compinit' >> ~/.zshrc
```
