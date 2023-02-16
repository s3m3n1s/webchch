import os, json
from analyzer.analyzers.analyzer_interface import AnalyzerABC
from hashlib import md5
import subprocess


class WhatWeb(AnalyzerABC):
    def analyze(self, url=None):
        if not os.path.exists('whatweb_scans'):
            os.mkdir('whatweb_scans')
        if os.path.exists('whatweb_scans/{:s}'.format(md5(url.encode()).hexdigest())):
            os.remove('whatweb_scans/{:s}'.format(md5(url.encode()).hexdigest()))

        subprocess.run(["whatweb", url, "--log-json=whatweb_scans/{:s}".format(md5(url.encode()).hexdigest())],
                       stdout=subprocess.PIPE)

        with open('whatweb_scans/' + md5(url.encode()).hexdigest(), 'r') as memo:  # пересоздание json в нужном формате
            res = {url: json.load(memo)}

        with open('whatweb_scans/' + md5(url.encode()).hexdigest(), 'w') as memo:
            json.dump(res, memo)

        return dict(res)

    def get_last_data(self, url=str) -> dict:
        try:
            with open('whatweb_scans/' + md5(url.encode()).hexdigest(), 'r') as memo:
                res = json.load(memo)
                return dict(res)
        except Exception as e:
            return {}
