import time


import pytest
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common import keys

from pageObjects.LoginPage import Login
import webbrowser
from datetime import date
from pynput.keyboard import Controller,Key
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


Keyboard = Controller()



#
# class Test_001_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "contentadmin2"
#     password = "-mF9SF^g}{&S1O"
#
#
#     def test_homePageTitle(self,setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#         self.lp = Login(self.driver)
#         try:
#             self.lp.setUserName(self.username)
#             print("Username is Entered")
#         except NoSuchElementException:
#             print("username textbox is not found")
#
#         try:
#             self.lp.ClickNext()
#             print("Next button is found and clicked")
#         except NoSuchElementException:
#             print("Next button is not found")
#
#         try:
#             self.lp.setPassword(self.password)
#             print("password id entered")
#         except NoSuchElementException:
#             print("password textbox is not found")
#
#         try:
#             self.lp.ClickSubmit()
#             print("Submit button is found and clicked")
#         except NoSuchElementException:
#             print("Submit button is not found and clicked")
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         try:
#             self.lp.Click_Course()
#             print("Click courses button is clicked")
#         except NoSuchElementException:
#             print("Click courses button is not found")
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         try:
#             self.lp.Click_View_all_past_courses()
#             print("View_all_past_courses button is clicked")
#         except NoSuchElementException:
#             print("View_all_past_courses button is not found")
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         try:
#             self.lp.Click_QA_Main_sec1()
#             print("QA main Section1 is clicked")
#         except NoSuchElementException:
#             print("QA main Section1 is not found")
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             assert True
#         else:
#             assert False
#
#         try:
#             self.lp.Click_turn_edit_on()
#             print("turn editing on button is clicked")
#         except NoSuchElementException:
#             print("turn editing on button is not found")
#         time.sleep(3)
#         try:
#             self.lp.Select_Quiz()
#             print("Quiz is selected")
#         except NoSuchElementException:
#             print("Quiz is not selected")
#         time.sleep(3)
#         try:
#             self.lp.Add_assignment_name()
#             print("Assignment name is Added")
#         except NoSuchElementException:
#             print("Assignment name is not added")
#         time.sleep(3)
#
#         try:
#             self.lp.Add_iframe()
#             print("Quiz Introduction is Added")
#         except NoSuchElementException:
#             print("Quiz Introduction is not Added")
#         time.sleep(3)
#         self.driver.switch_to.default_content()
#         time.sleep(3)
#         try:
#             self.lp.Required_password()
#             print("Password is removed")
#         except NoSuchElementException:
#             print("Password textbox is not found")
#         time.sleep(10)
#         try:
#             self.lp.Save_Display()
#             print("Save and Display Button is Clicked")
#         except NoSuchElementException:
#             print("Save and Display button is not found")
#         time.sleep(3)
#         try:
#             self.lp.click_edit_quiz_button()
#             print("Edit quiz button is clicked")
#         except NoSuchElementException:
#             print("Edit quiz button is not found")
#         time.sleep(1)
#         try:
#             self.lp.click_add_a_question()
#             print("Add question button is clicked")
#         except NoSuchElementException:
#             print("Add Question button is not found")
#         time.sleep(1)
#         try:
#             self.lp.click_essay_radiobutton()
#             print("Essay radio button is selected")
#         except NoSuchElementException:
#             print("Essay radio button is not found")
#
#         time.sleep(1)
#         try:
#             self.lp.click_next_button()
#             print("Next button is Clicked")
#         except NoSuchElementException:
#             print("Next button is not found")
#         time.sleep(3)
#         try:
#             self.lp.set_question_name()
#             print("Question name is Added")
#         except NoSuchElementException:
#             print("Question name textbox is not found")
#         time.sleep(3)
#         try:
#             self.lp.Add_iframe_question_text()
#             print("Question text is Entered")
#         except NoSuchElementException:
#             print("Question text Frame is not found")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.set_marks()
#             print("Marks is Set")
#             print("\n Save button is found and clicked")
#         except NoSuchElementException:
#             print("Marks box is not found")
#             print("\n Save button is not found")
#         try:
#             self.lp.click_add_a_question()
#             print("Add question button is clicked")
#         except NoSuchElementException:
#             print("Add Question button is not found")
#         try:
#             self.lp.clickmcqradiobutton()
#             print("MCQ radio button is selected")
#         except NoSuchElementException:
#             print("\n MCQ radio button is not found")
#         try:
#             self.lp.click_next_button()
#             print("Next button is Clicked")
#         except NoSuchElementException:
#             print("Next button is not found")
#         try:
#             self.lp.click_mcq_question_name()
#             print("MCQ Question name is entered")
#         except NoSuchElementException:
#             print("MCQ Question name is not found")
#         try:
#             self.lp.Add_mcq_iframe_question_text()
#             print("MCQ question text is Entered")
#         except NoSuchElementException:
#             print("MCQ question text frame is not found")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.set_mcq_marks()
#             print("MCQ marks is Entered")
#         except NoSuchElementException:
#             print("MCQ Marks box is not found")
#         try:
#             self.lp.Add_choice1()
#             print("Choice 1 is added")
#         except NoSuchElementException:
#             print("choice 1 is not selected")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.select_Choice1_marks()
#             print("Choice 1 marks is added")
#         except NoSuchElementException:
#             print("Marks texbox is not found")
#         try:
#             self.lp.Add_choice2()
#             print("Choice 2 is added")
#         except NoSuchElementException:
#             print("choice 2 is not selected")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.Add_choice3()
#             print("Choice 3 is added")
#         except NoSuchElementException:
#             print("choice 3 is not selected")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.Add_choice4()
#             print("Choice 4 is added")
#         except NoSuchElementException:
#             print("choice 4 is not selected")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.Add_choice5()
#             print("Choice 5 is added")
#         except NoSuchElementException:
#             print("choice 5 is not selected")
#         self.driver.switch_to.default_content()
#         time.sleep(5)
#         try:
#             self.lp.click_mcq_save_changes_button()
#             print("MCQ save changes button is found & clicked")
#         except NoSuchElementException:
#             print("MCQ save changes button is not found")
#         try:
#             self.lp.click_add_3rd_question()
#             print("Add button for 3rd question is clicked")
#         except NoSuchElementException:
#             print("Add button for 3rd question is not clicked")
#         try:
#             self.lp.select_true_false_radio_button()
#             print("True false radio button is selected")
#         except NoSuchElementException:
#             print("True false radio button is not selected")
#         try:
#             self.lp.click_next_button()
#             print("Next button is clicked")
#         except NoSuchElementException:
#             print("Next button is not found or clicked")
#         time.sleep(5)
#         try:
#             self.lp.True_false_question_name()
#             print("True false Question name is Added")
#         except NoSuchElementException:
#             print("True false question name is not Added")
#         try:
#             self.lp.Add_true_false_iframe_question_text()
#             print("Select True/False is Added")
#         except NoSuchElementException:
#             print("Select True/False is not Added")
#         self.driver.switch_to.default_content()
#         try:
#             self.lp.set_true_false_marks()
#             print("True false marks is set")
#         except NoSuchElementException:
#             print("True false marks is not set")
#         try:
#             self.lp.select_correct_answer()
#             print("correct Answer is selected by faculty user")
#         except NoSuchElementException:
#             print("correct Answer is not selected by faculty user")
#         time.sleep(3)
#         try:
#             self.lp.click_true_false_save_changes_button()
#             print("True/false Save Changes Button is Clicked")
#         except NoSuchElementException:
#             print("Save Changes Button is not Clicked")
#         time.sleep(3)
#         try:
#             self.lp.click_Quiz_save_button_1()
#             print("Save Changes Button")
#         except NoSuchElementException:
#             print("save Changes Not Button")
#         time.sleep(2)
#         self.lp.click_max_grade_save()
#         self.lp.click_QA_main_adminpage()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             print(act_title)
#             assert True
#         else:
#             assert False
#         self.lp.click_gradebook_admin()
#         time.sleep(20)
#         self.lp.click_refresh_button()
#         time.sleep(5)
#         self.driver.quit()
#
#
#
#
#
#
#
# class Test_002_Login:
#     baseURL = "https://learn.datascience.berkeley.edu/"
#     username = "student3"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_Course()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_View_all_past_courses()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         self.lp.click_QA_Main()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             assert True
#         else:
#             assert False
#         self.lp.click_show_content()
#         time.sleep(2)
#         self.lp.click_created_quiz()
#         time.sleep(5)
#         self.lp.click_attempt_quiz_now()
#         time.sleep(5)
#         self.lp.click_cancel_button()
#         time.sleep(5)
#         self.lp.click_attempt_quiz_now()
#         time.sleep(5)
#         self.lp.click_start_attempt_button()
#         time.sleep(5)
#         parentHandle = self.driver.current_window_handle
#         print(parentHandle)
#         print(self.driver.title)
#         handles = self.driver.window_handles
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#             print(self.driver.title)
#             time.sleep(10)
#         self.lp.Add_answer()
#         self.driver.switch_to.default_content()
#         self.lp.click_save_continue()
#         time.sleep(3)
#         self.lp.click_radio_button_answer()
#         self.lp.click_save_continue()
#         time.sleep(3)
#         self.lp.click_select_true_radio()
#         self.lp.click_save_continue()
#         time.sleep(3)
#         self.lp.click_submit_all_and_finish_button()
#         time.sleep(3)
#         self.lp.click_cancel_button()
#         time.sleep(5)
#         self.lp.click_submit_all_and_finish_button()
#         time.sleep(5)
#         self.lp.click_submit_all_and_finish_button2()
#         time.sleep(10)
#         self.driver.back()
#         time.sleep(5)
#         self.lp.click_next_answer()
#         time.sleep(5)
#         self.lp.click_next_answer()
#         time.sleep(5)
#         self.lp.click_show_all_question()
#         time.sleep(5)
#         self.lp.click_show_one_page()
#         time.sleep(5)
#         self.lp.click_finish_review()
#         time.sleep(5)
#         self.lp.click_gradebook_link()
#         time.sleep(10)
#         self.driver.back()
#         time.sleep(5)
#         self.lp.click_back_to_the_course()
#         time.sleep(5)
#         self.driver.back()
#         time.sleep(5)
#         self.driver.quit()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Test_003_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "teacher3"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(2)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_Course()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_View_all_past_courses()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         self.lp.click_QA_Main()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             assert True
#         else:
#             assert False
#         self.lp.click_show_content()
#         time.sleep(2)
#         self.lp.click_created_quiz()
#         time.sleep(5)
#         self.lp.click_Manual_Grading()
#         time.sleep(5)
#         self.lp.click_grade_all()
#         time.sleep(5)
#         self.lp.click_comment_iframe()
#         time.sleep(3)
#         self.lp.click_comment_text()
#         self.driver.switch_to.default_content()
#         time.sleep(10)
#         self.lp.click_marks()
#         time.sleep(5)
#         self.lp.save_next_button()
#         time.sleep(2)
#         self.lp.back_to_list_of_question()
#         time.sleep(15)
#         self.lp.Go_to_gradebook_link()
#         parentHandle = self.driver.current_window_handle
#         print(parentHandle)
#         print(self.driver.title)
#         handles = self.driver.window_handles
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#             print(self.driver.title)
#             time.sleep(10)
#         self.lp.Choose_student()
#         time.sleep(15)
#         self.lp.Faculty_feedback()
#         time.sleep(5)
#         self.lp.publish_Grade()
#         time.sleep(3)
#         self.lp.Unpublish_Grade()
#         time.sleep(5)
#         self.lp.publish_Grade()
#         time.sleep(3)
#         self.lp.click_Back()
#         time.sleep(3)
#         self.lp.click_Items()
#         time.sleep(10)
#         self.lp.find_created_quiz_by_item()
#         time.sleep(10)
#         self.lp.Export_Grades()
#         time.sleep(2)
#         self.lp.Raw_data_format()
#         time.sleep(15)
#         self.lp.Export_Grades()
#         time.sleep(2)
#         self.lp.Grader_report_format()
#         time.sleep(15)
#         self.lp.Grader_report_link()
#         time.sleep(15)
#         self.lp.click_Back()
#         time.sleep(5)
#         self.lp.click_By_student()
#         time.sleep(5)
#         self.lp.Export_Grades()
#         time.sleep(2)
#         self.lp.Raw_data_format()
#         time.sleep(15)
#         self.lp.Export_Grades()
#         time.sleep(2)
#         self.lp.Grader_report_format()
#         time.sleep(15)
#         self.lp.Grader_report_link()
#         time.sleep(5)
#         self.lp.click_Back()
#         time.sleep(5)
#         self.lp.click_By_student()
#         time.sleep(30)
#         self.lp.Choose_student()
#         time.sleep(20)
#         self.lp.find_created_quiz_by_student()
#         time.sleep(10)
#         self.driver.quit()
#
#
# class Test_004_Login:
#     baseURL = "https://learn.datascience.berkeley.edu/"
#     username = "student3"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         self.lp.student_notification_page()
#         time.sleep(5)
#         self.lp.student_Quiz_notification()
#         time.sleep(10)
#         self.lp.Open_Quiz()
#         time.sleep(5)
#         parentHandle = self.driver.current_window_handle
#         print(parentHandle)
#         print(self.driver.title)
#         handles = self.driver.window_handles
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#             print(self.driver.title)
#             time.sleep(10)
#         self.lp.Review()
#         time.sleep(5)
#         self.lp.click_finish_review()
#         time.sleep(5)
#         self.lp.click_Student_QA_MAIN()
#         time.sleep(5)
#         self.lp.click_show_content()
#         time.sleep(2)
#         created_quiz = self.driver.find_element("xpath",'//li[@id="section-1"]//ul[@class="section img-text"]/li[last()]//a').text
#         print(created_quiz)
#         try:
#             self.lp.student_grade_page()
#             time.sleep(20)
#             print("Grade page is open successfully")
#             quiz_name = self.driver.find_element("//span[text()='%s']" % str(self.lp.Add_assignment_name().str2))
#             if quiz_name == created_quiz:
#                 print("Quiz is present in Grade page Successfully")
#                 time.sleep(10)
#                 self.driver.quit()
#         except NoSuchElementException:
#             print("Quiz is not present in Grade page")
#             time.sleep(10)
#             self.driver.quit()
#
#
# class Test_Edited_Quiz_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "contentadmin2"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#         self.lp = Login(self.driver)
#         try:
#             self.lp.setUserName(self.username)
#             print("Username is Entered")
#         except NoSuchElementException:
#             print("username textbox is not found")
#
#         try:
#             self.lp.ClickNext()
#             print("Next button is found and clicked")
#         except NoSuchElementException:
#             print("Next button is not found")
#
#         try:
#             self.lp.setPassword(self.password)
#             print("password id entered")
#         except NoSuchElementException:
#             print("password textbox is not found")
#
#         try:
#             self.lp.ClickSubmit()
#             print("Submit button is found and clicked")
#         except NoSuchElementException:
#             print("Submit button is not found and clicked")
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         try:
#             self.lp.Click_Course()
#             print("Click courses button is clicked")
#         except NoSuchElementException:
#             print("Click courses button is not found")
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         try:
#             self.lp.Click_View_all_past_courses()
#             print("View_all_past_courses button is clicked")
#         except NoSuchElementException:
#             print("View_all_past_courses button is not found")
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         try:
#             self.lp.Click_QA_Main_sec1()
#             print("QA main Section1 is clicked")
#         except NoSuchElementException:
#             print("QA main Section1 is not found")
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             assert True
#         else:
#             assert False
#
#         try:
#             self.lp.Click_turn_edit_on()
#             print("turn editing on button is clicked")
#         except NoSuchElementException:
#             print("turn editing on button is not found")
#         time.sleep(15)
#         self.lp.EditQuiz()
#         time.sleep(10)
#         self.lp.edit_Update_quiz()
#         time.sleep(10)
#         try:
#             self.lp.Update_assignment_name()
#             print("Assignment name is updated")
#         except NoSuchElementException:
#             print("Assignment name is not updated")
#         time.sleep(3)
#
#         try:
#             self.lp.Required_password()
#             print("Password is removed")
#         except NoSuchElementException:
#             print("Password textbox is not found")
#         time.sleep(10)
#         try:
#             self.lp.Update_editQuiz()
#             print("Save and Display Button is Clicked")
#         except NoSuchElementException:
#             print("Save and Display button is not found")
#         time.sleep(3)
#         self.lp.Go_to_gradebook_link()
#         parentHandle = self.driver.current_window_handle
#         print(parentHandle)
#         print(self.driver.title)
#         handles = self.driver.window_handles
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#             print(self.driver.title)
#             time.sleep(10)
#         self.lp.print_edited_quiz_name()
#         time.sleep(5)
#         self.driver.quit()
#
#
#
#
#
#
# class Test_Meeting_Login:
#     baseURL = "http://2vu.peabodyonline.vanderbilt.edu/"
#     username = "teacher2"
#     password = "-mF9SF^g}{&S1O"
#
#
#     def test_homePageTitle(self,setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.driver.maximize_window()
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Meeting_Icon()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "Meetings":
#             assert True
#         else:
#             assert False
#         self.lp.create_meeting()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "Create Meeting":
#             assert True
#         else:
#             assert False
#         self.lp.Topic()
#         self.lp.set_duration()
#         self.lp.set_host()
#         time.sleep(5)
#         self.lp.make_host()
#         time.sleep(5)
#         self.lp.search_invitees()
#         time.sleep(3)
#         self.lp.select_section_checkbox()
#         time.sleep(3)
#         self.lp.create_meeting_button()
#         time.sleep(10)
#         self.lp.join_meeting_button()
#         parentHandle = self.driver.current_window_handle
#         print(parentHandle)
#         handles= self.driver.window_handles
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#             print(self.driver.title)
#         time.sleep(2)
#         Keyboard.press(Key.enter)
#         self.lp.join_from_your_browser()
#         time.sleep(10)
#         self.lp.join_by_computer_audio()
#         time.sleep(5)
#         self.lp.Click_mute_audio()
#         time.sleep(15)
#         self.lp.Click_End_meeting()
#         time.sleep(1)
#         self.lp.Click_End_meeting_for_all()
#         self.driver.close()
#         time.sleep(2)
#         self.driver.switch_to.window(parentHandle)
#         time.sleep(120)
#         self.lp.View_all_upcoming_meeting()
#         time.sleep(3)
#         self.lp.click_edit_mode_button()
#         time.sleep(5)
#         self.lp.Click_Meetings_link()
#         time.sleep(3)
#         self.lp.View_all_past_meeting()
#         time.sleep(3)
#         self.lp.Click_Meetings_link()
#         time.sleep(120)
#         self.driver.refresh()
#         time.sleep(5)
#         self.lp.Click_play_video()
#
#
#
# class Test_sessionExpirationQuiz_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "contentadmin2"
#     password = "-mF9SF^g}{&S1O"
#
#
#     def test_homePageTitle(self,setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_Course()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_View_all_past_courses()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_QA_Main_sec1()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             assert True
#         else:
#             assert False
#         self.lp.Click_turn_edit_on()
#         time.sleep(3)
#         self.lp.Select_Quiz()
#         time.sleep(3)
#         self.lp.Add_Quiz_session_expiry_name()
#         time.sleep(3)
#         self.lp.Add_Quiz_session_expiry_iframe()
#         self.driver.switch_to.default_content()
#         time.sleep(3)
#         self.lp.Attempts_allowed()
#         time.sleep(2)
#         self.lp.Save_Display()
#         time.sleep(3)
#         self.lp.click_edit_quiz_button()
#         time.sleep(1)
#         self.lp.click_add_a_question()
#         time.sleep(1)
#         self.lp.click_essay_radiobutton()
#         time.sleep(1)
#         self.lp.click_next_button()
#         time.sleep(3)
#         self.lp.set_question_name()
#         time.sleep(3)
#         self.lp.Add_iframe_question_text()
#         self.driver.switch_to.default_content()
#         self.lp.set_marks()
#         self.lp.click_add_a_question()
#         self.lp.clickmcqradiobutton()
#         self.lp.click_next_button()
#         self.lp.click_mcq_question_name()
#         self.lp.Add_mcq_iframe_question_text()
#         self.driver.switch_to.default_content()
#         self.lp.set_mcq_marks()
#         self.lp.Add_choice1()
#         self.driver.switch_to.default_content()
#         self.lp.select_Choice1_marks()
#         self.lp.Add_choice2()
#         self.driver.switch_to.default_content()
#         self.lp.Add_choice3()
#         self.driver.switch_to.default_content()
#         self.lp.Add_choice4()
#         self.driver.switch_to.default_content()
#         self.lp.Add_choice5()
#         self.driver.switch_to.default_content()
#         time.sleep(5)
#         self.lp.click_mcq_save_changes_button()
#         self.lp.click_add_3rd_question()
#         self.lp.select_true_false_radio_button()
#         self.lp.click_next_button()
#         time.sleep(5)
#         self.lp.True_false_question_name()
#         self.lp.Add_true_false_iframe_question_text()
#         self.driver.switch_to.default_content()
#         self.lp.set_true_false_marks()
#         self.lp.select_correct_answer()
#         time.sleep(3)
#         self.lp.click_true_false_save_changes_button()
#         time.sleep(3)
#         self.lp.click_Quiz_save_button_1()
#         time.sleep(2)
#         self.lp.click_max_grade_save()
#         self.lp.click_QA_main_adminpage()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             print(act_title)
#             assert True
#         else:
#             assert False
#         self.lp.click_Assignmentss_Show_Content()
#         time.sleep(20)
#
#
# class Test_Student_quiz_session_expiration_Login:
#     baseURL = "https://learn.cybersecurity.berkeley.edu/login?expire_seconds=180"
#     username = "student3"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         action = ActionChains(self.driver)
#         action.send_keys(keys.Keys.ENTER)
#         time.sleep(10)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(10)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_Course()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "All Courses":
#             assert True
#         else:
#             assert False
#         self.lp.Click_View_all_past_courses()
#         time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "ISVC: My Courses":
#             assert True
#         else:
#             assert False
#         self.lp.click_QA_Main()
#         time.sleep(3)
#         act_title = self.driver.title
#         if act_title == "Course: QA Main":
#             assert True
#         else:
#             assert False
#         self.lp.click_show_content()
#         time.sleep(2)
#         self.lp.click_created_quiz()
#         time.sleep(5)
#         self.lp.click_attempt_quiz_now()
#         time.sleep(5)
#         self.lp.click_cancel_button()
#         time.sleep(5)
#         self.lp.click_attempt_quiz_now()
#         time.sleep(5)
#         self.lp.click_start_attempt_button()
#         time.sleep(5)
#         parentHandle = self.driver.current_window_handle
#         print(parentHandle)
#         print(self.driver.title)
#         handles = self.driver.window_handles
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#             print(self.driver.title)
#             time.sleep(10)
#         self.lp.Add_answer()
#         time.sleep(60)
#         self.driver.switch_to.default_content()
#         self.lp.click_save_continue()
#         time.sleep(60)
#         self.lp.click_radio_button_answer()
#         self.lp.click_save_continue()
#         time.sleep(60)
#         self.lp.click_select_true_radio()
#         self.lp.click_save_continue()
#         time.sleep(3)
#         self.lp.click_submit_all_and_finish_button()
#         time.sleep(3)
#         self.lp.click_cancel_button()
#         time.sleep(5)
#         self.lp.click_submit_all_and_finish_button()
#         time.sleep(5)
#         self.lp.click_submit_all_and_finish_button2()
#         time.sleep(10)
#         self.driver.back()
#         time.sleep(5)
#         self.lp.click_next_answer()
#         time.sleep(5)
#         self.lp.click_next_answer()
#         time.sleep(5)
#         self.lp.click_show_all_question()
#         time.sleep(5)
#         self.lp.click_show_one_page()
#         time.sleep(5)
#         self.lp.click_finish_review()
#         time.sleep(5)
#         self.driver.quit()
#
#
# class Test_Faculty_IntercomIcon_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "teacher3"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(2)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         time.sleep(5)
#         self.lp.Click_Course()
#         time.sleep(10)
#         self.lp.IntercommIconIframeicon()
#         time.sleep(10)
#         self.driver.quit()
#
#
#
# class Test_Student_IntercomIcon_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "student3"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(2)
#         act_title = self.driver.title
#         if act_title == "No Courses":
#             assert True
#         else:
#             assert False
#         time.sleep(5)
#         self.lp.Click_Course()
#         time.sleep(10)
#         self.lp.IntercommIconIframeicon()
#         time.sleep(10)
#         self.driver.quit()
#
#
#
#
#
# class Test_Faculty_Atrio_Video_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "teacher1"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         self.driver.maximize_window()
#         time.sleep(5)
#         self.lp.click_coursework_atrio()
#         time.sleep(5)
#         self.lp.select_Module_atrio()
#         time.sleep(5)
#         self.lp.select_video_lecture()
#         time.sleep(10)
#         self.lp.play_pause_Atrio_video()
#         time.sleep(2)
#         self.driver.quit()
#
#
# class Test_Student_Atrio_Video_Login:
#     baseURL = "https://learn.datascience.berkeley.edu"
#     username = "student6"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_homePageTitle(self, setup1):
#         self.driver = setup1
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         self.driver.maximize_window()
#         time.sleep(5)
#         self.lp.click_student_coursework_atrio()
#         time.sleep(5)
#         self.lp.select_Module_atrio()
#         time.sleep(5)
#         self.lp.select_video_lecture()
#         time.sleep(10)
#         self.lp.play_pause_Atrio_video()
#         time.sleep(2)
#         self.driver.quit()






class Test_Course_Player:
    baseURL = "https://learn.datascience.berkeley.edu/"
    username = "student3"
    password = "-mF9SF^g}{&S1O"

    def test_homePageTitle(self, setup1):
        self.driver = setup1
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.ClickNext()
        self.lp.setPassword(self.password)
        self.lp.ClickSubmit()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "No Courses":
            assert True
        else:
            assert False
        self.lp.Click_Course()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "All Courses":
            assert True
        else:
            assert False
        self.lp.Click_View_all_past_courses()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "ISVC: My Courses":
            assert True
        else:
            assert False
        self.lp.click_QA_Main()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Course: QA Main":
            assert True
        else:
            assert False
        self.lp.click_show_content()
        time.sleep(2)
        self.lp.Click_courseplayer()
        time.sleep(10)
        all_available_elements = self.driver.find_element("xpath", '//h1[text()="4.1 All Available Elements"]').is_displayed()
        print(all_available_elements)
