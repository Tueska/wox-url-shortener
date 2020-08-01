# -*- coding: utf-8 -*-

import pyperclip
import pyshorteners
from wox import Wox

class URLShort(Wox):

    def copyToClipboard(self, value):
        pyperclip.copy(value)

    def query(self, query):
        shortURL = ''
        s = pyshorteners.Shortener(domain='https://0x0.st')
        shortURL = 'URL' if not query else s.nullpointer.short(query)

        results = []

        results.append({
            "Title": shortURL,
            "SubTitle": "Long: \"{}\"".format(query),
            "IcoPath":"icon.png",
            "JsonRPCAction":{
                "method": "copyToClipboard",
                "parameters":[shortURL.strip()],
                "dontHideAfterAction":False
            }
        })
        
        return results

if __name__ == "__main__":
    URLShort()
