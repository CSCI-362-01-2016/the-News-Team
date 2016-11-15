#!/usr/bin/env python
from project.youtube_dl import utils

def main():
    print("what" ,calc_percent(128,1024))
def calc_percent(byte_counter, data_len):
    if data_len is None:
        return None
    return float(byte_counter) / float(data_len) * 100.0
