def get_choises_keys(struct: tuple) -> set:
    keys = set()
    for kind in struct:
        if isinstance(kind[1], tuple):
            for inner_kind in kind[1]:
                keys.add(inner_kind[0])
        else:
            keys.add(kind[0])
    return keys
