import os, json
from analyzer.analyzers.analyzer_interface import AnalyzerABC
import wad
from hashlib import md5


class Wad(AnalyzerABC):
    def analyze(self, url=None):
        results = wad.detection.Detector().detect_multiple([url])
        res = json.loads(wad.JSONOutput().retrieve(results=results))
        if not os.path.exists('wad_scans'):
            os.mkdir('wad_scans')
        with open('wad_scans/' + md5(url.encode()).hexdigest(), 'w') as memo:
            json.dump(res, memo)
        return res

    def get_last_data(self, url=str) -> dict:
        try:
            with open('wad_scans/' + md5(url.encode()).hexdigest(), 'r') as memo:
                res = json.load(memo)
                return dict(res)
        except Exception as e:
            return {}
