import allure
from allure_commons.types import AttachmentType

email = 'meek22@gmail.com'
newemail = 'meek23@gmail.com'
bademail = 'test3gmail.com'
password = 'fakePassword22#'
badpassword = 'badpass'
beta = 'com.upside.consumer.android.beta:id'

@allure.severity(allure.severity_level.NORMAL)
def test_page_assertion(app_driver):
    # driver to wait 30 seconds for elements to load
    app_driver .implicitly_wait(30)

    # assert that all actionable items present, could not inspect TOS element
    assert app_driver.find_element(by='id', value=f'{beta}/login_top_image_iv').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_sign_in_with_apple_b').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_sing_in_google_b').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_sing_in_fb_b').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_sing_up_email_b').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_clickable_tv').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_in_privacy_tv').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/login_clickable_tv').is_displayed()



@allure.severity(allure.severity_level.NORMAL)
def test_sign_up_page_assertion(app_driver):
    # this test validates the input fields, buttons and warnings
    # driver to wait 30 seconds for elements to load
    app_driver.implicitly_wait(30)

    # find the sign up by email button and validate all others are displayed
    signup_btn = app_driver.find_element(by='id', value=f'{beta}/login_sing_up_email_b')
    signup_btn.click()

    #  validate email and password input fields
    assert app_driver.find_element(by='id', value=f'{beta}/sign_up_email_edit_et').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et').is_displayed()
    email_input_field = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_edit_et')
    email_input_field.click()
    assert app_driver.is_keyboard_shown()
    email_input_field.set_value(value=bademail)
    assert app_driver.find_element(by='id', value=f'{beta}/sign_up_email_message_tv')
    password_input = app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et')
    password_input.click()
    assert app_driver.is_keyboard_shown()
    password_input.set_value(value=badpassword)
    assert app_driver.find_element(by='id', value=f'{beta}/text_input_password_toggle')
    assert app_driver.find_element(by='id', value=f'{beta}/sign_up_password_stregth_text_tv')

@allure.severity(allure.severity_level.CRITICAL)
def test_signup_page_fail(app_driver):
    # same test as before except it inputs and sends test values with an email already in-use
    # this test is intended to fail
    # driver to wait 30 seconds for elements to load
    app_driver.implicitly_wait(30)
    signup_btn = app_driver.find_element(by='id', value=f'{beta}/login_sing_up_email_b')
    signup_btn.click()
    email_input_field = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_edit_et')
    email_input_field.click()
    password_input = app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et')
    password_input.click()
    email_input_field.set_value(value=email)
    password_input = app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et')
    password_input.click()
    password_input.set_value(value=password)
    app_driver.hide_keyboard()
    create_acct_btn = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_b')
    assert app_driver.find_element(by='id', value=f'{beta}/login_sing_up_email_b').is_displayed()
    create_acct_btn.click()

    # only used screenshot here to capture the failure to the report
    allure.attach(app_driver.get_screenshot_as_png(), name="testSignupFail", attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
def test_signup_page(app_driver):
    # same test as before except it inputs and sends test values with an email not in use
    # driver to wait 30 seconds for elements to load
    app_driver.implicitly_wait(30)
    signup_btn = app_driver.find_element(by='id', value=f'{beta}/login_sing_up_email_b')
    signup_btn.click()
    email_input_field = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_edit_et')
    email_input_field.click()
    password_input = app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et')
    password_input.click()
    email_input_field.set_value(value=newemail)
    password_input = app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et')
    password_input.click()
    password_input.set_value(value=password)
    app_driver.hide_keyboard()
    create_acct_btn = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_b')
    assert app_driver.find_element(by='id', value=f'{beta}/login_sing_up_email_b').is_displayed()
    create_acct_btn.click()

    # validating fuel select screen is accurate
    assert app_driver.find_element(by='id', value=f'{beta}/regular').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/midgrade').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/premium').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/diesel').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/other').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/account_details_create_account_b').is_displayed()
    # selecting fuel grade
    gas_grade_selection = app_driver.find_element(by='id', value=f'{beta}/midgrade')
    gas_grade_selection.click()
    create_acct_btn = app_driver.find_element(by='id', value=f'{beta}/account_details_create_account_b')
    create_acct_btn.click()

    # validating and accepting CC options
    assert app_driver.find_element(by='id', value=f'{beta}/viewthrough_icon_iv').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/viewthrough_maybe_later_b').is_displayed()
    assert app_driver.find_element(by='id', value=f'{beta}/viewthrough_link_your_cards_b').is_displayed()
    maybe_later_btn = app_driver.find_element(by='id', value=f'{beta}/viewthrough_maybe_later_b')
    maybe_later_btn.click()

@allure.severity(allure.severity_level.NORMAL)
def test_login_with_email(app_driver):
    # this is to validate that the account was created correctly and the user can login
    # driver to wait 30 seconds for elements to load
    app_driver.implicitly_wait(30)
    login_btn = app_driver.find_element(by='id', value=f'{beta}/login_clickable_tv')
    login_btn.click()
    email_input_field = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_edit_et')
    email_input_field.click()
    email_input_field.set_value(value=email)
    password_input = app_driver.find_element(by='id', value=f'{beta}/sign_up_password_edit_et')
    password_input.click()
    password_input.set_value(password)
    app_driver.hide_keyboard()
    create_acct_btn = app_driver.find_element(by='id', value=f'{beta}/sign_up_email_b')
    create_acct_btn.click()

    # validate main screen showing balance to ensure successful login.
    assert app_driver.find_element(by='id', value=f'{beta}/view_menu_item_balance_text_tv').is_displayed()
