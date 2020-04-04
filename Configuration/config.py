"""Module for configuring the application.

The configuration is read from a YAML file and saved in a module-global
variable.

```python
import ema.config

# Load configuration file
ema.config.load(path)

# View the configuration
print(ema.config.value)
```
"""
import yaml

value = {} # Global var, not constant

def load(config_path):
    """Loads a configuration file into a module-global variable.

    The module-global variable is a dict named `value`. If several files are
    loaded sequentially, the dict is updated (not overwritten).

    Args:
        config_path (str): path of the YAML configuration file.
    """
    with open(config_path, 'r') as config_file:
        value.update(yaml.load(config_file, Loader=yaml.FullLoader))
