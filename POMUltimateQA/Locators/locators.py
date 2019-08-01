class Locators():


    #-header
    title_text = "Ultimate QA"
    sign_in_link = "/users/sign_in"

    # -footer
    home_page_link = "href = /" #??
    all_courses_linkText = "/collections" #??

    # login page objects:
    #body
    email_textbox_id = "user[email]"
    password_textbox_id = "user[password]"

    incorrect_credentials_classText = "form-error__list-item"

    remember_checkbox_id = "user[remember_me]"
    forgot_password_linkText = "/users/password/new"

    sign_in_button_id = "sign-in"
    alternative_sign_in_class = "fa fa-linkedin" #??

    new_acc_linkText = "/users/sign_up"


    #forgot password body objects:
    #body
    forgot_password_textbox_id = "user[email]"
    submit_nameText = "commit"

    #sign up body objects:
    first_name_textbox_id = "user[first_name]"
    last_name_textbox_id = "user[last_name]"
    new_user_email_textbox_id = "user[email]"
    new_user_password_textbox_id = "user[password]"
    agreement_checkbox_id = "user[terms]"
    privacy_linkText = "/pages/privacy"
    new_acc_sign_up_id = "sign-up"





