import os
import urllib.request
import urllib.parse
import urllib.error
import urllib.parse
import requests
import platform
import logging as log
from tqdm import tqdm
from shutil import unpack_archive
import subprocess
import re
import datetime
from dateutil.parser import parse as parsedate
import pytz
from dateutil.tz import tzlocal
import shutil


def fn_from_url(url):
    return os.path.basename(urllib.parse.urlparse(url).path)


def download_file(url, dest_path, progress=False):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    if progress:
        log.info('downloading from: %s', url)

    fn = fn_from_url(url)
    full_fn = os.path.join(dest_path, fn)

    if os.path.exists(full_fn):
        log.info('File %s already exists in %s ...' % (fn, dest_path))
    else:
        r = requests.get(url, stream=True)
        total_length = r.headers.get('content-length')
        pg = tqdm(total=int(total_length)) if (
            total_length is not None and progress) else None
        dl = 0
        with open(full_fn, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    if progress and pg:
                        pg.update(len(chunk))
                    f.write(chunk)
                    f.flush()
        if progress and pg:
            pg.close()

    return full_fn


def install_jar_if_needed(path, v='v0.0.1'):
    file_name = 'build-bins.tgz'
    url = 'https://github.com/L1NNA/JARV1S-Kam1n0/releases/download/{}/{}'.format(
        v, file_name)
    bin_file = os.path.join(path, file_name)
    jar = os.path.join(path, 'build-bins', 'kam1n0-server.jar')
    download = True
    if os.path.exists(bin_file):
        u = urllib.request.urlopen(url)
        meta = u.info()
        url_time = meta['Last-Modified']
        url_date = datetime.datetime.strptime(
            url_time, "%a, %d %b %Y %X GMT")
        url_date = pytz.utc.localize(url_date)
        file_time = datetime.datetime.fromtimestamp(
            os.path.getmtime(bin_file), tz=tzlocal())

        if url_date > file_time:
            log.info('Jar file exists but the server has a newer version. {} vs {}'.format(
                url_date, file_time))
            shutil.rmtree(os.path.join(path, 'build-bins'), ignore_errors=True)
            os.remove(bin_file)
            download = True
        else:
            download = False

    if download:
        log.info('Dowloading latest pre-built Kam1n0 jar into {}'.format(path))
        download_file(
            url, path, progress=True)
    if not os.path.exists(bin_file):
        log.error('Failed to download the latest Kam1n0 distribution.')
    else:
        shutil.unpack_archive(bin_file, path)
        if not os.path.exists(jar):
            log.error('Jar downloaded to {} but still not found'.format(path))
    return jar


def install_jdk_if_needed(path, jdk='jdk8u242-b08'):
    version = subprocess.check_output(
        ['java', '-version'], stderr=subprocess.STDOUT)
    pattern = b'\"(\d+\.\d+).*\"'
    val = re.search(pattern, version).groups()[0]
    val = float(val)
    # if val < 9:
    #     return 'java'

    if not os.path.exists(path):
        os.mkdir(path)

    java = {
        'linux': '{}-jre/bin/java',
        'windows': '{}-jre/bin/java.exe',
        'darwin': '{}-jre/bin/java',
    }[platform.system().lower()]
    java = os.path.join(path, java.format(jdk))

    if not os.path.exists(java):
        url = {
            'linux': 'https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u242-b08/OpenJDK8U-jre_x64_linux_hotspot_8u242b08.tar.gz',
            'windows': 'https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u242-b08/OpenJDK8U-jre_x64_windows_hotspot_8u242b08.zip',
            'darwin': 'https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u242-b08/OpenJDK8U-jre_x64_mac_hotspot_8u242b08.tar.gz'
        }[platform.system().lower()]
        log.info(
            'Current version of java is {} (not supported by Ghidra).'.format(val))
        log.info('Downloading OpenJDK from {} to {}'.format(url, path))
        fn = download_file(
            url, path, progress=True)

        unpack_archive(fn, path)
        os.remove(fn)
        if not os.path.exists(java):
            log.error(
                'Java not found even though JDK has been downloaded. Check here %s',
                path
            )
    log.info('using: %s for Kam1n0', java)
    return java
