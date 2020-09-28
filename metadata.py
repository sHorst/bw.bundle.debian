@metadata_reactor
def add_check_mk_tags(metadata):
    if not node.has_bundle("check_mk_agent"):
        raise DoNotRunAgain

    return {
        'check_mk': {
            'tags': {
                'dist': 'deb',
            }
        }
    }


@metadata_reactor
def add_apt_packages(metadata):
    if not node.has_bundle("apt"):
        raise DoNotRunAgain

    return {
        'apt': {
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
    }
