from selenium.webdriver import Chrome

def before_all(context):
    context.browser = Chrome()

def after_all(context):
    context.browser.quit()


"""
def before_scenario(context):
    ...
def before_feature(context):
    ...
def before_step(context):
    ...
#também vale para os after 
"""