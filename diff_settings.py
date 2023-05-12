def apply(config, args):
    config["baseimg"] = "baserom.us.z64"
    config["myimg"] = "build/mickey.us.z64"
    config["mapfile"] = "build/mickey.us.map"
    config["source_directories"] = ["src"]
    config["show_line_numbers_default"] = True
    config["expected_dir"] = "expected/"
