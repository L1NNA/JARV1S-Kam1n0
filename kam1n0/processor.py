from kam1n0.dependencies import install_jar_if_needed, install_jdk_if_needed
import os
from pathlib import Path
from subprocess import Popen, PIPE, STDOUT
from shutil import rmtree
import sys
import json
import errno
from tempfile import TemporaryFile
import logging as log

NULL_FILE = open(os.devnull, 'w')
home = os.path.join(
    str(Path.home()), '.jarv1s-kam1n0'
)
jar = install_jar_if_needed(
    home
)
java = install_jdk_if_needed(
    home
)


def process_folder(
        folder,
        model='asmbin2vec',
        result_file='similarity.txt',
        load=False,
        cleanUp=False,
        show_stdout=False):
    folder = os.path.abspath(folder)
    cmd = [java,
           '-jar', jar, '--b',
           '-res={}'.format(result_file),
           '-md={}'.format(model),
           '-dir={}'.format(folder)]
    print(cmd)
    out_stream = STDOUT
    out = []
    p = Popen(cmd, stdout=PIPE, stderr=STDOUT)
    if show_stdout:
        while p.poll() is None:
            l = p.stdout.readline().decode('utf-8')  # This blocks until it receives a newline.
            print(l, end='')
            out.append(l)
        out = ''.join(out)
    else:
        out, _ = p.communicate()
    if os.path.exists(result_file):
        if load:
            with open(result_file, 'r') as o_file:
                return json.load(o_file), out
        else:
            return result_file, out
    else:
        log.info('Failed to process.')
        return None, out
