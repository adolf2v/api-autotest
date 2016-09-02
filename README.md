# api-autotest
将测试用例格式化为一定的xml文件
xml格式如下
<testcase class="testcase" name="登录接口">
    <testcase>
        <api>url</api>
        <desc>正常登录</desc>
        <data>{"_xsrf": "2|084224b9|da57b7cd758f539cd1505da579a375a7|1433236535","identity": "xxxxx","password":
            "xxxx", "autoLogin": "on", "utype": 1}
        </data>
        <method>post</method>
        <assert1>
            <status>200</status>
            <retcode>0</retcode>
            <content id="text">登录成功!</content>
        </assert1>
    </testcase>
</testcase>
通过读取xml文件是实施在自动化测试


