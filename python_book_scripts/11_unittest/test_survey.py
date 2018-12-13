import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):#测试用例执行前运行
        question = "What language did you first learn to speak?"
        self.responses = ['English','Spanish','Mandarin']
        self.my_survey = AnonymousSurvey(question)


    def tearDown(self):  # 测试用例执行后运行
        print('z')

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])

        self.assertIn('English',self.my_survey.response)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""

        for language in self.responses:
            self.my_survey.store_response(language)
        for language in self.responses:
            self.assertIn(language,self.my_survey.response)

if __name__ == '__main__':
    unittest.main()