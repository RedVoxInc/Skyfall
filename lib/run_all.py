"""
Runs all skyfall examples
"""

import lib.skyfall_tdr_rpd as tdr
import lib.skyfall_tfr_rpd as tfr
import lib.skyfall_station_specs as sfp
import lib.skyfall_ensonify as sfe
import lib.skyfall_loc_rpd as sfl
import lib.skyfall_spinning as sfs
import lib.skyfall_gravity as sfg


if __name__ == "__main__":
    print("RedPandas Example: Skyfall")
    print("\nTime domain representation: skyfall_tdr_rpd.py")
    tdr.main()
    print("\nTime frequency representation: skyfall_tfr_rpd.py")
    tfr.main()
    print("\nStation details: skyfall_station_specs.py")
    sfp.main()
    print("\nSonification: skyfall_ensonify.py")
    sfe.main()
    print("\nLocation: skyfall_loc_rpd.py")
    sfl.main()
    print("\nAcceleration and gravity: skyfall_gravity.py")
    sfg.main()
    print("\nRotation: skyfall_spinning.py")
    sfs.main()
