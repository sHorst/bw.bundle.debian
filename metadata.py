@metadata_processor
def add_check_mk_tags(metadata):
    if node.has_bundle('check_mk_agent'):
        metadata.setdefault('check_mk', {})
        metadata['check_mk'].setdefault('tags', [])
        metadata['check_mk']['tags'] += ['deb', ]

    return metadata, DONE
