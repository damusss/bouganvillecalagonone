CONFIG = {
    "home.html": [["apartment_slideshows", {"APARTM_VARIABLE": "apartment"}]],
    "apartment.html": [["apartment_slideshows", {"APARTM_VARIABLE": "apartm"}]],
}


def resolve_mod(mod_name, conf):
    with open(f"js_smart_syntax/{mod_name}.js", "r") as file:
        content = file.read()
        for confkey, confval in conf.items():
            content = content.replace(confkey, confval)
        lines = content.splitlines()
        conf_line = lines[0]
        content = "\n".join(lines[1:])
        content = content.replace("// <>", "")
        conf_split = conf_line.removeprefix("//").strip().split(";")
        for conf_replace in conf_split:
            replace, replace_to = conf_replace.split("->")
            content = content.replace(replace, "{{" + replace_to + "}}")

    return content


def mod_file(file_name, mod_name, conf):
    with open(f"sito/templates/sito/{file_name}", "r") as file:
        content = file.read()
        everything_before, after = content.split(f"// smart-start:{mod_name}")
        _, everything_after = after.split(f"// smart-end:{mod_name}")
        mod = resolve_mod(mod_name, conf)
    with open(f"sito/templates/sito/{file_name}", "w") as file:
        file.write(
            everything_before
            + f"// smart-start:{mod_name}\n"
            + mod
            + f"\n// smart-end:{mod_name}"
            + everything_after
        )


for prod_file, mod_names in CONFIG.items():
    for name, conf in mod_names:
        mod_file(prod_file, name, conf)
