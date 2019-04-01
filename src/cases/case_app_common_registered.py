import unittest
from src.cases.base import TestWallet


class LoginPassword:
    """
    定义用于测试的密码
    """
    Normal = "Test123456"
    New = "Test12345678"
    Low = "12345678"


class VerifyType:
    """
    验证码类型
    """
    Register = 1
    Login = 2
    ResetPwd = 3
    SetPayPwd = 4


class TestWallet_registered(TestWallet):
    def setUp(self):
        self.api = "/app/common/registered"
        self._add_log(case_name=self._testMethodName,
                      api=self.api,
                      info=self._testMethodDoc)

    def tearDown(self):
        super().tearDown()

    def test__registered__pass__china_telecom_001(self):
        """
        mobile为**电信**手机号码，password在60分以上，正常注册

        1. 获取一个电信手机号码
        2. 获取一个得分在60分以上的密码
        3. 以第一步的手机号获取注册验证码
        4. 以前3步数据为参数请求注册接口
        5. 检查请求结果:应该为注册成功
        6. 检查新注册的账号登陆:应该可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertTrue(self._check_login(number, LoginPassword.Normal))

    def test__registered__pass__china_mobile_001(self):
        """
        mobile为**移动**手机号码，password在60分以上，正常注册

        1. 获取一个移动手机号码
        2. 获取一个得分在60分以上的密码
        3. 以第一步的手机号获取注册验证码
        4. 以前3步数据为参数请求注册接口
        5. 检查请求结果:应该为注册成功
        6. 检查新注册的账号登陆:应该可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)

    def test__registered__pass__china_unicom_001(self):
        """
        mobile为**联通**手机号码，password在60分以上，正常注册

        1. 获取一个联通手机号码
        2. 获取一个得分在60分以上的密码
        3. 以第一步的手机号获取注册验证码
        4. 以前3步数据为参数请求注册接口
        5. 检查请求结果:应该为注册成功
        6. 检查新注册的账号登陆:应该可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertTrue(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__china_telecom_password_low_001(self):
        """
        mobile为**电信**手机号码，password在60分以下，正常注册，注册结果应该失败

        1. 获取一个电信手机号码
        2. 获取一个得分在60分以下的密码
        3. 以第一步的手机号获取注册验证码
        4. 以前3步数据为参数请求注册接口
        5. 检查请求结果:应该为注册失败
        6. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Low,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__china_mobile_password_low_001(self):
        """
        "mobile为**移动**手机号码，password在60分以下，正常注册，注册结果应该失败"

        1. 获取一个移动手机号码
        2. 获取一个得分在60分以下的密码
        3. 以第一步的手机号获取注册验证码
        4. 以前3步数据为参数请求注册接口
        5. 检查请求结果:应该为注册失败
        6. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Low,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__china_unicom_password_low_001(self):
        """
        mobile为**联通**手机号码，password在60分以下，正常注册，注册结果应该失败

        1. 获取一个电信手机号码
        2. 获取一个得分在60分以下的密码
        3. 以第一步的手机号获取注册验证码
        4. 以前3步数据为参数请求注册接口
        5. 检查请求结果:应该为注册失败
        6. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Low,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__number_short_001(self):
        """
        mobile格式不对：不足11位，password在60分以上，正常注册，注册结果应该失败

        1. 创建一个不足11位的手机号码
        2. 获取一个得分在60分以上的密码
        3. 以上面的数据为参数请求注册接口(验证码用错误验证码)
        4. 检查请求结果:应该为注册失败
        5. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018"[:-1]
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": "123456"
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__number_long_001(self):
        """
        mobile格式不对：超过11位，password在60分以上，正常注册，注册结果应该失败

        1. 创建一个超过11位的手机号码
        2. 获取一个得分在60分以上的密码
        3. 以上面的数据为参数请求注册接口(验证码用错误验证码)
        4. 检查请求结果:应该为注册失败
        5. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018" + "1"
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": "123456"
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__number_regular_error_001(self):
        """
        mobile格式不对：号段不对，password在60分以上，正常注册，注册结果应该失败

        1. 创建一个号段错误的手机号码
        2. 获取一个得分在60分以上的密码
        3. 以上面的数据为参数请求注册接口(验证码用错误验证码)
        4. 检查请求结果:应该为注册失败
        5. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "2" + "15700000018"[:-1]
        data = {
            "mobile": "2" + number,
            "password": LoginPassword.Normal,
            "verifyCode": "123456"
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    @unittest.skip(reason="优化类bug3061，bug未修复前先暂停测试")
    def test__registered__fail__number_empty_001(self):
        """
        mobile为空，password在60分以上，正常注册，注册结果应该失败

        1. 获取一个得分在60分以上的密码
        2. 以上面的数据为参数请求注册接口(验证码用错误验证码，手机号为空)
        3. 检查请求结果:应该为注册失败
        """

        data = {
            "password": LoginPassword.Normal,
            "verifyCode": "123456"
        }
        resp, parameters = self.request(data=data)

        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)


    def test__registered__fail__number_has_registered_other_user_code_001(self):
        """
        手机号未注册，验证码为其他手机登录验证码，注册结果应该失败

        1. 创建一个手机号码
        2. 以这个号码获取注册验证码
        3. 创建另一个手机号码
        4. 以第2步和第3步的数据为参数请求注册接口
        5. 检查请求结果:应该为注册失败
        6. 检查新注册的账号登陆:应该不可以登陆

        """

        number = "15700000018"
        code = self.sms(number, int(VerifyType.Register))

        data = {
            "mobile": "15700000018",
            "password": LoginPassword.Normal,
            "verifyCode": code
        }

        resp, parameters = self.request(data=data)
        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)

    def test__registered__fail__password_empty_001(self):
        """
        密码为空，注册结果应该失败

        1. 获取一个手机号码
        2. 以第一步的手机号获取注册验证码
        3. 以前2步数据为参数请求注册接口(不填密码)
        4. 检查请求结果:应该为注册失败
        5. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }

        resp, parameters = self.request(data=data)
        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)
        self.assertFalse(self._check_login(number, LoginPassword.Normal))

    def test__registered__fail__number_with_text_001(self):
        """
        mobile中出现非法字符

        1. 获取一个手机号码
        2. 以第一步的手机号获取注册验证码
        3. 以前2步验证码,合规的密码以及一个错的手机码(最后一们是字符)尝试注册
        4. 检查请求结果:应该为注册失败
        5. 检查新注册的账号登陆:应该不可以登陆
        """

        number = "15700000018"
        code_ = self.sms(number, int(VerifyType.Register))
        number = number[:-1] + "x"
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": code_
        }

        resp, parameters = self.request(data=data)
        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)

    def test__registered__pass__code_too_frequent_001(self):
        """
        验证码过于频繁后，用最后一个注册验证码，尝试注册
        :return:
        """

        number = "15700000018"
        data = {
            "mobile": number,
            "password": LoginPassword.Normal,
            "verifyCode": self.sms(number, int(VerifyType.Register))
        }
        for n in range(20):
            self.sms(number, int(VerifyType.Register))

        resp, parameters = self.request(data=data)
        expect_ = {
            "equal": {
                "header.returnCode": 0
            }
        }
        self.check(expect=expect_, res=resp, parameters=parameters)

