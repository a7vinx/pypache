import argparse


class HttpServlet(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        # 从命令行获取数据路径,默认 MINIST_data
        parser.add_argument('--pipe_name', type=str,
                            help='parameter pipe_name is required')
        parser.add_argument('--data', type=str,
                            help='parameter data is required')
        self.data = eval(parser.parse_args().data)
        self.pipe = open(parser.parse_args().pipe_name, 'w')
        self.parameters = self.data['params']
        self.cookie = self.data['cookie']
        self.reqType = self.data['reqType']
        self.__run()
        self.pipe.close()

    def __run(self):
        if self.reqType == 'POST':
            self._doPOST(self.printToWeb)
        else:
            self._doGET(self.printToWeb)

    def getCookie(self):
        return self.cookie

    def getParameter(self, param):
        if param in self.parameters:
            return self.parameters[param]
        return None

    def getParameters(self):
        return self.parameters

    def getRequestType(self):
        return self.reqType

    def setContentType(self, content_type):
        self.pipe.write("command:" + "setContentType(" + str(content_type) + ")")
        pass

    def setCookie(self, set_cookie):
        self.pipe.write("command:" + "setCookie(" + str(set_cookie) + ")")
        pass

    def setResponseCode(self, code):
        self.pipe.write("command:" + "setCode(" + str(code) + ")")
        pass

    def printToWeb(self, text):
        if text is None:
            text = ''
        self.pipe.write("out:" + str(text) + "\n")
        pass

    def _doGET(self, echo):
        # 默认禁止get方法
        self.setResponseCode(501)

    def _doPOST(self, echo):
        # 默认禁止get方法
        self.setResponseCode(501)
        pass
