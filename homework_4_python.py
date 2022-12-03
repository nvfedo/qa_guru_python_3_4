def correct_print_function(major_name, *args):
    major_name = major_name.__name__.replace('_', ' ').title()
    print(major_name, *args)


def OPEN_WEB_BROWSER(site_name):
    correct_print_function(OPEN_WEB_BROWSER, site_name)


def GO_TO_COMPANYNAME_HOMEPAGE(page_link):
    correct_print_function(GO_TO_COMPANYNAME_HOMEPAGE, page_link)


def FIND_REGISTRATION_BUTTON_ON_LOGIN_PAGE(page_link, button_text):
    correct_print_function(FIND_REGISTRATION_BUTTON_ON_LOGIN_PAGE, page_link, button_text)


OPEN_WEB_BROWSER('Mozilla')
GO_TO_COMPANYNAME_HOMEPAGE('https://www.notion.so/')
FIND_REGISTRATION_BUTTON_ON_LOGIN_PAGE('https://www.notion.so/', 'Log in')
