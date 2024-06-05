import time
from datetime import date
from datetime import datetime
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
import pyperclip


class Login:
    textbox_username_id = "username"
    next_button_xpath = "//button[@id='login-submit']"
    textbox_password_id = "//input[@id='password']"
    submit_button_xpath = "//button[@id='login-submit']"
    Courses_linktext_xpath = "//a[contains(text(),'Courses')]"
    View_all_past_courses_xpath = '//a[text()="View all past courses"]'
    QA_main_sec1_xpath = "//a[contains(text(),'QA Main Section 1')]"
    Turn_edit_on_xpath ='//a[@title="Turn editing on"]'
    select_Quiz_xpath = '//li[@id="section-1"]//option[text()="Quiz"]'
    Assignment_name_xpath = '//input[@id="id_name"]'
    iframe_window_xpath = '//table[@id="id_introeditor_tbl"]//iframe'
    iframe_text_xpath = '//body[@id="tinymce"]'
    save_display_button_xpath = '/html/body/div[3]/main/div/div[1]/div/div/div[1]/div/form/fieldset[11]/div/div[1]/fieldset/input[2]'
    meeting_icon_xpath = '//a[@class="_28qln cPcrj _1X-fp xsceX _1Ueot _30o9j _1uj2V _1cYoe _1yCC2"]/*'
    create_meeting_xpath = "//button[contains(text(),'Create Meeting')]"
    Topic_xpath = '//div[@class="meeting__form-group--label-and-input"]//input[@formcontrolname="topic"]'
    Duration_xpath = '//input[@formcontrolname="duration"]'
    Host_xpath = '//input[@id="host"]'
    select_host_xpath = '//div[@id="mat-autocomplete-0"]'
    make_host_xpath = '//button/i[text()="person"]'
    invitees_xpath = '//input[@id="invitees"]'
    select_checkbox1_xpath = '//input[@id="588e89ab-e884-4a5d-b949-95ac8c833998"]'
    select_checkbox2_xpath = '//input[@id="d981422d-8e74-4caf-b0d9-e22eb4174d26"]'
    create_meeting_button_xpath = '//button[@aria-label="create meeting"]'
    join_meeting_xpath = '//button[text()="Join Meeting "]'
    Join_from_your_browser_xpath = '//a[text()="Join from Your Browser"]'
    Join_by_computer_audio_xpath = '//button[text()="Join Audio by Computer"]'
    mute_audio_xpath = '//button[@class="footer-button-base__button ax-outline join-audio-container__btn"]'
    End_meeting_xpath = '//button[text()="End"]'
    End_meeting_for_All_xpath = '//button[text()="End Meeting for All"]'
    View_all_upcoming_meeting_xpath = '//a[@href="#/meetings/upcoming_meetings"]'
    Meetings_xpath = '//a[text()="Meetings"]'
    View_all_past_meeting_xpath = '//a[@href="#/meetings/past_meetings"]'
    play_arrow_xpath = '//span[text()="play_arrow"]'
    click_play_button_xpath = '//button[@class = "vjs-play-control vjs-control vjs-button"]//span[@class="vjs-icon-placeholder"]'
    click_edit_mode_xpath = '//tbody/tr[1]/td[5]/a[1]/span[1]'
    click_delete_meeting_button_xpath = '//button[text()="Delete Meeting " and @aria-label="Delete Meeting"]'
    click_delete_meeting_popup_xpath = '//button[text()="Delete Meeting " and @class="button button--danger"]'
    click_edit_quiz_xpath = '//input[@value= "Edit quiz"]'
    click_add_question_xpath = "//input[@value = 'Add a question ...' and @type='button']"
    click_essay_radio_xpath = '//input[@id="qtype_essay"]'
    click_next_xpath = "//input[@id='chooseqtype_submit']"
    Question_name_xpath = '//input[@id="id_name"]'
    iframe_question_text_xpath = '//table[@id="id_questiontext_tbl"]//iframe'
    defaultmark_xpath = '//input[@id="id_defaultmark"]'
    savechanges_button_xpath = '//input[@id="id_submitbutton"]'
    mcq_radiobutton_xpath = '//input[@id="qtype_multichoice"]'
    mcq_question_name_xpath = '//input[@id="id_name"]'
    iframe_mcq_question_text_xpath = '//iframe[@id="id_questiontext_ifr"]'
    choice1_iframe_xpath = '//iframe[@id="id_answer_0_ifr"]'
    choice1_xpath = "//select[@id='id_fraction_0']//option[@value='1.0']"
    choice2_iframe_xpath = '//iframe[@id="id_answer_1_ifr"]'
    choice3_iframe_xpath = '//iframe[@id="id_answer_2_ifr"]'
    choice4_iframe_xpath = '//iframe[@id="id_answer_3_ifr"]'
    choice5_iframe_xpath = '//iframe[@id="id_answer_4_ifr"]'
    mcq_save_changes_button_xpath = '//input[@id="id_submitbutton"]'
    add_3rd_question_xpath = '//input[@onclick="return submitAddQuestion(2)"]'
    true_false_button_xpath = '//input[@id="qtype_truefalse"]'
    question_name_true_false_xpath = '//input[@id="id_name"]'
    correct_answer_xpath = '//select[@id="id_correctanswer"]/option[@value="1"]'
    true_false_save_changes_button_xpath = '//input[@id="id_submitbutton"]'
    Quiz_save_button_1_xpath = '//input[@class="pointssubmitbutton"]'
    max_grade_save_xpath = '//fieldset/input[@value="Save"]'
    QA_main_page_xpath = '//div[@id="onlineCampusApp"]/nav/a/span'
    gradebook_admin_xpath = '//a[text()="gradebook admin"]'
    refresh_button_xpath = "//button[@class='button btn__icon--small']/i"
    coursework_xpath = '//a[text()="Coursework"]'
    avtar_xpath = '//button[@aria-label="Profile Menu"]'
    admin_logout_xpath = '//a[@href="/logout"]'
    QA_main_xpath = '//a[@href="https://learn.datascience.berkeley.edu/course/view.php?id=16&group=23&page=coursework"]'
    show_content_xpath = '//a[@aria-label="Assignmentss"]'
    created_Quiz_xpath = '//li[@id="section-1"]//ul[@class="section img-text"]/li[last()]//a'
    attempt_quiz_now_xpath = '//input[@value="Attempt quiz now"]'
    Confirmation_dialog_box = '//div[@id="confirmdialog"]'
    Cancel_button_xpath = "//div[@id='confirmdialog']//span//button[text()='Cancel']"
    start_attempt_button_xpath = "//div[@id='confirmdialog']//span//button[text()='Start attempt']"
    continue_last_attempt_xpath = '//div[@class="box quizattempt"]//form//input[@value="Continue the last attempt"]'
    iframe_window_answer_xpath = '//div[@class="answer"]//iframe'
    save_continue_xpath = '//input[@name="next"]'
    radio_button_answer_xpath = '//div[@class="r0"]//input[@value="0"]'
    select_true_radio_xpath = '//div[@class="r0"]//input'
    submit_all_and_finish_button_xpath = '//input[@value="Submit all and finish"]'
    submit_all_and_finish_button_xpath2 = '//button[text()="Submit all and finish"]'
    click_next_answer_xpath = '//a[@title="Next"]'
    click_show_all_question_xpath = '//a[text()="Show all questions on one page"]'
    click_show_one_page_xpath = '//a[text()="Show one page at a time"]'
    click_finish_review_xpath = '//a[text()="Finish review"]'
    click_gradebook_link_xpath = '//a[text()="gradebook"]'
    click_back_to_the_course_xpath = '//input[@value="Back to the course"]'
    click_Manual_Grading_xpath = '//a[text()="Manual Grading"]'
    click_grade_all_xpath = '//a[text()="grade all"]'
    comment_iframe_xpath = '//td//iframe'
    comment_text_xpath = '//body[@id="tinymce"]'
    marks_xpath = '//div[@class="comment"]//input[@type="text"]'
    save_next_button_xpath = '//input[@value="Save and go to next page"]'
    back_to_list_of_question_xpath = '//div[@id="region-main"]/div/p/a'
    Go_to_gradebook_link_xpath = '//div[@id="region-main-wrap"]//a[text()="Go to Gradebook to publish scores to students »"]'
    Choose_student_xpath = '//a[text()="Royster, Tammy"]'
    Faculty_feedback_xpath = '//div[@class="fr-element fr-view"]'
    publish_Grade_xpath = '//button[text()="Publish"]'
    Unpublish_Grade_xpath = '//button[text()="Unpublish"]'
    Back_xpath = '//span[@aria-label="Back"]'
    click_Items_xpath = '//a[text()="Items"]'
    Export_Grades_xpath = '//button[text()="Export Grades"]'
    Raw_data_format_xpath = '//a[text()="Raw data format"]'
    Grader_report_format_xpath = '//a[text()="Grader Report format"]'
    Grader_report_link_xpath = '//a[text()="Grader Report"]'
    click_By_student_xpath = '//input[@id="By Student"]'
    student_notification_page_xpath = '//a[@href="/notifications/all_notifications.php"]'
    student_Quiz_notification_xpath = '//div[@id="region-main"]/div/div/div/div[1]/a[1]'
    BACK_TO_GRADES_XPATH = '//span[text()="BACK TO GRADES"]'
    Open_Quiz_xpath = '//a[@target="blank"]'
    Review_xpath = '//a[text()="Review"]'
    student_click_QA_main_xpath = '//a[@class="coursework-link"]'
    Attempts_allowed_xpath = '//select[@id="id_attempts"]/option[@value="0"]'
    Assignmentss_Show_Content_xpath = '//a[@class="showdetails" and @aria-label ="Assignmentss"]'
    Required_password_xpath = '//input[@name="quizpassword"]'
    Required_password_checkbox_xpath ='//input[@id="id_quizpasswordunmask"]'
    find_created_quiz_xpath_by_item = '//a[text()=" Automation Quiz testing "]'
    find_created_quiz_xpath_by_student = '//span[text()="Automation Quiz testing"]'
    get_Quiz_attempted_Student_name_text_xpath = '//h4'
    intercomm_icon_iframe_xpath = "//body/div[@id='intercom-container']/div[1]/div[2]/iframe[1]"
    intercom_icon_click_xpath = '//*[@id="intercom-container"]/div/div[@data-testid]'
    Click_courseplayer_xpath = '//span[@class="instancename" and text()="Course Player (DS Only)"]'



    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)

    def ClickNext(self):
        self.driver.find_element("xpath",self.next_button_xpath).click()

    def setPassword(self,password):
        self.driver.find_element("xpath",self.textbox_password_id).send_keys(password)

    def ClickSubmit(self):
        self.driver.find_element("xpath",self.submit_button_xpath).click()

    def Click_Course(self):
        self.driver.find_element("xpath",self.Courses_linktext_xpath).click()

    def Click_View_all_past_courses(self):
        self.driver.find_element("xpath",self.View_all_past_courses_xpath).click()

    def Click_QA_Main_sec1(self):
        self.driver.find_element("xpath",self.QA_main_sec1_xpath).click()

    def Click_turn_edit_on(self):
        self.driver.find_element("xpath",self.Turn_edit_on_xpath).click()

    def Select_Quiz(self):
        self.driver.find_element("xpath",self.select_Quiz_xpath).click()

    def Add_assignment_name(self):
        #today = date.today()
        now = datetime.now()
        #d2 = today.strftime(" %B %d, %Y")
        d2 = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("Automation Quiz testing", d2)
        str1 = "Automation Quiz testing"
        timestamp = str(d2)
        print("timestamp value of d2=", timestamp)
        str2 = str1 + timestamp
        print("value of str2= ", str2)
        self.driver.find_element("xpath",self.Assignment_name_xpath).send_keys(str2)
        # Assignment_name = self.driver.find_element("xpath",self.Assignment_name_xpath).text
        # print(Assignment_name , "this is my Assignment name ")

    def Update_assignment_name(self):
        now = datetime.now()
        d2 = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("Edit Automation Quiz testing", d2)
        str1 = "Edit Automation Quiz testing", d2
        self.driver.find_element("xpath", self.Assignment_name_xpath).clear()
        self.driver.find_element("xpath", self.Assignment_name_xpath).send_keys(str1)

    def Update_editQuiz(self):
        self.driver.find_element("xpath",'//input[@id="id_submitbutton"]').click()


    def Add_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.iframe_window_xpath))
        today = date.today()
        d2 = today.strftime(" %B %d, %Y")
        print("Automation Quiz testing", d2)
        self.driver.find_element("xpath",self.iframe_text_xpath).send_keys("Automation Quiz testing", d2)

    def Required_password(self):
        self.driver.find_element("xpath",self.Required_password_xpath).clear()

    def Add_Quiz_session_expiry_name(self):
        self.driver.find_element("xpath",self.Assignment_name_xpath).send_keys("Automation Quiz Session Expiration testing")

    def Add_Quiz_session_expiry_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.iframe_window_xpath))
        self.driver.find_element("xpath",self.iframe_text_xpath).send_keys("Automation Quiz Session Expiration testing")

    def IntercommIconIframeicon(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.intercomm_icon_iframe_xpath))
        self.driver.find_element("xpath", self.intercom_icon_click_xpath).click()
        print("Chat icon is Open Successfully")
        time.sleep(5)
        self.driver.find_element("xpath", self.intercom_icon_click_xpath).click()
        print("Chat icon is close Successfully")


    def Attempts_allowed(self):
        self.driver.find_element("xpath",self.Attempts_allowed_xpath).click()

    def Save_Display(self):
        self.driver.find_element("xpath",self.save_display_button_xpath).click()

    def Meeting_Icon(self):
        self.driver.find_element("xpath", self.meeting_icon_xpath).click()

    def create_meeting(self):
        self.driver.find_element("xpath",self.create_meeting_xpath).click()

    def Topic(self):
        self.driver.find_element("xpath",self.Topic_xpath).send_keys("Meeting Test")

    def set_duration(self):
        self.driver.find_element("xpath",self.Duration_xpath).send_keys("2")

    def set_host(self):
        self.driver.find_element("xpath",self.Host_xpath).click()
        self.driver.find_element("xpath", self.Host_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element("xpath", self.Host_xpath).send_keys(Keys.ENTER)

    def make_host(self):
        self.driver.find_element("xpath", self.make_host_xpath).click()

    def search_invitees(self):
        self.driver.find_element("xpath",self.invitees_xpath).click()

    def select_section_checkbox(self):
        self.driver.find_element("xpath",self.select_checkbox1_xpath).click()
        self.driver.find_element("xpath",self.select_checkbox2_xpath).click()

    def create_meeting_button(self):
        self.driver.find_element("xpath",self.create_meeting_button_xpath).click()

    def join_meeting_button(self):
        self.driver.find_element("xpath",self.join_meeting_xpath).click()

    def join_from_your_browser(self):
        self.driver.find_element("xpath",self.Join_from_your_browser_xpath).click()

    def join_by_computer_audio(self):
        self.driver.find_element("xpath", self.Join_by_computer_audio_xpath).click()

    def Click_mute_audio(self):
        self.driver.find_element("xpath", self.mute_audio_xpath).click()

    def Click_End_meeting(self):
        self.driver.find_element("xpath", self.End_meeting_xpath).click()

    def Click_End_meeting_for_all(self):
        self.driver.find_element("xpath", self.End_meeting_for_All_xpath).click()

    def View_all_upcoming_meeting(self):
        self.driver.find_element("xpath", self.View_all_upcoming_meeting_xpath).click()

    def Click_Meetings_link(self):
        self.driver.find_element("xpath", self.Meetings_xpath).click()

    def View_all_past_meeting(self):
        self.driver.find_element("xpath", self.View_all_past_meeting_xpath).click()

    def Click_play_video(self):
        self.driver.find_element("xpath",self.play_arrow_xpath).click()

    def click_play_button(self):
        self.driver.find_element("xpath",self.click_play_button_xpath).click()

    def click_edit_mode_button(self):
        self.driver.find_element("xpath",self.click_edit_mode_xpath).click()

    def click_delete_meeting(self):
        self.driver.find_element("xpath",self.click_delete_meeting_button_xpath).click()
        self.driver.find_element("xpath",self.click_delete_meeting_popup_xpath).click()

    def click_edit_quiz_button(self):
        self.driver.find_element("xpath",self.click_edit_quiz_xpath).click()

    def click_add_a_question(self):
        self.driver.find_element("xpath",self.click_add_question_xpath).click()

    def click_essay_radiobutton(self):
        self.driver.find_element("xpath",self.click_essay_radio_xpath).click()

    def click_next_button(self):
        self.driver.find_element("xpath",self.click_next_xpath).click()

    def set_question_name(self):
        self.driver.find_element("xpath",self.Question_name_xpath).send_keys('Essay Writing1')

    def Add_iframe_question_text(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.iframe_question_text_xpath))
        self.driver.find_element("xpath",self.iframe_text_xpath).send_keys("Write an essay")

    def set_marks(self):
        self.driver.find_element("xpath", self.defaultmark_xpath).clear()
        self.driver.find_element("xpath",self.defaultmark_xpath).send_keys('5')
        self.driver.find_element("xpath",self.savechanges_button_xpath).click()

    def clickmcqradiobutton(self):
        self.driver.find_element("xpath",self.mcq_radiobutton_xpath).click()

    def click_mcq_question_name(self):
        self.driver.find_element("xpath",self.mcq_question_name_xpath).send_keys('MCQ')

    def Add_mcq_iframe_question_text(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.iframe_mcq_question_text_xpath))
        self.driver.find_element("xpath",self.iframe_text_xpath).send_keys('What is Lion?')

    def set_mcq_marks(self):
        self.driver.find_element("xpath", self.defaultmark_xpath).clear()
        self.driver.find_element("xpath",self.defaultmark_xpath).send_keys('3')

    def Add_choice1(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.choice1_iframe_xpath))
        self.driver.find_element("xpath", self.iframe_text_xpath).send_keys("Animal")

    def select_Choice1_marks(self):
        self.driver.find_element("xpath",self.choice1_xpath).click()

    def Add_choice2(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.choice2_iframe_xpath))
        self.driver.find_element("xpath", self.iframe_text_xpath).send_keys("Human")

    def Add_choice3(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.choice3_iframe_xpath))
        self.driver.find_element("xpath", self.iframe_text_xpath).send_keys("Bird")

    def Add_choice4(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.choice4_iframe_xpath))
        self.driver.find_element("xpath", self.iframe_text_xpath).send_keys("Fish")

    def Add_choice5(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.choice5_iframe_xpath))
        self.driver.find_element("xpath", self.iframe_text_xpath).send_keys("Tree")

    def click_mcq_save_changes_button(self):
        self.driver.find_element("xpath",self.mcq_save_changes_button_xpath).click()

    def click_add_3rd_question(self):
        self.driver.find_element("xpath",self.add_3rd_question_xpath).click()

    def select_true_false_radio_button(self):
        self.driver.find_element("xpath",self.true_false_button_xpath).click()

    def True_false_question_name(self):
        self.driver.find_element("xpath", self.question_name_true_false_xpath).send_keys("True or False")

    def Add_true_false_iframe_question_text(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.iframe_mcq_question_text_xpath))
        self.driver.find_element("xpath", self.iframe_text_xpath).send_keys('select True?')

    def set_true_false_marks(self):
        self.driver.find_element("xpath", self.defaultmark_xpath).clear()
        self.driver.find_element("xpath", self.defaultmark_xpath).send_keys('2')

    def select_correct_answer(self):
        self.driver.find_element("xpath", self.correct_answer_xpath).click()

    def click_true_false_save_changes_button(self):
        self.driver.find_element("xpath", self.true_false_save_changes_button_xpath).click()

    def click_Quiz_save_button_1(self):
        self.driver.find_element("xpath",self.Quiz_save_button_1_xpath).click()

    def click_max_grade_save(self):
        self.driver.find_element("xpath",self.max_grade_save_xpath).click()

    def click_QA_main_adminpage(self):
        self.driver.find_element("xpath",self.QA_main_page_xpath).click()

    def click_gradebook_admin(self):
        self.driver.find_element("xpath",self.gradebook_admin_xpath).click()

    def click_refresh_button(self):
        self.driver.find_element("xpath",self.refresh_button_xpath).click()

    def click_coursework_adminpage(self):
        self.driver.find_element("xpath",self.coursework_xpath).click()

    def click_avtar(self):
        self.driver.find_element("xpath",self.avtar_xpath).click()

    def click_sign_out(self):
        self.driver.find_element("xpath",self.admin_logout_xpath).click()

    def click_QA_Main(self):
        self.driver.find_element("xpath",self.QA_main_xpath).click()

    def click_show_content(self):
        self.driver.find_element("xpath", self.show_content_xpath).click()

    def click_created_quiz(self):
        self.driver.find_element("xpath",self.created_Quiz_xpath).click()

    def click_attempt_quiz_now(self):
        self.driver.find_element("xpath",self.attempt_quiz_now_xpath).click()

    def click_cancel_button(self):
        self.driver.find_element("xpath",self.Cancel_button_xpath).click()

    def click_start_attempt_button(self):
        self.driver.find_element("xpath",self.start_attempt_button_xpath).click()

    def click_continue_last_attempt(self):
        self.driver.find_element("xpath",self.continue_last_attempt_xpath).click()

    def Add_answer(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.iframe_window_answer_xpath))
        self.driver.find_element("xpath",self.iframe_text_xpath).send_keys("test")

    def click_save_continue(self):
        self.driver.find_element("xpath",self.save_continue_xpath).click()

    def click_radio_button_answer(self):
        self.driver.find_element("xpath",self.radio_button_answer_xpath).click()

    def click_select_true_radio(self):
        self.driver.find_element("xpath",self.select_true_radio_xpath).click()

    def click_submit_all_and_finish_button(self):
        self.driver.find_element("xpath",self.submit_all_and_finish_button_xpath).click()

    def click_submit_all_and_finish_button2(self):
        self.driver.find_element("xpath",self.submit_all_and_finish_button_xpath2).click()

    def click_next_answer(self):
        self.driver.find_element("xpath",self.click_next_answer_xpath).click()

    def click_show_all_question(self):
        self.driver.find_element("xpath",self.click_show_all_question_xpath).click()

    def click_show_one_page(self):
        self.driver.find_element("xpath",self.click_show_one_page_xpath).click()

    def click_finish_review(self):
        self.driver.find_element("xpath",self.click_finish_review_xpath).click()

    def click_gradebook_link(self):
        self.driver.find_element("xpath",self.click_gradebook_link_xpath).click()

    def click_back_to_the_course(self):
        self.driver.find_element("xpath",self.click_back_to_the_course_xpath).click()

    def click_Manual_Grading(self):
        self.driver.find_element("xpath",self.click_Manual_Grading_xpath).click()

    def click_grade_all(self):
        self.driver.find_element("xpath",self.click_grade_all_xpath).click()

    def click_comment_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.comment_iframe_xpath))

    def click_comment_text(self):
        self.driver.find_element("xpath", self.comment_text_xpath).clear()
        self.driver.find_element("xpath",self.comment_text_xpath).send_keys("Good")

    def click_marks(self):
        self.driver.find_element("xpath",self.marks_xpath).clear()
        self.driver.find_element("xpath",self.marks_xpath).send_keys("3")

    def save_next_button(self):
        self.driver.find_element("xpath",self.save_next_button_xpath).click()

    def back_to_list_of_question(self):
        self.driver.find_element("xpath",self.back_to_list_of_question_xpath).click()

    def Go_to_gradebook_link(self):
        self.driver.find_element("xpath",self.Go_to_gradebook_link_xpath).click()

    def Choose_student(self):
        self.driver.find_element("xpath",self.Choose_student_xpath).click()


    def Faculty_feedback(self):
        self.driver.find_element("xpath", self.Faculty_feedback_xpath).clear()
        self.driver.find_element("xpath",self.Faculty_feedback_xpath).send_keys("QA Test")

    def publish_Grade(self):
        self.driver.find_element("xpath",self.publish_Grade_xpath).click()

    def Unpublish_Grade(self):
        self.driver.find_element("xpath",self.Unpublish_Grade_xpath).click()


    def click_Back(self):
        self.driver.find_element("xpath",self.Back_xpath).click()

    def click_Items(self):
        self.driver.find_element("xpath",self.click_Items_xpath).click()

    def Export_Grades(self):
        self.driver.find_element("xpath",self.Export_Grades_xpath).click()

    def Raw_data_format(self):
        self.driver.find_element("xpath",self.Raw_data_format_xpath).click()

    def Grader_report_format(self):
        self.driver.find_element("xpath",self.Grader_report_format_xpath).click()

    def Grader_report_link(self):
        self.driver.find_element("xpath",self.Grader_report_link_xpath).click()

    def click_By_student(self):
        self.driver.find_element("xpath",self.click_By_student_xpath).click()

    def student_notification_page(self):
        self.driver.find_element("xpath",self.student_notification_page_xpath).click()

    def student_Quiz_notification(self):
        self.driver.find_element("xpath",self.student_Quiz_notification_xpath).click()

    def BACK_TO_GRADES(self):
        self.driver.find_element("xpath",self.BACK_TO_GRADES_XPATH).click()

    def Open_Quiz(self):
        self.driver.find_element("xpath",self.Open_Quiz_xpath).click()

    def Review(self):
        self.driver.find_element("xpath",self.Review_xpath).click()

    def click_Student_QA_MAIN(self):
        self.driver.find_element("xpath",self.student_click_QA_main_xpath).click()

    def click_Assignmentss_Show_Content(self):
        self.driver.find_element("xpath",self.Assignmentss_Show_Content_xpath).click()

    def find_created_quiz_by_item(self):
        text = self.driver.find_element("xpath", self.find_created_quiz_xpath_by_item).text
        print(text , "is present in By Item list")

    def find_created_quiz_by_student(self):
        text = self.driver.find_element("xpath", self.find_created_quiz_xpath_by_student).text
        print(text , "is present in By student list")

    def student_grade_page(self):
        self.driver.find_element("xpath", '//*[@id="onlineCampusApp"]//a[text()="grades"]').click()

    def EditQuiz(self):
        self.driver.find_element("xpath", '//h3[text()="Assignmentss"]//..//div[@class="showhide_section"]//a').click()

    def click_coursework_atrio(self):
        self.driver.find_element("xpath", '//span[text()="Coursework"]').click()

    def click_student_coursework_atrio(self):
        self.driver.find_element("xpath", '//a[text()="Coursework"]').click()

    def select_Module_atrio(self):
        self.driver.find_element("xpath", '//div[text()="1: Importance of Experimentation"]//..//..//a').click()

    def select_video_lecture(self):
        self.driver.find_element("xpath", '//a[text()="1.1 Introduction to Week 1"]').click()

    def edit_Update_quiz(self):
        self.driver.find_element("xpath", '//li[@id="section-1"]//ul[@class="section img-text"]/li[last()]//a[@class="editing_update"]').click()

    def print_edited_quiz_name(self):
        Edited_quiz_name = self.driver.find_element("xpath","//h2").text
        print(Edited_quiz_name)

    def play_pause_Atrio_video(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", '//iframe[@role="main"]'))
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Play"]').click()
        time.sleep(10)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Pause"]').click()
        time.sleep(5)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Play"]').click()
        time.sleep(10)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Show closed captions"]').click()
        time.sleep(5)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Hide closed captions"]').click()
        time.sleep(5)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Fullscreen"]').click()
        time.sleep(2)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Non-Fullscreen"]').click()
        time.sleep(2)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Mute"]').click()
        time.sleep(5)
        self.driver.find_element("xpath", '//*[local-name()="button" and @title="Unmute"]').click()
        time.sleep(5)
        self.driver.find_element("xpath", '//button[@id="copy-to-clipboard"]')
        self.driver.find_element("xpath", '//button[@id="copy-to-clipboard"]').click()
        text = pyperclip.paste()
        print(text)
        time.sleep(5)

    def Click_courseplayer(self):
        self.driver.find_element("xpath", '//span[@class="instancename" and text()="Course Player (DS Only)"]').click()


























