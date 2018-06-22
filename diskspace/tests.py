#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import unittest
import diskspace
import os

class TestDiskSpaceMethods(unittest.TestCase):
    def test_bytes_to_readable(self):
        blocks = 40
        self.assertEqual(diskspace.bytes_to_readable(blocks), '20.00Kb')

    def test_zero_bytes_to_readable(self):
        blocks = 0
        self.assertEqual(diskspace.bytes_to_readable(blocks), '0.00B')

    def test_kbytes_to_readable(self):
        blocks = 1024
        self.assertEqual(diskspace.bytes_to_readable(blocks), '512.00Kb') 

    def test_mbytes_to_readable(self):
        blocks = 1048576
        self.assertEqual(diskspace.bytes_to_readable(blocks), '512.00Mb')

    def test_gbytes_to_readable(self):
        blocks = 1073741824
        self.assertEqual(diskspace.bytes_to_readable(blocks), '512.00Gb')

    def test_subprocess_check_output(self):
        command = "du -d 1 /home/joao/Documentos/UnB/6º_semestre/Tecprog/05--joaovitor3/diskspace"
        self.assertEqual(diskspace.subprocess_check_output(command),"16\t"+\
                        "/home/joao/Documentos/UnB/6º_semestre/Tecprog/05--joaovitor3/diskspace"+\
                        "/__pycache__"+"\n"+"40\t"+"/home/joao/Documentos/UnB/6º_semestre/Tecprog/05--joaovitor3/diskspace"+'\n')

if __name__ == '__main__':
    unittest.main()