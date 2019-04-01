import unittest
import requests
from src.utils import config
from src.utils import url
import copy
import logging
import jmespath
import json


CONCURRENT_RUN = config.get("run.concurrent")
logger = logging.getLogger(config.get("project.name"))


_TEST_CASES = []


class TestWallet(unittest.TestCase):
    """
    封装过的测试用例基类，其中实现当前测试项目中测试用例会用到的基础函数或会共函数、数据等
    """
    @classmethod
    def setUpClass(cls):
        cls.api = ""
        cls.host = config.get("host", default=config.get("default_host"))
        cls.default_parameter = config.get("default_parameter", {})
        cls.default_header = config.get("default_header", {})

    @staticmethod
    def register_case(case):
        global _TEST_CASES
        if isinstance(case, str):
            if case not in _TEST_CASES:
                _TEST_CASES.append(case)
        elif isinstance(case, TestWallet):
            _TEST_CASES.append(case.__name__)

    @staticmethod
    def cases() -> list:
        return copy.deepcopy(_TEST_CASES)

    @staticmethod
    def _add_log(case_name, api: str = None, info: str = None):
        logger.info("\n\n测试用例：{case_name}开始\n接口：{api}\n信息：\n{info}\n\n".format(
            case_name=case_name, api=api, info=info))

    def check(self, expect: dict, res: dict, parameters: dict = None):
        equal = expect.get("equal", {})
        notequal = expect.get("notequal", {})
        exists = expect.get("exists", {})

        message = json.dumps(
            {"send": parameters, "response": res},
            ensure_ascii=False, indent=4)
        logger.info(msg=message)

        # check exists
        for key in exists:
            msg = "期望存在的关键字“{key}”在结果中未找到。\n\n数据:\n{message}\n".format(key=key, message=message)
            self.assertIsNotNone(jmespath.search(key, res), msg)

        # check equal
        for key in equal:
            value = jmespath.search(key, res)
            msg = "需要检查类型的关键字“{key}={value}”在结果中未找到。\n\n数据:\n{message}\n".format(
                key=key, value=equal[key], message=message)
            self.assertIsNotNone(value, msg)

            expect_value = equal[key]
            if isinstance(expect_value, list):
                msg = "期望实际值在列表 {expect} 中的返回值 {key}，实际值 {actual} 不在列表中。\n\n数据:\n{message}\n".format(
                    key=key, expect=expect_value, actual=value, message=message)
                self.assertIn(value, expect_value, msg=msg)
            else:
                msg = "期望相等值关键字“{key}的值{expect}与返回值不相等：{actual}。\n\n数据:\n{message}\n".format(
                    key=key, expect=expect_value, actual=value, message=message)
                self.assertEqual(value, expect_value, msg=msg)

        # check notequal
        for key in notequal:
            item = jmespath.search(key, res)
            msg = "需要检查类型的关键字“{key}!={value}”在结果中未找到。\n\n数据:\n{message}\n".format(
                key=key, value=notequal[key], message=message)
            self.assertIsNotNone(item, msg=msg)

            expect_value = notequal[key]
            if isinstance(expect_value, list):
                msg = "期望实际值不在列表 {expect} 中的返回值 {key}，实际值 {actual} 在列表中。\n\n数据:\n{message}\n".format(
                    key=key, expect=expect_value, actual=item, message=message)
                self.assertNotIn(item, expect_value, msg=msg)
            else:
                msg = "期望不相等值关键字“{key}的值与返回值相等：{value}。\n\n数据:\n{message}\n".format(
                    key=key, value=item, message=message)
                self.assertNotEqual(item, expect_value, msg=msg)

    def prepare_data(self, api: str = None, data: dict = None, headers: dict = None):
        headers_, data_ = headers or {}, data or {}
        headers_.update(self.default_header)
        data_.update(self.default_parameter)

        logger.info(data_)
        return url(self.host, api or self.api), data_, headers_

    @classmethod
    def _request(cls, api: str, **kwargs) -> (dict, dict):
        parameters = {
            "url": url(cls.host, api),
            "headers": cls.default_header,
            "data": cls.default_parameter
        }

        kwgs = dict()
        for key in kwargs:
            if kwargs[key] is not None:
                kwgs[key] = kwargs[key]
        parameters.update(kwgs)
        response = requests.post(**parameters).json()
        return response, (copy.deepcopy(parameters) if "files" not in parameters else {})

    def request(self, api: str = None, **kwargs) -> (dict, dict):
        return self._request(api=api or self.api, **kwargs)
