global node

pkg_apt = {
    # remove unused packages
    'nano': {
        "installed": False,
    },
}

if node.metadata.get('debian', {}).get('unattended_upgrades', {}).get('enabled', False):
    unattended_upgrades_cfg  = node.metadata.get('debian', {}).get('unattended_upgrades', {})

    files = {
        '/etc/apt/apt.conf.d/52unattended-upgrades-local': {
            'source': 'etc/apt/apt.conf.d/52unattended-upgrades-local.j2',
            'content_type': 'jinja2',
            'context': {
                'pkg_blacklist': unattended_upgrades_cfg.get('pkg_blacklist'),
                'mail_report': unattended_upgrades_cfg.get('mail_report'),
                'mail_receiver': unattended_upgrades_cfg.get('mail_receiver'),
            },
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
        },
        '/etc/apt/apt.conf.d/20auto-upgrades': {
            'source': 'etc/apt/apt.conf.d/20auto-upgrades.j2',
            'content_type': 'jinja2',
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
        },
    }
