@metadata_processor
def add_check_mk_tags(metadata):
    if node.has_bundle('check_mk_agent'):
        metadata.setdefault('check_mk', {})
        metadata['check_mk'].setdefault('tags', {})
        metadata['check_mk']['tags']['dist'] = 'deb'

    return metadata, DONE


@metadata_processor
def add_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        for package in ['cron-apt', 'curl', 'ca-certificates', 'git',
                "grep", "gzip", "hostname", "htop", 'tmux',
                'vim', 'zsh', 'unzip']:

            metadata['apt']['packages'][package] = {'installed': True}

    return metadata, DONE
