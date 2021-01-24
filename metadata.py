defaults = {}

# if we use check_mk, add the dist tag
if node.has_bundle("check_mk_agent"):
    defaults['check_mk'] = {
        'tags': {
            'dist': 'deb',
        }
    }

# if we install apt, install default packages
if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'cron-apt': {'installed': True},
            'curl': {'installed': True},
            'ca-certificates': {'installed': True},
            'git': {'installed': True},

            "grep": {'installed': True},
            "gzip": {'installed': True},
            "hostname": {'installed': True},
            "htop": {'installed': True},
            'tmux': {'installed': True},

            'vim': {'installed': True},
            'zsh': {'installed': True},
            'unzip': {'installed': True},
        }
    }

release_names = {
    8: 'jessie',
    9: 'stretch',
    10: 'buster',
    11: 'bullseye',
    12: 'bookworm',
}

# set release_name
defaults['debian'] = {
    'release_name': release_names.get(node.os_version[0], 'jessie'),
}
