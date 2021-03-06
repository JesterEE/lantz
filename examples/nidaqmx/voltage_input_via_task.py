#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lantz.drivers.ni.daqmx import AnalogInputTask
from lantz.drivers.ni.daqmx import VoltageInputChannel

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Print debug information')
    parser.add_argument('phys_channel', type=str,
                        help='Physical channel')
    args = parser.parse_args()

    if args.debug:
        import lantz.log
        lantz.log.log_to_screen(lantz.log.DEBUG)

    task = AnalogInputTask()
    task.add_channel(VoltageInputChannel(args.phys_channel))
    task.start()
    print(task.read_scalar())
    task.stop()
