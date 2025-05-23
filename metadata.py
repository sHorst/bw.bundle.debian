global node

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
            'cron-apt': {'installed': False},

            'unattended-upgrades': {'installed': True},
            'apt-listchanges': {'installed': True},
            'mailutils': {'installed': True},

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
    13: 'trixie',
    14: 'forky',
}

# set release_name
defaults['debian'] = {
    'release_name': release_names.get(node.os_version[0], 'jessie'),
    'init': 'systemd' if node.os_version[0] > 8 else 'init5',
    'unattended_upgrades': {
        'enabled': True,
        'pkg_blacklist': [],
        'mail_receiver': 'root',
        'mail_report': 'on-error',
    }
}
