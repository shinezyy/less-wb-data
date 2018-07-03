import common as c

keys = [
        'system.switch_cpus.phyRegFilenumShortLifeIntReg',
        'system.switch_cpus.phyRegFilenumShortLifeCCReg',
        'system.switch_cpus.int_regfile_writes',
        'system.switch_cpus.cc_regfile_writes',
        ]

path = '/ramdisk/zyy/gem5_run/results/short_life_reg_2/gcc/stats.txt'

print(c.extract_x_from_file(keys, path))
