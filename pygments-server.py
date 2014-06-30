#! /usr/bin/env python
import sys
import cubi.engine as engine
import cubi.logger as logger
import cubi.params as params
from cubi.engine import Servant;

from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments import highlight

class PygmentServant(Servant):

    @params.extract_args
    def highlight(self, lang, code):

        logger.get_logger().debug("highlight: %s %s", lang, code)

        lexer = get_lexer_by_name(lang)
        fmter = HtmlFormatter(nowrap=True)

        lexer.encoding = 'ascii'
        fmter.encoding = 'ascii'

        html = highlight(code, lexer, fmter)

        result = {}
        result['data'] = html;
        return result

if __name__ == '__main__':

    logger.enable_debug_log()

    endp = "pygments@tcp::2016"
    setting = {}
    setting['debug'] = True
    setting['endpoint'] = endp
    engine.make_easy_engine('pygments', PygmentServant, setting).serve_forever()
