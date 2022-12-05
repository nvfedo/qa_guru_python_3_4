def correct_print_function(major_name, *args):
    major_name = major_name.__name__.replace('_', ' ').title()
    print(major_name, *args)


def open_web_browser(site_name):
    correct_print_function(open_web_browser, site_name)


def go_to_companyname_homepage(page_link):
    correct_print_function(go_to_companyname_homepage, page_link)


def find_registration_button_on_login_page(page_link, button_text):
    correct_print_function(find_registration_button_on_login_page, page_link, button_text)


open_web_browser('Mozilla')
go_to_companyname_homepage('https://www.notion.so/')
find_registration_button_on_login_page('https://www.notion.so/', 'Log in')
