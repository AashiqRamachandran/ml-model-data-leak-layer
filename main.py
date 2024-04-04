from credsweeper import __main__
from argparse import Namespace
import json


def lambda_handler(log_line):
    with open("/tmp/log_data.json", "w") as f:
        json.dump(log_line, f, indent=4)

    namespace_object = Namespace(
        api_validation=False,
        banner=None,
        config_path=None,
        denylist_path=None,
        depth=0,
        diff_path=None,
        export_config=None,
        export_log_config=None,
        find_by_ext=False,
        jobs=1,
        json_filename='/tmp/output.json',
        ml_threshold="medium",
        log='WARNING',
        log_config_path=None,
        ml_batch_size=16,
        path=['/tmp/log_data.json'],
        rule_path=None,
        size_limit=None,
        skip_ignored=False,
        xlsx_filename=None)

    __main__.main(namespace_object)

    response = json.loads(
        open("/tmp/output.json").read()
    )
    return response