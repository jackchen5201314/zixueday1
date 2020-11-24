class Register:
    """
    注册页面po
    """

    def __init__(self, dr):
        self.dr = dr

    def register(self):
        """
        输入内容
        点击下拉框

        return
        """
        self.dr.find_element_by_id("corp_name").send_keys("12333")
        self.dr.find_element_by_id("manager_name").send_keys("jc")
        return True
