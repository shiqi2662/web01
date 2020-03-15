from selenium.webdriver.common.by import By

# 一.登录元素
page_ceshi_jia = By.LINK_TEXT,"测试甲"
page_login = By.CSS_SELECTOR,"#submit"

# 二.点击测试元素
page_ceshi = By.CSS_SELECTOR,"[data-id='qa']"

# 三.点击bug元素
page_bug = By.CSS_SELECTOR,"[data-id='bug']"

# 四.点击提bug
page_bug_browses = By.CSS_SELECTOR,".pull-right>.btn-primary"

# 五.创建bug元素
# 影响版本元素
page_bug_create001 = By.CSS_SELECTOR,"#openedBuild_chosen"
# 主干元素
page_bug_create002 = By.CSS_SELECTOR,"#openedBuild_chosen [class='active-result highlighted']"

#标题元素
page_title  = By.CSS_SELECTOR,"#title"

# 保存元素
page_bug_create003 = By.CSS_SELECTOR,"#submit"


