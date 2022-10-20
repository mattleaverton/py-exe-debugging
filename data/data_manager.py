"""

"""
import glob
import os
import importlib


def placeholder_baked_good(confection: str) -> str:
    """ Test mode - find and return a test baked good """
    # import code
    # code.interact(local=locals())
    baked_good = importlib.import_module('library.test_data')
    return baked_good.TEST_STRING.format(confection)


def get_baked_good(target_confection: str, test_mode: bool = False) -> str:
    """ Find and return a baked good - real or test version depending on the flag """
    if test_mode:
        try:
            return placeholder_baked_good(target_confection)
        except ModuleNotFoundError:
            return f"Crusty Test {target_confection}"
    else:
        # Search for an image file and return info about it if it exists
        confections = glob.glob("data/*.jpg")
        # import code
        # code.interact(local=locals())
        ret_info = f"Stale {target_confection}"
        if len(confections) >= 1:
            if os.path.exists(os.path.abspath(confections[0])):
                ret_info = f"{confections[0]} - {os.path.getsize(os.path.abspath(confections[0]))} bytes"
        return ret_info
